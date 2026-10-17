#!/usr/bin/env python3
"""
render.py - Runner multiplataforma de renderizado y pruebas para Manim.
Grupo 3 - MAT1188 Cálculo Intermedio (EID)

Resuelve automáticamente los problemas de PYTHONPATH y simplifica la
ejecución de las escenas tanto por línea de comandos (CLI) como mediante
un menú interactivo en consola.

Uso CLI rápido:
    python render.py 1              # Escena 1 en 480p (-pql)
    python render.py 2 -H           # Escena 2 en 1080p (-pqh)
    python render.py 3 --high       # Escena 3 en 1080p (-pqh)
    python render.py verify         # Ejecutar auditoría matemática
    python render.py test           # Ejecutar pruebas unitarias
    python render.py -h             # Muestra la ayuda
    python render.py                # Modo menú interactivo
"""

import os
import sys
import subprocess
from pathlib import Path

# 1. Configuración de rutas y PYTHONPATH multiplataforma
PROJECT_ROOT = Path(__file__).resolve().parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Definición de escenas oficiales del Grupo 3
SCENES = {
    1: {
        "title": "Escena 1: Construcción progresiva (n = 4)",
        "file": PROJECT_ROOT / "scenes" / "escena1_construccion.py",
        "class_name": "Escena1Construccion",
        "ticket": "EID-8",
    },
    2: {
        "title": "Escena 2: Refinamiento (n = 4 → 8 → 16 → 32)",
        "file": PROJECT_ROOT / "scenes" / "escena2_refinamiento.py",
        "class_name": "Escena2Refinamiento",
        "ticket": "EID-9",
    },
    3: {
        "title": "Escena 3: Del límite a la integral definida",
        "file": PROJECT_ROOT / "scenes" / "escena3_integral.py",
        "class_name": "Escena3Integral",
        "ticket": "EID-10",
    },
}

_PYTHON_RESOLVED = None


def get_subprocess_env():
    """Genera variables de entorno asegurando que la raíz esté en PYTHONPATH."""
    env = os.environ.copy()
    current_pythonpath = env.get("PYTHONPATH", "")
    if current_pythonpath:
        env["PYTHONPATH"] = f"{PROJECT_ROOT}{os.pathsep}{current_pythonpath}"
    else:
        env["PYTHONPATH"] = str(PROJECT_ROOT)
    return env


def resolve_python():
    """
    Obtiene el intérprete de Python a utilizar.
    Usa sys.executable, y si no está en un venv pero existe .venv local,
    informa y prefiere el del venv.
    """
    global _PYTHON_RESOLVED
    if _PYTHON_RESOLVED is not None:
        return _PYTHON_RESOLVED

    # Si ya estamos en un venv activo, usar sys.executable
    if getattr(sys, "base_prefix", sys.prefix) != sys.prefix:
        _PYTHON_RESOLVED = sys.executable
        return _PYTHON_RESOLVED

    # Si se ejecutó con el python del sistema pero existe un .venv local
    venv_unix = PROJECT_ROOT / ".venv" / "bin" / "python"
    venv_win = PROJECT_ROOT / ".venv" / "Scripts" / "python.exe"

    if venv_unix.is_file():
        print(f"[INFO] Utilizando entorno virtual local detectado: {venv_unix}")
        _PYTHON_RESOLVED = str(venv_unix)
        return _PYTHON_RESOLVED
    if venv_win.is_file():
        print(f"[INFO] Utilizando entorno virtual local detectado: {venv_win}")
        _PYTHON_RESOLVED = str(venv_win)
        return _PYTHON_RESOLVED

    _PYTHON_RESOLVED = sys.executable
    return _PYTHON_RESOLVED


