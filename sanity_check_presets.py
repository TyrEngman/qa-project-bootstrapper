import os
import shutil
import subprocess
import sys
from pathlib import Path

# Ruta base del repo (donde está qa_init.py)
BASE_DIR = Path(__file__).parent

# Escenarios a probar: (nombre_carpeta, args_para_qa_init)
SCENARIOS = [
    ("sanity_default", []),                          # preset default
    ("sanity_api", ["--preset", "api"]),             # preset api
    ("sanity_ui", ["--preset", "ui"]),               # preset ui
    ("sanity_minimal", ["--preset", "minimal", "--no-ci"]),  # preset minimal sin CI
]


def run(cmd, cwd=None):
    """Ejecuta un comando y lo muestra en consola."""
    print(f"\n$ {' '.join(str(c) for c in cmd)}")
    subprocess.run(cmd, cwd=cwd, check=True)


def get_venv_python(project_path: Path) -> Path:
    """Devuelve la ruta al python del .venv dentro del proyecto."""
    if os.name == "nt":
        # Windows
        return project_path / ".venv" / "Scripts" / "python.exe"
    else:
        # macOS / Linux
        return project_path / ".venv" / "bin" / "python"


def sanity_check_scenario(project_name: str, extra_args: list[str]) -> bool:
    """Ejecuta el sanity check para un preset.

    1) Borra carpeta si ya existe.
    2) Genera proyecto con qa_init.py.
    3) Crea .venv.
    4) Instala requirements.
    5) Corre pytest -v.

    Devuelve True si todo sale bien, False si falla algo.
    """
    project_path = BASE_DIR / project_name

    print("\n" + "=" * 80)
    print(f"🔎 Running sanity check for scenario: {project_name}")
    print("=" * 80)

    # 1) Borrar carpeta previa si existe
    if project_path.exists():
        print(f"🧹 Removing existing folder: {project_path}")
        shutil.rmtree(project_path)

    try:
        # 2) Generar proyecto con qa_init.py
        cmd_init = [sys.executable, "qa_init.py", project_name] + extra_args
        run(cmd_init, cwd=BASE_DIR)

        # 3) Crear .venv dentro del proyecto
        print(f"\n📦 Creating virtualenv in: {project_path / '.venv'}")
        run([sys.executable, "-m", "venv", ".venv"], cwd=project_path)

        # 4) Instalar requirements
        venv_python = get_venv_python(project_path)
        print(f"\n📥 Installing requirements using: {venv_python}")
        run([str(venv_python), "-m", "pip", "install", "-r", "requirements.txt"], cwd=project_path)

        # 5) Correr pytest -v
        print("\n🧪 Running pytest -v")
        run([str(venv_python), "-m", "pytest", "-v"], cwd=project_path)

        print(f"\n✅ Scenario '{project_name}' PASSED")
        return True

    except subprocess.CalledProcessError as e:
        print(f"\n❌ Scenario '{project_name}' FAILED with return code {e.returncode}")
        return False


def main():
    print("\n🚀 QA Project Bootstrapper – Sanity check for presets")
    print("   (default, api, ui, minimal)\n")

    results = []

    for name, args in SCENARIOS:
        ok = sanity_check_scenario(name, args)
        results.append((name, ok))

    print("\n" + "#" * 80)
    print("📊 SANITY CHECK SUMMARY")
    print("#" * 80)

    for name, ok in results:
        status = "✅ OK" if ok else "❌ FAIL"
        print(f"- {name}: {status}")

    # Si quieres que el script devuelva error global si algo falla:
    if not all(ok for _, ok in results):
        print("\nSome scenarios FAILED. Please review the logs above.")
        sys.exit(1)

    print("\nAll scenarios PASSED. Bootstrapper looks healthy! 🎉")


if __name__ == "__main__":
    main()