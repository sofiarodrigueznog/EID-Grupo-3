#!/usr/bin/env python3
r"""
verify.py - Script de verificación matemática y auditoría independiente (EID-4)
Grupo 3 - Cálculo Intermedio MAT1188 (2026)

Función analizada: f(x) = x^2 + 1 en el intervalo [0, 2] con puntos medios.
Integral exacta: \int_0^2 (x^2 + 1) dx = 14/3.
Fórmula analítica cerrada de Paulo: S_n = 14/3 - 2 / (3 * n^2).

Uso como CLI:
    python3 verify.py

Uso como módulo importable (para auditoría en EID-11 y configuración en Manim):
    from verify import obtener_datos_tabla, VALOR_EXACTO, f, suma_riemann_discreta
"""

from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction
import sys

# Constantes del problema oficial
A = Fraction(0, 1)
B = Fraction(2, 1)
N_VALORES = [4, 8, 16, 32]
VALOR_EXACTO = Fraction(14, 3)

# Datos documentados en docs/ejemplo.md (EID-3) para validación cruzada
TABLA_DOCS = {
    4: {
        "delta": Fraction(1, 2),
        "sn_frac": Fraction(37, 8),
        "sn_dec": "4.625000",
        "err_frac": Fraction(1, 24),
        "err_dec": "0.041667",
    },
    8: {
        "delta": Fraction(1, 4),
        "sn_frac": Fraction(149, 32),
        "sn_dec": "4.656250",
        "err_frac": Fraction(1, 96),
        "err_dec": "0.010417",
    },
    16: {
        "delta": Fraction(1, 8),
        "sn_frac": Fraction(597, 128),
        "sn_dec": "4.664063",
        "err_frac": Fraction(1, 384),
        "err_dec": "0.002604",
    },
    32: {
        "delta": Fraction(1, 16),
        "sn_frac": Fraction(2389, 512),
        "sn_dec": "4.666016",
        "err_frac": Fraction(1, 1536),
        "err_dec": "0.000651",
    },
}


def f(x: Fraction) -> Fraction:
    """Evalúa f(x) = x^2 + 1 en aritmética racional exacta."""
    return x * x + 1


def a_decimal_str(frac: Fraction, precision: int = 6) -> str:
    """
    Convierte una fracción a string decimal con redondeo aritmético convencional (ROUND_HALF_UP).
    Garantiza consistencia con la notación matemática estándar usada en el apunte y docs/ejemplo.md.
    """
    d = Decimal(frac.numerator) / Decimal(frac.denominator)
    formato = Decimal("10") ** -precision
    return str(d.quantize(formato, rounding=ROUND_HALF_UP))


def suma_riemann_discreta(n: int) -> Fraction:
    """Calcula término a término la suma de Riemann usando puntos medios en [0, 2]."""
    if n <= 0:
        raise ValueError("n debe ser un entero positivo.")
    delta_x = (B - A) / n
    suma = Fraction(0, 1)
    for i in range(1, n + 1):
        x_mid = A + Fraction(2 * i - 1, 2) * delta_x
        suma += f(x_mid) * delta_x
    return suma


def formula_paulo(n: int) -> Fraction:
    """Evalúa la fórmula cerrada deducida por Paulo: S_n = 14/3 - 2 / (3 * n^2)."""
    if n <= 0:
        raise ValueError("n debe ser un entero positivo.")
    return VALOR_EXACTO - Fraction(2, 3 * n * n)


def error_teorico(n: int) -> Fraction:
    """Calcula el error absoluto teórico |14/3 - S_n| = 2 / (3 * n^2)."""
    if n <= 0:
        raise ValueError("n debe ser un entero positivo.")
    return Fraction(2, 3 * n * n)


def obtener_datos_tabla() -> dict:
    """
    Retorna un diccionario con los resultados calculados para cada n.
    Estructurado para su consumo directo en pruebas de Manim (EID-11) y Ficha PDF (EID-21).
    """
    datos = {}
    for n in N_VALORES:
        delta = (B - A) / n
        sn = suma_riemann_discreta(n)
        err = VALOR_EXACTO - sn
        datos[n] = {
            "n": n,
            "delta_frac": delta,
            "delta_dec": float(delta),
            "sn_frac": sn,
            "sn_dec": float(sn),
            "sn_dec_str": a_decimal_str(sn, 6),
            "err_frac": err,
            "err_dec": float(err),
            "err_dec_str": a_decimal_str(err, 6),
        }
    return datos