def render_scene(scene_num: int, high_quality: bool = False, preview: bool = True) -> int:
    """Renderiza una escena de Manim con los parámetros adecuados."""
    if scene_num not in SCENES:
        print(f"\n[ERROR] Escena {scene_num} no válida. Las opciones son 1, 2 o 3.")
        return 1

    scene_info = SCENES[scene_num]
    scene_file = scene_info["file"]
    scene_class = scene_info["class_name"]

    if not scene_file.is_file():
        print(f"\n[AVISO] El archivo {scene_file.relative_to(PROJECT_ROOT)} aún no existe.")
        print(f"       ({scene_info['title']} - Tarea {scene_info['ticket']} pendiente)")
        return 1

    # Construir flags de Manim
    flag_q = "qh" if high_quality else "ql"
    flag = f"-p{flag_q}" if preview else f"-{flag_q}"

    quality_desc = "Alta calidad 1080p" if high_quality else "Baja calidad 480p"
    preview_desc = "con vista previa" if preview else "sin vista previa"

    print("=" * 72)
    print(f" RENDERIZANDO: {scene_info['title']}")
    print(f" Clase: {scene_class} | Archivo: {scene_file.relative_to(PROJECT_ROOT)}")
    print(f" Modalidad: {quality_desc} ({preview_desc}) -> Flag: {flag}")
    print("=" * 72)

    python_bin = resolve_python()
    cmd = [python_bin, "-m", "manim", flag, str(scene_file), scene_class]

    result = subprocess.run(cmd, cwd=str(PROJECT_ROOT), env=get_subprocess_env())
    return result.returncode


def run_verify() -> int:
    """Ejecuta el script de auditoría matemática independiente verify.py."""
    verify_script = PROJECT_ROOT / "verify.py"
    if not verify_script.is_file():
        print("\n[ERROR] No se encontró verify.py en la raíz del proyecto.")
        return 1

    python_bin = resolve_python()
    print("=" * 72)
    print(" EJECUTANDO AUDITORÍA MATEMÁTICA: verify.py")
    print("=" * 72)
    result = subprocess.run([python_bin, str(verify_script)], cwd=str(PROJECT_ROOT), env=get_subprocess_env())
    return result.returncode


def run_tests() -> int:
    """Ejecuta la suite de pruebas unitarias con unittest."""
    python_bin = resolve_python()
    print("=" * 72)
    print(" EJECUTANDO PRUEBAS UNITARIAS: tests/")
    print("=" * 72)
    cmd = [python_bin, "-m", "unittest", "discover", "-s", "tests"]
    result = subprocess.run(cmd, cwd=str(PROJECT_ROOT), env=get_subprocess_env())
    return result.returncode


def interactive_menu():
    """Despliega un menú interactivo en consola si no se pasan argumentos."""
    while True:
        print("\n" + "=" * 72)
        print("     RUNNER DE RENDERIZADO Y AUDITORÍA - GRUPO 3 (MAT1188)")
        print("=" * 72)
        print("  [1] Escena 1: Construcción progresiva (n = 4) [EID-8]")
        print("  [2] Escena 2: Refinamiento de particiones (n = 4 → 8 → 16 → 32) [EID-9]")
        print("  [3] Escena 3: Del límite a la integral definida [EID-10]")
        print("  [4] Renderizar todas las escenas disponibles")
        print("  [5] Ejecutar verificación matemática (verify.py)")
        print("  [6] Ejecutar pruebas unitarias (tests/)")
        print("  [0] Salir")
        print("-" * 72)

        try:
            choice = input("Seleccione una opción [0-6]: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nOperación cancelada por el usuario.")
            return 0

        if choice == "0":
            print("Saliendo del runner.")
            return 0
        elif choice in ("1", "2", "3"):
            scene_num = int(choice)
            high, preview = prompt_quality()
            if high is None:
                continue
            render_scene(scene_num, high_quality=high, preview=preview)
        elif choice == "4":
            high, preview = prompt_quality()
            if high is None:
                continue
            for s_num in (1, 2, 3):
                if SCENES[s_num]["file"].is_file():
                    ret = render_scene(s_num, high_quality=high, preview=preview)
                    if ret != 0:
                        print(f"[AVISO] Falló el renderizado de la escena {s_num}.")
                else:
                    print(f"\n[OMITIDA] Escena {s_num}: {SCENES[s_num]['file'].name} no existe aún.")
        elif choice == "5":
            run_verify()
        elif choice == "6":
            run_tests()
        else:
            print("[OPCIÓN NO VÁLIDA] Ingrese un número entre 0 y 6.")


