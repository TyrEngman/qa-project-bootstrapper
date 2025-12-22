from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


PRESETS = ["default", "api", "ui", "minimal"]


def _is_windows() -> bool:
    return sys.platform.startswith("win")


def _venv_python(venv_dir: Path) -> Path:
    if _is_windows():
        return venv_dir / "Scripts" / "python.exe"
    return venv_dir / "bin" / "python"


def _run(cmd: list[str], cwd: Path) -> None:
    print(f"\n[CMD] {' '.join(cmd)}")
    subprocess.run(cmd, cwd=str(cwd), check=True)


def _run_ui_playwright_install(py: Path, project_dir: Path) -> None:
    """
    ROBUSTO:
    - En Linux CI: usa --with-deps para evitar faltantes en runners limpios.
    - En Windows/macOS local: install normal.
    """
    if sys.platform.startswith("linux"):
        _run([str(py), "-m", "playwright", "install", "--with-deps"], cwd=project_dir)
    else:
        _run([str(py), "-m", "playwright", "install"], cwd=project_dir)


def main() -> int:
    repo_root = Path(__file__).parent.resolve()
    qa_init = repo_root / "qa_init.py"

    if not qa_init.exists():
        print("ERROR: qa_init.py not found in repo root.")
        return 1

    temp_root = Path(tempfile.mkdtemp(prefix="bootstrapper_sanity_"))
    print(f"\n[INFO] Temp workspace: {temp_root}")

    try:
        for preset in PRESETS:
            project_dir = temp_root / f"demo_{preset}"
            print("\n" + "=" * 90)
            print(f"[INFO] Preset: {preset}")
            print(f"[INFO] Generating: {project_dir}")

            # 1) Generar proyecto
            _run([sys.executable, str(qa_init), str(project_dir), "--preset", preset], cwd=repo_root)

            # 2) Crear venv dentro del proyecto generado
            venv_dir = project_dir / ".venv"
            _run([sys.executable, "-m", "venv", str(venv_dir)], cwd=project_dir)

            py = _venv_python(venv_dir)
            if not py.exists():
                print(f"ERROR: venv python not found at: {py}")
                return 1

            # 3) pip install requirements
            _run([str(py), "-m", "pip", "install", "--upgrade", "pip"], cwd=project_dir)
            _run([str(py), "-m", "pip", "install", "-r", "requirements.txt"], cwd=project_dir)

            # 4) Si es UI: instalar browsers (robusto por OS)
            if preset == "ui":
                _run_ui_playwright_install(py, project_dir)

            # 5) correr pytest
            _run([str(py), "-m", "pytest", "-q"], cwd=project_dir)

            print(f"[OK] Preset '{preset}' passed ✅")

        print("\n" + "=" * 90)
        print("[SUCCESS] All presets passed ✅")
        return 0

    except subprocess.CalledProcessError as e:
        print("\n" + "=" * 90)
        print("[FAIL] A command failed ❌")
        print(f"Return code: {e.returncode}")
        return e.returncode

    finally:
        # Limpieza automática
        shutil.rmtree(temp_root, ignore_errors=True)
        print(f"\n[INFO] Temp workspace cleaned: {temp_root}")


if __name__ == "__main__":
    raise SystemExit(main())
