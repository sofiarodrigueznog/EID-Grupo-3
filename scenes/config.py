"""
EID-7: Parámetros matemáticos centralizados.

Tema: Aproximación y refinamiento de sumas
de Riemann mediante puntos medios.

Fuente de los parámetros:
docs/ejemplo.md

Todas las escenas deben utilizar esta
configuración para mantener coherencia.
"""

# 1. Función a integrar

def f(x: float) -> float:
    """f(x) = x² + 1."""
    return x**2 + 1



# 2. Intervalo de integración

a = 0.0
b = 2.0



# 3. Valores de n para la tabla

n_values = [4, 8, 16, 32]




# 4. Criterio de muestreo de los rectángulos

# Manim utiliza "center" para puntos medios.
sample_type = "center"




# 5. Valor exacto de la integral

integral_exacta = 14 / 3



# 6. Ancho de los rectángulos (Δx)

def delta_x(n: int) -> float:
    """Calcula Δx = (b-a)/n."""

    if n <= 0:
        raise ValueError("n debe ser positivo")

    if b <= a:
        raise ValueError("El intervalo debe cumplir a < b")

    return (b - a) / n



# 7. Punto muestra

def sample_x(i: int, n: int) -> float:
    """
    Calcula el punto muestra del rectángulo i.

    Se utilizan índices desde 0 hasta n-1.
    """

    if n <= 0 or not 0 <= i < n:
        raise ValueError("Índice o número de rectángulos inválido")

    offsets = {
        "left": 0.0,
        "center": 0.5,
        "right": 1.0,
    }

    if sample_type not in offsets:
        raise ValueError("Criterio de muestreo inválido")

    return a + (i + offsets[sample_type]) * delta_x(n)



# 8. Suma de Riemann numérica centralizada

def riemann_sum(n: int) -> float:
    """
    Calcula la suma de Riemann numérica para n subintervalos
    utilizando la función f y el criterio de muestreo configurado.
    """
    dx = delta_x(n)
    return sum(f(sample_x(i, n)) * dx for i in range(n))



# 9. Deducción analítica cerrada (Paulo)

def suma_analitica(n: int) -> float:
    """
    Fórmula analítica cerrada de Paulo: S_n = 14/3 - 2/(3n²).
    Permite contrastar numéricamente la suma sin aproximación discreta.
    """
    if n <= 0:
        raise ValueError("n debe ser positivo")
    return (14 / 3) - 2 / (3 * (n**2))


def error_analitico(n: int) -> float:
    """
    Término de error analítico: |14/3 - S_n| = 2/(3n²).
    Demuestra la convergencia monótona hacia cero a medida que n -> ∞.
    """
    if n <= 0:
        raise ValueError("n debe ser positivo")
    return 2 / (3 * (n**2))