def prompt_quality():
    """Pregunta al usuario la calidad y vista previa deseada en el modo interactivo."""
    print("\nSeleccione calidad de renderizado:")
    print("  [1] 480p con vista previa (-pql) [Rápida / Recomendada]")
    print("  [2] 1080p con vista previa (-pqh) [Alta calidad final]")
    print("  [3] 480p sin abrir reproductor (-ql)")
    print("  [4] 1080p sin abrir reproductor (-qh)")

    try:
        q_choice = input("Opción [1-4] (por defecto 1): ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\n[AVISO] Selección cancelada por el usuario.")
        return None, None

    if q_choice == "2":
        return True, True
    elif q_choice == "3":
        return False, False
    elif q_choice == "4":
        return True, False
    return False, True


def print_help():
    """Muestra la ayuda de uso de render.py."""
    print("""
Uso de render.py:
  python render.py [escena] [opciones]
  python render.py <comando>

Comandos y escenas disponibles:
  1, 2, 3           Número de la escena a renderizar.
  all               Renderiza todas las escenas disponibles.
  verify            Ejecuta verify.py (auditoría matemática independiente).
  test              Ejecuta las pruebas unitarias en tests/.

Opciones:
  -H, --high        Renderiza en alta resolución 1080p (-pqh).
                    (También se acepta -h si se especifica número de escena, ej: 'render.py 1 -h').
  --no-preview, -np No abre automáticamente el reproductor de video (-ql / -qh).
  -h, --help        Muestra esta ayuda.

Ejemplos:
  python render.py 1              # Escena 1 en 480p con preview
  python render.py 2 -H           # Escena 2 en 1080p con preview
  python render.py 2 -h           # Escena 2 en 1080p con preview
  python render.py 2 --high -np   # Escena 2 en 1080p sin abrir ventana
  python render.py verify         # Verificación matemática
  python render.py test           # Pruebas unitarias
  python render.py -h             # Muestra esta ayuda
  python render.py                # Menú interactivo
""")


def parse_cli_args(args):
    """
    Parsea los argumentos CLI considerando compatibilidad con:
    -h para ayuda estándar cuando no hay escena especificada,
    o como alias de alta calidad cuando acompaña a una escena.
    """
    if not args:
        return interactive_menu()

    # Si el usuario ejecuta explícitamente ayuda
    if "--help" in args or "help" in args:
        print_help()
        return 0

    # Extraer banderas y objetivo
    high_quality = False
    preview = True
    target = None
    has_h_flag = False

    for arg in args:
        if arg in ("-H", "--high"):
            high_quality = True
        elif arg == "-h":
            has_h_flag = True
        elif arg in ("-np", "--no-preview"):
            preview = False
        elif target is None:
            target = arg
        else:
            print(f"[ERROR] Argumento desconocido o duplicado: '{arg}'")
            print_help()
            return 1

    # Si se pasó -h sin ningún objetivo (ej: python render.py -h), mostrar ayuda
    if has_h_flag:
        if target is None:
            print_help()
            return 0
        else:
            high_quality = True

    if target is None:
        return interactive_menu()

    target_lower = target.lower()

    if target_lower == "verify":
        return run_verify()
    elif target_lower == "test":
        return run_tests()
    elif target_lower == "all":
        ret = 0
        for s_num in (1, 2, 3):
            if SCENES[s_num]["file"].is_file():
                r = render_scene(s_num, high_quality=high_quality, preview=preview)
                if r != 0:
                    ret = r
            else:
                print(f"\n[OMITIDA] Escena {s_num}: {SCENES[s_num]['file'].name} no existe aún.")
        return ret
    elif target in ("1", "2", "3"):
        return render_scene(int(target), high_quality=high_quality, preview=preview)
    else:
        print(f"[ERROR] Objetivo no reconocido: '{target}'")
        print_help()
        return 1


if __name__ == "__main__":
    sys.exit(parse_cli_args(sys.argv[1:]))