def ejecutar_auditoria() -> bool:
    """
    Ejecuta la validación cruzada y emite el reporte en consola con la tabla en Markdown.
    Retorna True si todas las aserciones pasan, False si ocurre algún error.
    """
    print("=" * 72)
    print(" AUDITORÍA MATEMÁTICA INDEPENDIENTE - GRUPO 3 (MAT1188)")
    print(" Tarea EID-4: Verificación de Sumas de Riemann (f(x) = x^2 + 1, [0, 2])")
    print("=" * 72)
    print()

    datos = obtener_datos_tabla()
    todos_ok = True

    print("1. Comprobación cruzada término a término vs. fórmula analítica y docs/ejemplo.md:")
    for n in N_VALORES:
        d = datos[n]
        s_disc = d["sn_frac"]
        s_anal = formula_paulo(n)
        esperado = TABLA_DOCS[n]

        # Validación 1: Suma discreta == Fórmula analítica
        if s_disc != s_anal:
            print(f"  [ERROR] n={n}: Suma discreta ({s_disc}) != Fórmula de Paulo ({s_anal})")
            todos_ok = False
            continue

        # Validación 2: Coincidencia con docs/ejemplo.md (fracción)
        if s_disc != esperado["sn_frac"]:
            print(f"  [ERROR] n={n}: Calculado ({s_disc}) != Documentado ({esperado['sn_frac']})")
            todos_ok = False
            continue

        # Validación 3: Error teórico exacto
        err_calculado = VALOR_EXACTO - s_disc
        if err_calculado != esperado["err_frac"]:
            print(f"  [ERROR] n={n}: Error calculado ({err_calculado}) != Documentado ({esperado['err_frac']})")
            todos_ok = False
            continue

        # Validación 4: Comparación decimal a 6 decimales
        sn_dec_str = d["sn_dec_str"]
        err_dec_str = d["err_dec_str"]
        if sn_dec_str != esperado["sn_dec"] or err_dec_str != esperado["err_dec"]:
            print(f"  [ERROR] n={n}: Discrepancia decimal ({sn_dec_str} vs {esperado['sn_dec']})")
            todos_ok = False
            continue

        print(f"  [OK] n={n:2d}: S_{n:<2d} = {str(s_disc):<10} ({sn_dec_str}) | Error = {str(err_calculado):<8} ({err_dec_str})")

    print()
    print("2. Tabla consolidada (formato Markdown para guion, PR y Ficha PDF):")
    print()
    print("| $n$ | $\\Delta x$ | $S_n$ exacta | $S_n$ decimal | Error exacto | Error decimal |")
    print("| :---: | :---: | :---: | :---: | :---: | :---: |")
    for n in N_VALORES:
        d = datos[n]
        print(f"| {n} | {d['delta_frac']} | {d['sn_frac']} | {d['sn_dec_str']} | {d['err_frac']} | {d['err_dec_str']} |")

    print()
    print("3. Comportamiento asintótico (n -> infinito):")
    limite = VALOR_EXACTO
    print(f"  * Integral definida exacta: 14/3 ≈ {a_decimal_str(limite, 6)}")
    print(f"  * Límite analítico: lim_{{n->inf}} (14/3 - 2/(3n^2)) = 14/3")
    print(f"  * Monotonía del error: {datos[4]['err_frac']} > {datos[8]['err_frac']} > {datos[16]['err_frac']} > {datos[32]['err_frac']} (Convergencia monótona)")
    print()

    if todos_ok:
        print("[RESULTADO] AUDITORÍA EXITOSA: Todos los valores coinciden al 100% con docs/ejemplo.md.")
    else:
        print("[RESULTADO] AUDITORÍA FALLIDA: Se detectaron discrepancias matemáticas.")

    return todos_ok


if __name__ == "__main__":
    exito = ejecutar_auditoria()
    sys.exit(0 if exito else 1)
