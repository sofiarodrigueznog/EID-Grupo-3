#Segunda escena de la suma de Riemann, mostrando el refinamiento de la aproximación paso a paso, para n = 4, 8, 16 y 32.

from manim import *
from decimal import Decimal, ROUND_HALF_UP
from scenes.config import (
    f, a, b, n_values, sample_type, delta_x, sample_x,     #Importa la función y valores definidos en config.py
)


class Escena2Refinamiento(Scene):
    def construct(self):
        # 1. Parámetros matemáticos
        if list(n_values) != [4, 8, 16, 32]:
            raise ValueError("EID-9 requiere n = 4, 8, 16 y 32")
        if sample_type != "center":
            raise ValueError("EID-9 utiliza puntos medios")

        def calcular_suma(n):
            ancho = delta_x(n)
            return sum(
                f(sample_x(i, n)) * ancho
                for i in range(n)
            )

        def formatear_suma(valor):
            """Redondeo decimal para coincidir con docs/ejemplo.md."""
            return str(
                Decimal(str(valor)).quantize(
                    Decimal("0.000001"), rounding=ROUND_HALF_UP
                )
            )

        # 2. Título y subtítulo
        titulo = Text(
            "Refinamiento de las sumas de Riemann",
            font_size=34,
        ).to_edge(UP, buff=0.25)

        subtitulo = MathTex(
            r"f(x)=x^2+1,\quad [0,2]",
            font_size=29,
        ).next_to(titulo, DOWN, buff=0.17)

        self.play(Write(titulo), run_time=1.3)
        self.play(Write(subtitulo), run_time=1)

        # 3. Ejes y curva
        axes = Axes(
            x_range=[a, b + 0.5, 0.5],
            y_range=[0, 6, 1],
            x_length=6.3,
            y_length=4.7,
            tips=False,
        )
        axes.move_to(LEFT * 2.8 + DOWN * 0.65)

        curva = axes.plot(f, x_range=[a, b], color=YELLOW)
        curva.set_z_index(3)

        etiquetas_x = VGroup()
        for x in [a, a + 0.5, a + 1, a + 1.5, b]:
            etiquetas_x.add(
                MathTex(f"{x:g}", font_size=23).next_to(
                    axes.c2p(x, 0), DOWN, buff=0.18
                )
            )

        etiquetas_y = VGroup()
        for y in range(1, 6):
            etiquetas_y.add(
                MathTex(str(y), font_size=22).next_to(
                    axes.c2p(a, y), LEFT, buff=0.18
                )
            )

        self.play(
            Create(axes),
            FadeIn(etiquetas_x),
            FadeIn(etiquetas_y),
            run_time=1.5,
        )
        self.play(Create(curva), run_time=1.5)

        # 4. Objetos auxiliares para cada refinamiento
        def crear_rectangulos(n):
            rectangulos = axes.get_riemann_rectangles(
                curva,
                x_range=[a, b],
                dx=delta_x(n),
                input_sample_type=sample_type,
                color=BLUE_D,
                stroke_color=BLUE_B,
                stroke_width=1.2,
                fill_opacity=0.55,
                width_scale_factor=1.0,
            )
            rectangulos.set_z_index(1)
            if len(rectangulos) != n:
                raise ValueError("Cantidad incorrecta de rectángulos")
            return rectangulos

        def crear_segmento_dx(n):
            segmento = Line(
                axes.c2p(a, 0),
                axes.c2p(a + delta_x(n), 0),
                color=TEAL,
                stroke_width=8,
            )
            segmento.set_z_index(4)
            return segmento

        # 5. Panel derecho: encabezado, indicadores y tabla
        PANEL_X = 3.7

        encabezado = Text(
            "Aproximación actual", font_size=28
        ).move_to((PANEL_X, 2.14, 0))

        def crear_indicadores(n):
            datos = VGroup(
                MathTex(fr"n={n}", font_size=33),
                MathTex(fr"\Delta x={delta_x(n):g}", font_size=31),
                MathTex(
                    fr"S_{{{n}}}={formatear_suma(calcular_suma(n))}",
                    font_size=31,
                    color=YELLOW,
                ),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.20)
            datos.move_to((PANEL_X, 1.10, 0))
            return datos

        criterio = Text(
            "Criterio: puntos medios",
            font_size=23,
            color=TEAL_A,
        ).move_to((PANEL_X, 0.09, 0))

        self.play(
            FadeIn(encabezado),
            FadeIn(criterio),
            run_time=1,
        )

        # 6. Tabla
        tabla_titulo = Text(
            "Comparación numérica", font_size=25
        ).move_to((PANEL_X, -0.40, 0))

        columnas_x = (1.8, 3.5, 5.2)
        encabezados = VGroup(
            MathTex("n", font_size=25).move_to((columnas_x[0], -0.83, 0)),
            MathTex(r"\Delta x", font_size=25).move_to((columnas_x[1], -0.83, 0)),
            MathTex("S_n", font_size=25).move_to((columnas_x[2], -0.83, 0)),
        )

        def crear_fila(n, indice):
            y = -1.19 - indice * 0.36
            return VGroup(
                MathTex(str(n), font_size=24).move_to((columnas_x[0], y, 0)),
                MathTex(f"{delta_x(n):g}", font_size=24).move_to(
                    (columnas_x[1], y, 0)
                ),
                MathTex(
                    formatear_suma(calcular_suma(n)),
                    font_size=24,
                    color=YELLOW,
                ).move_to((columnas_x[2], y, 0)),
            )

        filas = [crear_fila(n, i) for i, n in enumerate(n_values)]

        self.play(
            FadeIn(tabla_titulo),
            FadeIn(encabezados),
            run_time=1,
        )

        # 7. Primera aproximación n=4
        n_inicial = n_values[0]
        rectangulos_actuales = crear_rectangulos(n_inicial)
        segmento_actual = crear_segmento_dx(n_inicial)
        indicadores_actuales = crear_indicadores(n_inicial)

        self.play(
            FadeIn(rectangulos_actuales),
            Create(segmento_actual),
            FadeIn(indicadores_actuales),
            run_time=1.8,
        )
        self.play(FadeIn(filas[0]), run_time=0.7)
        self.wait(2)

        # 8. Refinamiento: 4 -> 8 -> 16 -> 32
        for indice, n in enumerate(n_values[1:], start=1):
            nuevos_rectangulos = crear_rectangulos(n)
            nuevo_segmento = crear_segmento_dx(n)
            nuevos_indicadores = crear_indicadores(n)

            # Evita deformaciones de las expresiones matemáticas.
            self.play(FadeOut(indicadores_actuales), run_time=0.25)

            self.play(
                ReplacementTransform(rectangulos_actuales, nuevos_rectangulos),
                Transform(segmento_actual, nuevo_segmento),
                run_time=2.5,
            )

            self.play(FadeIn(nuevos_indicadores), run_time=0.4)
            self.play(FadeIn(filas[indice]), run_time=0.8)
            self.wait(2)

            rectangulos_actuales = nuevos_rectangulos
            indicadores_actuales = nuevos_indicadores

        # 9. Referencia exacta
        valor_exacto = MathTex(
            r"\int_0^2 (x^2+1)\,dx=\frac{14}{3}\approx4.666667",
            font_size=25,
            color=GREEN_C,
        )
        valor_exacto.move_to((PANEL_X, 0, 0))
        valor_exacto.to_edge(DOWN, buff=0.20)

        etiqueta_valor_exacto = Text(
            "Valor exacto de la integral",
            font_size=22,
            color=GREEN_C,
        ).next_to(valor_exacto, UP, buff=0.18)
        etiqueta_valor_exacto.set_x(PANEL_X)

        # Comprobaciones de encuadre y separación vertical.
        margen_inferior = -config.frame_height / 2 + 0.15
        if valor_exacto.get_bottom()[1] < margen_inferior:
            raise ValueError("La integral quedó fuera del encuadre inferior")

        # Orden de arriba a abajo: fila n=32 -> etiqueta -> integral.
        separacion = (
            filas[-1].get_bottom()[1]
            - etiqueta_valor_exacto.get_top()[1]
        )
        if separacion < 0.12:
            raise ValueError(
                "La tabla y el valor exacto están demasiado próximos: "
                f"espacio={separacion:.3f} unidades"
            )

        self.play(
            FadeIn(etiqueta_valor_exacto),
            Write(valor_exacto),
            run_time=1.5,
        )
        self.wait(4)
