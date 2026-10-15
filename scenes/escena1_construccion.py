#Primera escena de la suma de Riemann, mostrando la construcción paso a paso, para n = 4.
#

from manim import *

from scenes.config import (
    f, a, b, n_values, sample_type, delta_x, sample_x       #Importa la función y valores definidos en config.py
)


class Escena1Construccion(Scene):

    def construct(self):

        # 1. Parámetros iniciales de config.py

        n = n_values[0]
        dx = delta_x(n)

        if n != 4 or sample_type != "center":
            raise ValueError(
                "EID-8 requiere n=4 y puntos medios"
            )

        puntos_medios = [
            sample_x(i, n) for i in range(n)
        ]

        alturas = [
            f(x) for x in puntos_medios
        ]

        areas = [
            altura * dx for altura in alturas
        ]

        suma = sum(areas)


        # 2. Título y subtítulo

        titulo = Text(
            "Construcción de la suma de Riemann",
            font_size=34
        ).to_edge(UP, buff=0.25)

        subtitulo = MathTex(
            fr"f(x)=x^2+1,\quad {a:g}\leq x\leq {b:g}",
            font_size=30
        ).next_to(
            titulo, DOWN, buff=0.2
        )

        self.play(Write(titulo))
        self.play(Write(subtitulo))
        self.wait(0.7)


        # 3. Ejes y curva de la función

        axes = Axes(
            x_range=[a, b + 0.5, 0.5],
            y_range=[0, 6, 1],
            x_length=6,
            y_length=4.3,
            tips=False,
        )

        axes.move_to(
            LEFT * 2.3 + DOWN * 0.45
        )

        curva = axes.plot(
            f,
            x_range=[a, b],
            color=YELLOW
        )

        curva.set_z_index(3)

        etiquetas_y = VGroup()

        for y in range(1, 6):

            etiqueta_y = MathTex(
                str(y),
                font_size=21
            ).next_to(
                axes.c2p(a, y),
                LEFT,
                buff=0.18
            )

            etiquetas_y.add(etiqueta_y)

        self.play(
            Create(axes),
            FadeIn(etiquetas_y),
            run_time=1.5
        )

        self.play(
            Create(curva),
            run_time=2
        )

        self.wait(0.7)



        # 4. Marcas y etiquetas del eje X

        marcas = VGroup()
        etiquetas_x = VGroup()

        for i in range(n + 1):

            x = a + i * dx

            marca = Line(
                axes.c2p(x, 0.12),
                axes.c2p(x, -0.12),
                color=WHITE,
                stroke_width=2
            )

            etiqueta = MathTex(
                f"{x:g}",
                font_size=22
            ).next_to(
                axes.c2p(x, 0),
                DOWN,
                buff=0.18
            )

            marcas.add(marca)
            etiquetas_x.add(etiqueta)

        self.play(
            Create(marcas),
            FadeIn(etiquetas_x),
            run_time=1.5
        )

        # Resaltar el ancho del
        # primer subintervalo.

        segmento_dx = Line(
            axes.c2p(a, 0),
            axes.c2p(a + dx, 0),
            color=TEAL,
            stroke_width=7
        )

        segmento_dx.set_z_index(5)

        self.play(Create(segmento_dx))
        self.wait(0.7)


        # 5. Informacion sobre n, Δx y criterio de muestreo
        informacion = VGroup(

            MathTex(
                f"n={n}",
                font_size=31
            ),

            MathTex(
                fr"\Delta x=\frac{{{b-a:g}}}"
                fr"{{{n}}}={dx:g}",
                font_size=28
            ),

            Text(
                "Criterio: puntos medios",
                font_size=27,
                color=TEAL_A
            ),

            MathTex(
                r"A_i=f(x_i^*)\Delta x",
                font_size=28
            )

        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.16
        )


        # 6. Rectángulos de Riemann

        rectangulos = axes.get_riemann_rectangles(
            curva,
            x_range=[a, b],
            dx=dx,
            input_sample_type=sample_type,
            color=BLUE_D,
            stroke_color=BLUE_B,
            stroke_width=1.5,
            fill_opacity=0.55,
            width_scale_factor=1.0
        )

        rectangulos.set_z_index(1)

        if len(rectangulos) != n:
            raise ValueError(
                "La cantidad de rectángulos "
                "no coincide con n"
            )


        # 7. Etiquetas de los puntos muestra y áreas de los rectángulos

        etiquetas_areas = VGroup()

        for i in range(n):

            etiqueta_punto = MathTex(
                fr"x_{{{i+1}}}^*={puntos_medios[i]:.2f}",
                font_size=28
            )

            etiqueta_area = MathTex(
                fr"A_{{{i+1}}}={areas[i]:.5f}",
                font_size=28,
                color=BLUE_B
            )

            fila = VGroup(
                etiqueta_punto,
                etiqueta_area
            ).arrange(
                RIGHT,
                buff=0.28
            )

            etiquetas_areas.add(fila)

        etiquetas_areas.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.18
        )


        # 8. Resultado de la suma de Riemann

        resultado = MathTex(
            fr"S_{{{n}}}={suma:.3f}",
            font_size=40,
            color=YELLOW
        )


        # 9. Panel de información, etiquetas y resultado

        panel = VGroup(
            informacion,
            etiquetas_areas,
            resultado
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.26
        )

        # Limitar tamaño para mantener
        # todo dentro del encuadre.

        if panel.width > 5.2:
            panel.scale_to_fit_width(5.2)

        if panel.height > 5.35:
            panel.scale_to_fit_height(5.35)

        # Ubicar a la derecha de la gráfica,
        # dejando espacio bajo el subtítulo.

        panel.to_edge(
            RIGHT,
            buff=0.48
        )

        panel.to_edge(
            UP,
            buff=1.72
        )

        # Mostrar información inicial.
        self.play(
            FadeIn(informacion),
            run_time=1.5
        )

        self.wait(1)

        # 10. Construcción paso a paso de los rectángulos

        for i in range(n):

            x_i = puntos_medios[i]
            altura = alturas[i]

            # Línea vertical desde el eje X
            # hasta el punto de la curva.

            linea = DashedLine(
                axes.c2p(x_i, 0),
                axes.c2p(x_i, altura),
                color=GREEN_C,
                stroke_width=2
            )

            linea.set_z_index(2)

            # Punto medio sobre el eje X.
            # Ayuda a identificar dónde se
            # evalúa la función.

            punto_base = Dot(
                axes.c2p(x_i, 0),
                color=TEAL_A,
                radius=0.045
            )

            punto_base.set_z_index(6)

            # Punto muestra sobre la curva.

            punto = Dot(
                axes.c2p(x_i, altura),
                color=ORANGE,
                radius=0.055
            )

            punto.set_z_index(4)

            # Primero se muestra el punto
            # medio y su altura.

            self.play(
                FadeIn(punto_base),
                Create(linea),
                FadeIn(punto),
                run_time=0.7
            )

            # Después aparece el rectángulo
            # con su correspondiente área.

            self.play(
                FadeIn(rectangulos[i]),
                Write(etiquetas_areas[i]),
                run_time=1.1
            )

            self.wait(0.65)


        # 11. Muestra de la suma de Riemann final

        self.play(
            Write(resultado),
            run_time=1.2
        )

        # Mantener el resultado visible
        # durante cuatro segundos.

        self.wait(4)
