"""
scenes/escena3_integral.py - Escena 3: Del límite a la integral definida.
Grupo 3 - MAT1188 Cálculo Intermedio (EID)

Eje 3: Aproximación y refinamiento.
Tema: De pocos rectángulos a una mejor aproximación.

Esta escena concluye la explicación matemática conectando la aproximación
fina de rectángulos (n = 32) con la integral definida exacta a través del
paso al límite, demostrando la anulación analítica del término de error
y respondiendo explícitamente a la Pregunta Central del equipo.
"""

from manim import *
from scenes.config import (
    f,
    a,
    b,
    n_values,
    sample_type,
    delta_x,
)


class Escena3Integral(Scene):
    """
    Escena 3: Transición del límite discreto a la integral continua
    y respuesta a la pregunta central del Grupo 3.
    """

    def construct(self):
        # 0. Verificación de coherencia con scenes/config.py
        if sample_type != "center":
            raise ValueError("EID-10 requiere criterio de puntos medios")
        if n_values[-1] != 32:
            raise ValueError("EID-10 requiere n=32 como última partición de config.py")

        PANEL_X = 3.45

        # =====================================================================
        # 1. PARTE 1: TÍTULO Y SUBTÍTULO
        # =====================================================================
        titulo = Text(
            "Del límite a la integral definida",
            font_size=34,
        ).to_edge(UP, buff=0.25)

        subtitulo = MathTex(
            fr"f(x)=x^2+1,\quad [{a:g},{b:g}]",
            font_size=28,
        ).next_to(titulo, DOWN, buff=0.15)

        self.play(Write(titulo), run_time=1.2)
        self.play(Write(subtitulo), run_time=0.8)
        self.wait(0.5)

        # =====================================================================
        # 2. PARTE 2: DE LO DISCRETO A LO CONTINUO (GRÁFICA Y TRANSFORMACIÓN)
        # =====================================================================
        axes = Axes(
            x_range=[a, b + 0.5, 0.5],
            y_range=[0, 6, 1],
            x_length=5.8,
            y_length=4.3,
            tips=False,
        )
        # Posición optimizada para dar margen superior e inferior holgados
        axes.move_to(LEFT * 3.35 + DOWN * 0.45)

        curva = axes.plot(f, x_range=[a, b], color=YELLOW)
        curva.set_z_index(5)

        etiquetas_x = VGroup()
        for x in [a, a + 0.5, a + 1.0, a + 1.5, b]:
            etiquetas_x.add(
                MathTex(f"{x:g}", font_size=21).next_to(
                    axes.c2p(x, 0), DOWN, buff=0.15
                )
            )

        etiquetas_y = VGroup()
        for y in range(1, 6):
            etiquetas_y.add(
                MathTex(str(y), font_size=20).next_to(
                    axes.c2p(a, y), LEFT, buff=0.15
                )
            )

        self.play(
            Create(axes),
            FadeIn(etiquetas_x),
            FadeIn(etiquetas_y),
            run_time=1.2,
        )
        self.play(Create(curva), run_time=1.0)

        # Rectángulos de la partición más fina de la Escena 2 (n = 32 desde config.py)
        n_inicial = n_values[-1]
        rectangulos_n32 = axes.get_riemann_rectangles(
            curva,
            x_range=[a, b],
            dx=delta_x(n_inicial),
            input_sample_type=sample_type,
            color=BLUE_C,
            stroke_color=BLUE_A,
            stroke_width=0.8,
            fill_opacity=0.60,
            width_scale_factor=1.0,
        )
        rectangulos_n32.set_z_index(2)

        # S_32 en amarillo para mantener consistencia cromática con Escenas 1 y 2
        etiqueta_n32 = MathTex(
            r"S_{32} = 4.666016 \quad (n=32)",
            font_size=21,
            color=YELLOW,
        ).next_to(etiquetas_x, DOWN, buff=0.20)

        self.play(
            FadeIn(rectangulos_n32),
            FadeIn(etiqueta_n32),
            run_time=1.2,
        )
        self.wait(1.0)

        # Transformación suave hacia el área continua exacta bajo la curva
        area_exacta = axes.get_area(
            curva,
            x_range=[a, b],
            color=BLUE_D,
            opacity=0.65,
        )
        area_exacta.set_z_index(2)

        etiqueta_area = MathTex(
            r"A = \int_0^2 (x^2+1)\,dx = \frac{14}{3} \approx 4.666667",
            font_size=20,
            color=GREEN_C,
        ).next_to(etiquetas_x, DOWN, buff=0.20)

        self.play(
            ReplacementTransform(rectangulos_n32, area_exacta),
            ReplacementTransform(etiqueta_n32, etiqueta_area),
            run_time=2.2,
        )
        self.wait(0.8)

        # =====================================================================
        # 3. PARTE 3: EL OPERADOR LÍMITE (TRANSICIÓN DE SÍMBOLOS)
        # =====================================================================
        encabezado_bloque1 = Text(
            "1. Transición al límite continuo",
            font_size=21,
            color=BLUE_B,
            weight=BOLD,
        ).move_to((PANEL_X, 2.38, 0))

        formula_integral = MathTex(
            r"\lim_{n \to \infty} \sum_{i=1}^n f(x_i^*)\,\Delta x = \int_0^2 (x^2+1)\,dx = \frac{14}{3}",
            font_size=23,
        ).next_to(encabezado_bloque1, DOWN, buff=0.18)

        correspondencia = MathTex(
            r"\sum \longrightarrow \int,\quad f(x_i^*) \longrightarrow f(x),\quad \Delta x \longrightarrow dx",
            font_size=19,
            color=TEAL_C,
        ).next_to(formula_integral, DOWN, buff=0.15)

        self.play(
            FadeIn(encabezado_bloque1),
            Write(formula_integral),
            run_time=1.8,
        )
        self.play(FadeIn(correspondencia), run_time=1.2)

        # El ancho de los rectángulos tiende a cero cuando n crece
        delta_x_cero = MathTex(
            fr"\Delta x=\frac{{{b - a:g}}}{{n}}\longrightarrow 0"
            r"\quad \text{cuando } n \to \infty",
            font_size=22,
            color=TEAL_C,
        ).next_to(correspondencia, DOWN, buff=0.15)

        self.play(FadeIn(delta_x_cero), run_time=1.0)
        self.wait(1.0)

        # =====================================================================
        # 4. PARTE 4: EL ERROR SE ANULA ANALÍTICAMENTE
        # =====================================================================
        encabezado_bloque2 = Text(
            "2. El error analítico tiende a cero",
            font_size=21,
            color=BLUE_B,
            weight=BOLD,
        ).next_to(delta_x_cero, DOWN, buff=0.28)

        formula_sn = MathTex(
            r"S_n = \frac{14}{3} - \frac{2}{3n^2}",
            font_size=23,
        ).next_to(encabezado_bloque2, DOWN, buff=0.16)

        limite_sn = MathTex(
            r"\lim_{n \to \infty} \left(\frac{14}{3} - \frac{2}{3n^2}\right) = \frac{14}{3} - 0 = \frac{14}{3}",
            font_size=22,
        ).next_to(formula_sn, DOWN, buff=0.15)

        # Destacar que el término 2/(3n^2) tiende a 0
        destacado_error = MathTex(
            r"\text{Para } n \to \infty \implies \frac{2}{3n^2} \longrightarrow 0 \quad (\text{Error} \to 0)",
            font_size=19,
            color=YELLOW,
        ).next_to(limite_sn, DOWN, buff=0.15)

        self.play(
            FadeIn(encabezado_bloque2),
            Write(formula_sn),
            run_time=1.4,
        )
        self.play(Write(limite_sn), run_time=1.6)
        self.play(FadeIn(destacado_error), run_time=1.0)
        self.wait(1.2)

        # =====================================================================
        # 5. PARTE 5: RESPUESTA A LA PREGUNTA CENTRAL (CONCLUSIÓN FINAL)
        # =====================================================================
        # Agrupamos los bloques analíticos para transicionar a la conclusión
        bloques_analiticos = VGroup(
            encabezado_bloque1,
            formula_integral,
            correspondencia,
            delta_x_cero,
            encabezado_bloque2,
            formula_sn,
            limite_sn,
            destacado_error,
        )

        # Cuadro de conclusión final con respuesta explícita a la pregunta central
        rect_fondo = RoundedRectangle(
            corner_radius=0.18,
            width=6.6,
            height=4.6,
            color=GOLD_B,
            stroke_width=2.5,
            fill_color=BLACK,
            fill_opacity=0.90,
        ).move_to((PANEL_X, 0.10, 0))

        titulo_pregunta = Text(
            "Pregunta central del Grupo 3:",
            font_size=20,
            color=GOLD_B,
            weight=BOLD,
        )

        pregunta = Text(
            "«¿Por qué una suma de Riemann puede aproximar cada vez mejor\nuna región cuando aumentamos el número de rectángulos?»",
            font_size=16,
            color=GRAY_A,
            line_spacing=1.1,
        )

        divisor = Line(
            LEFT * 2.8,
            RIGHT * 2.8,
            color=GOLD_D,
            stroke_width=1.5,
        )

        titulo_respuesta = Text(
            "Respuesta y Conclusión:",
            font_size=20,
            color=YELLOW,
            weight=BOLD,
        )

        # Párrafos tipográficos con MathTex/Tex para fuentes matemáticas de LaTeX
        parrafo_respuesta_1 = Tex(
            r"Al aumentar $n$ y reducir $\Delta x$, los rectángulos se",
            font_size=20,
            color=WHITE,
        )
        parrafo_respuesta_2 = Tex(
            r"ajustan con precisión creciente a la curva $f(x)$.",
            font_size=20,
            color=WHITE,
        )
        parrafo_respuesta_3 = Tex(
            r"El término de error $\frac{2}{3n^2}$ tiende a cero,",
            font_size=20,
            color=WHITE,
        )
        parrafo_respuesta_4 = Tex(
            r"\textbf{haciendo que la suma de Riemann converja}",
            font_size=20,
            color=YELLOW,
        )
        parrafo_respuesta_5 = Tex(
            r"\textbf{exactamente a la integral definida.}",
            font_size=20,
            color=YELLOW,
        )

        contenido_caja = VGroup(
            titulo_pregunta,
            pregunta,
            divisor,
            titulo_respuesta,
            parrafo_respuesta_1,
            parrafo_respuesta_2,
            parrafo_respuesta_3,
            parrafo_respuesta_4,
            parrafo_respuesta_5,
        ).arrange(DOWN, buff=0.13)

        contenido_caja.move_to(rect_fondo.get_center())

        # Transición limpia hacia la respuesta a la pregunta central
        self.play(FadeOut(bloques_analiticos), run_time=0.8)
        self.play(
            FadeIn(rect_fondo),
            FadeIn(contenido_caja),
            run_time=2.0,
        )

        # Tiempo final para que la locución de voz concluya con claridad
        self.wait(4.5)
