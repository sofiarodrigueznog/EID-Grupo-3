# Ficha de Entrega – Evaluación Integrada de Desempeño (EID)

**Curso / Asignatura:** MAT1188 – Cálculo Intermedio (Ingeniería Civil Informática · 2.º Año · Semestre 2026-2)  
**Grupo:** Grupo 3 (`G03`)  
**Tema:** Eje 3 · Aproximación y refinamiento — *«De pocos rectángulos a una mejor aproximación»*  
**Integrantes:**  
- **Denys Sofía Rodríguez Noguera** (`@sofiarodrigueznog`) — *Líder / Revisión e integración del video*  
- **Paulo Villalobos Aravena** (`@notKechai`) — *Matemática y explicación teórica*  
- **Antonio Ignacio Lara Fuentealba** (`@alara2024uct`) — *Visualización y código Manim*  
- **Renato Misrrain Carrasco Oviedo** (`@RCarrascoO`) — *Apoyo matemático, visualización y auditoría*  

**Fecha de entrega:** 18 de octubre de 2026  

---

## 1. Identificación y Metadatos de Entrega (Criterio V8)

| Campo | Información Oficial |
| :--- | :--- |
| **Código y Asignatura** | MAT1188 – Cálculo Intermedio |
| **Número de Grupo** | Grupo 3 (`G03`) |
| **Integrantes del Equipo** | Denys Sofía Rodríguez Noguera, Paulo Villalobos Aravena, Antonio Ignacio Lara Fuentealba y Renato Misrrain Carrasco Oviedo |
| **Repositorio Público de GitHub** | [https://github.com/sofiarodrigueznog/EID-Grupo-3](https://github.com/sofiarodrigueznog/EID-Grupo-3) |
| **SHA del Commit Entregado** | Commit con la etiqueta [`v1.2-entrega`](https://github.com/sofiarodrigueznog/EID-Grupo-3/releases/tag/v1.2-entrega) (el SHA completo figura en la ficha PDF entregada en Blackboard) |
| **Nombre del Archivo de Video** | `MAT1188_EID_G03_2026.mp4` |
| **Duración Exacta del Video** | `5 minutos y 55 segundos` *(05:55 min · Rango exigido: 4:00 a 6:00 min, incluye presentación y créditos)* |
| **Nombre de la Ficha PDF** | `MAT1188_EID_G03_2026.pdf` |
| **Código de Ética** | Entregado en Blackboard (`MAT1188_ETICA_G03_2026.pdf`) el 06 de octubre de 2026 |

### Mapa de Documentos en el Repositorio (V8d, V8e)

Todos los respaldos del video y la defensa oral se encuentran organizados y accesibles en el repositorio:

| Documento / Recurso | Ruta en el Repositorio | Contenido y Propósito |
| :--- | :--- | :--- |
| **Guion y Notas Matemáticas** | [`docs/guion.md`](https://github.com/sofiarodrigueznog/EID-Grupo-3/blob/main/docs/guion.md) | Guion completo del video con marcas de tiempo, locutores y desarrollo hablado. |
| **Marco Teórico** | [`docs/teoria.md`](https://github.com/sofiarodrigueznog/EID-Grupo-3/blob/main/docs/teoria.md) | Conceptos de partición, puntos muestra, sumas de Riemann, refinamiento e integral. |
| **Ejemplo Desarrollado** | [`docs/ejemplo.md`](https://github.com/sofiarodrigueznog/EID-Grupo-3/blob/main/docs/ejemplo.md) | Cálculos detallados para $n=4, 8, 16, 32$, deducción de la fórmula y tabla de valores. |
| **Fuentes y Referencias** | [`docs/referencias.md`](https://github.com/sofiarodrigueznog/EID-Grupo-3/blob/main/docs/referencias.md) | Bibliografía completa con enlaces directos, páginas e ISBN consultados. |
| **Declaración de Uso de IA** | [`docs/declaracion_ia.md`](https://github.com/sofiarodrigueznog/EID-Grupo-3/blob/main/docs/declaracion_ia.md) | Uso transparente de IA por cada integrante y métodos de verificación humana aplicados. |
| **Parámetros Centralizados** | [`scenes/config.py`](https://github.com/sofiarodrigueznog/EID-Grupo-3/blob/main/scenes/config.py) | Parámetros matemáticos compartidos por todas las animaciones ($f$, $[a,b]$, $n$, puntos medios). |
| **Auditoría y Pruebas** | [`verify.py`](https://github.com/sofiarodrigueznog/EID-Grupo-3/blob/main/verify.py) / [`tests/test_config.py`](https://github.com/sofiarodrigueznog/EID-Grupo-3/blob/main/tests/test_config.py) | Verificación independiente en fracciones exactas y suite de 11 pruebas automáticas. |
| **Runner Multiplataforma** | [`render.py`](https://github.com/sofiarodrigueznog/EID-Grupo-3/blob/main/render.py) | Script de ejecución para renderizar escenas y correr pruebas en Linux, Windows y macOS. |

---

## 2. Nómina de Integrantes y Responsabilidades

| Integrante | Cuenta GitHub | Responsabilidad Principal | Aporte Efectivo al Proyecto |
| :--- | :--- | :--- | :--- |
| **Denys Sofía Rodríguez Noguera** *(Líder)* | [@sofiarodrigueznog](https://github.com/sofiarodrigueznog) | Revisión e integración del video | Coordinación general, estructura del repositorio, automatización CI, edición y montaje final del video MP4 (5:55 min), locución y entrega oficial. |
| **Paulo Villalobos Aravena** | [@notKechai](https://github.com/notKechai) | Matemática y explicación | Redacción de la teoría (`teoria.md`), desarrollo analítico del ejemplo con puntos medios (`ejemplo.md`), deducción de la fórmula cerrada $S_n$, guion y locución. |
| **Antonio Ignacio Lara Fuentealba** | [@alara2024uct](https://github.com/alara2024uct) | Visualización y código | Centralización de parámetros en `config.py`, suite de pruebas (`test_config.py`), programación de Escena 1 ($n=4$) y Escena 2 (refinamiento), y locución. |
| **Renato Misrrain Carrasco Oviedo** | [@RCarrascoO](https://github.com/RCarrascoO) | Apoyo matemática y visualización | Script de auditoría independiente (`verify.py`), runner multiplataforma (`render.py`), programación de Escena 3 (límite e integral), locución y ficha técnica. |

---

## 3. Tema Asignado y Pregunta Central

* **Eje temático:** Eje 3 · Aproximación y refinamiento.
* **Tema oficial:** *De pocos rectángulos a una mejor aproximación*.
* **Pregunta central:**
  > *«¿Por qué una suma de Riemann puede aproximar cada vez mejor una región cuando aumentamos el número de rectángulos?»*

---

## 4. Fundamentos Matemáticos y Desarrollo del Ejemplo (Criterios V1, V2, V3)

### A. Definición de Suma de Riemann y Significado de los Símbolos (V1a, V1b)
Para aproximar el área bajo una curva dividimos el intervalo $[a,b]$ en $n$ partes iguales. Cada parte tiene un ancho uniforme $\Delta x$ y sirve como base para construir un rectángulo. La **suma de Riemann** es simplemente la suma de las áreas de todos esos rectángulos:

$$S_n = \sum_{i=1}^{n} f(x_i^*)\,\Delta x$$

* **$[a,b] = [0,2]$:** Intervalo cerrado donde analizamos la función.
* **$n$:** Cantidad de partes (subintervalos) y número total de rectángulos que construimos.
* **$\Delta x = \frac{b-a}{n} = \frac{2}{n}$:** Ancho de la base de cada rectángulo. Al aumentar $n$, las bases se vuelven cada vez más delgadas.
* **$x_i^*$:** Punto muestra elegido dentro de cada subintervalo para medir la altura. En este proyecto elegimos el **punto medio** de cada tramo:
  $$x_i^* = a + \left(i - \frac{1}{2}\right)\Delta x$$
* **$f(x_i^*)$:** Altura del rectángulo $i$, calculada evaluando la función en su punto medio.
* **$A_i = f(x_i^*)\,\Delta x$:** Área individual del rectángulo $i$ (base por altura).
* **$\sum_{i=1}^n$:** Sumatoria que reúne las áreas de los $n$ rectángulos para obtener la aproximación total $S_n$.

### B. Condiciones Necesarias y Conceptos Clave (V1c, V1d)
1. **Continuidad:** La función $f(x) = x^2 + 1$ es continua en todo el intervalo $[0,2]$ (no tiene saltos ni divisiones por cero). Esta condición asegura que el proceso de aproximación funcione de manera estable y que las sumas de Riemann converjan a un único valor exacto cuando $n$ crece.
2. **Positividad (Área geométrica):** En general, una suma de Riemann calcula el *área neta con signo* (las partes bajo el eje $x$ restan). En nuestro ejemplo, como $f(x) \geq 1 > 0$ en todo $[0,2]$, la curva está siempre por encima del eje horizontal. Por lo tanto, los rectángulos tienen alturas positivas y la suma representa directamente el **área geométrica** de la región.
3. **Distinción entre aproximación, límite e integral:**
   * **Suma de Riemann ($S_n$):** Es un cálculo aproximado que suma un número finito de rectángulos (por ejemplo, con 4 o 32 rectángulos).
   * **Refinamiento y límite ($n \to \infty$):** Es la idea matemática de hacer las bases cada vez más finas ($\Delta x \to 0$) aumentando indefinidamente la cantidad de rectángulos.
   * **Integral definida ($\int_0^2 f(x)\,dx$):** Es el número exacto al que se acercan las aproximaciones cuando $n$ tiende a infinito:
     $$\int_0^2 (x^2+1)\,dx = \lim_{n\to\infty} \sum_{i=1}^{n} f(x_i^*)\,\Delta x = \frac{14}{3}$$

### C. Cálculos del Ejemplo y Deducción de la Fórmula (V2b–e)
El **valor analítico exacto** del área se obtiene mediante la regla de Barrow (evaluando la primitiva):
$$\int_0^2 (x^2 + 1)\,dx = \left[ \frac{x^3}{3} + x \right]_0^2 = \frac{2^3}{3} + 2 = \frac{8}{3} + 2 = \frac{14}{3} \approx 4.666667$$

* **Cálculo paso a paso con 4 rectángulos ($n=4$):**
  El ancho de cada rectángulo es $\Delta x = \frac{2-0}{4} = \frac{1}{2} = 0.5$.  
  Los puntos medios de los 4 tramos son: $x_1^* = 0.25$, $x_2^* = 0.75$, $x_3^* = 1.25$ y $x_4^* = 1.75$ (o en fracciones: $\frac{1}{4}, \frac{3}{4}, \frac{5}{4}, \frac{7}{4}$).  
  Evaluamos la altura de cada uno y sumamos sus áreas:
  $$S_4 = \frac{1}{2}\left[\left(\left(\frac{1}{4}\right)^2+1\right) + \left(\left(\frac{3}{4}\right)^2+1\right) + \left(\left(\frac{5}{4}\right)^2+1\right) + \left(\left(\frac{7}{4}\right)^2+1\right)\right] = \frac{37}{8} = 4.625$$

* **Cómo se obtiene la fórmula general para cualquier $n$:**  
  Con $\Delta x = \frac{2}{n}$ y puntos medios $x_i^* = \frac{2i-1}{n}$, la suma completa queda:
  $$S_n = \sum_{i=1}^{n} \left[\left(\frac{2i-1}{n}\right)^2 + 1\right]\frac{2}{n} = \frac{2}{n}\left[\frac{1}{n^2}\sum_{i=1}^{n}(4i^2 - 4i + 1) + n\right]$$
  Al sumar los cuadrados de los números impares se obtiene la identidad conocida $\sum_{i=1}^n (2i-1)^2 = \frac{n(4n^2-1)}{3}$. Reemplazando esa suma y simplificando el álgebra:
  $$S_n = \frac{2(4n^2-1)}{3n^2} + 2 = \frac{8n^2 - 2 + 6n^2}{3n^2} = \frac{14n^2 - 2}{3n^2} = \frac{14}{3} - \frac{2}{3n^2}$$
  Esta fórmula permite conocer el valor exacto de la suma de Riemann para cualquier $n$ sin tener que sumar rectángulo por rectángulo.

### D. Tabla de Resultados y Comportamiento del Error (V2d, V3a)

| Cantidad de rectángulos $n$ | Ancho de base $\Delta x$ | Suma de Riemann $S_n$ | Valor decimal | Error exacto $\left|\frac{14}{3} - S_n\right|$ | Error decimal |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **4** | $1/2 = 0.5000$ | $37/8$ | $4.625000$ | $1/24$ | $0.041667$ |
| **8** | $1/4 = 0.2500$ | $149/32$ | $4.656250$ | $1/96$ | $0.010417$ |
| **16** | $1/8 = 0.1250$ | $597/128$ | $4.664063$ | $1/384$ | $0.002604$ |
| **32** | $1/16 = 0.0625$ | $2389/512$ | $4.666016$ | $1/1536$ | $0.000651$ |
| **$n \to \infty$** | $\Delta x \to 0$ | **$\mathbf{14/3}$** | **$4.666667$** | **$0$** | **$0.000000$** |

* **Por qué las aproximaciones quedan por debajo de $\frac{14}{3}$:**  
  La curva de $f(x)=x^2+1$ se dobla hacia arriba en todo el intervalo (su segunda derivada es positiva, $f''(x)=2>0$). Cuando se usa el punto medio en una curva con esta forma, la parte del rectángulo que queda por fuera de la curva es un poco más pequeña que el espacio que le falta por cubrir. Por esa razón geométrica, la suma siempre subestima levemente el área real ($S_n < \frac{14}{3}$).
* **Rapidez de aproximación:**  
  En nuestra fórmula el error es exactamente $\frac{2}{3n^2}$. Esto significa que cada vez que duplicamos la cantidad de rectángulos ($4 \to 8 \to 16 \to 32$), el error se divide por cuatro ($\frac{1}{24} \to \frac{1}{96} \to \frac{1}{384} \to \frac{1}{1536}$), haciendo que la aproximación mejore con gran rapidez.

### E. Respuesta a la Pregunta Central (V3c, V3d, V3e)
> Una suma de Riemann aproxima cada vez mejor la región porque, al mantener fijo el intervalo $[0,2]$ y aumentar la cantidad de rectángulos, el ancho de cada base $\Delta x = \frac{2}{n}$ se vuelve cada vez más pequeño. En tramos tan estrechos, una curva suave cambia muy poco de altura, por lo que el techo plano del rectángulo se ajusta mucho mejor a la forma real de la función, reduciendo al mínimo los espacios vacíos y los sobrantes. Matemáticamente, esto queda demostrado en nuestra fórmula $S_n = \frac{14}{3} - \frac{2}{3n^2}$: a medida que $n$ se hace grande, la diferencia $\frac{2}{3n^2}$ tiende directamente a cero, haciendo que la suma de rectángulos coincida de forma exacta con la integral definida $\int_0^2 (x^2+1)\,dx = \frac{14}{3}$.

---

## 5. Escenas de Manim y Participación en el Video (Criterios V4, V5, V6)

Las escenas fueron desarrolladas en **Manim Community v0.22.0** (Python 3.12). Todos los gráficos y tablas toman sus valores de `scenes/config.py`. En el video, de **5:55 minutos** de duración, los cuatro integrantes participan explicando contenido matemático con su propia voz y son identificados por su nombre en pantalla:

| Escena / Archivo | Tramo en Video | Integrante (Voz) | Contenido Explicado y Animación |
| :--- | :---: | :--- | :--- |
| **Presentación** | 0:00 – 0:17 | **Denys Sofía Rodríguez** | Título del proyecto, curso, grupo, integrantes, tema y pregunta central (en pantalla). |
| **Escena 1: Construcción ($n=4$)**<br>`escena1_construccion.py` | 0:17 – 0:47<br>0:47 – 1:41<br>1:41 – 2:35 | **Paulo Villalobos**<br>**Denys Sofía Rodríguez**<br>**Renato Carrasco** | • **Paulo:** función $f(x)=x^2+1$ en $[0,2]$, condiciones ($f$ continua y positiva) y pregunta central.<br>• **Sofía:** partición regular en $n=4$, cálculo de $\Delta x = 0.5$, punto muestra (punto medio) y área $f(x_i^{\ast})\Delta x$.<br>• **Renato:** $S_4=\frac{37}{8}=4.625$, cálculo paso a paso de $A_1 = 0.53125$ y significado de $S_n=\sum f(x_i^{\ast})\Delta x$. |
| **Escena 2: Refinamiento**<br>`escena2_refinamiento.py` | 2:35 – 3:00<br>3:00 – 3:53 | **Renato Carrasco**<br>**Denys Sofía Rodríguez** | • **Renato:** paso de $n=4$ a $n=8$, $\Delta x$ se reduce a la mitad ($0.25$).<br>• **Sofía:** $n=16$ y $n=32$ ($S_{32} = 4.666016$), tabla comparativa, valor exacto $\frac{14}{3}$ y diferencias $0.041667 \to 0.000651$. |
| **Escena 3: Límite e Integral**<br>`escena3_integral.py` | 3:53 – 4:29<br>4:29 – 5:21 | **Antonio Lara**<br>**Paulo Villalobos** | • **Antonio:** refinamiento, $\Delta x=\frac{b-a}{n}\to 0$ cuando $n\to\infty$, el límite de las sumas como integral definida y por qué no se construyen infinitos rectángulos.<br>• **Paulo:** fórmula $S_n=\frac{14}{3}-\frac{2}{3n^2}$ (comprobada con la tabla) y error $\frac{2}{3n^2}$ para $n=4$ y $n=32$, que tiende a cero. |
| **Respuesta y cierre** | 5:21 – 5:40<br>5:40 – 5:55 | **Paulo, Sofía, Renato**<br>**Antonio Lara** | • Respuesta a la pregunta central y conexión con la integral definida.<br>• Créditos: integrantes, fuentes, recursos y declaración de IA. |

---

## 6. Parámetros del Código y Respuestas ante Variaciones (Criterios D4 y D5)

El archivo `scenes/config.py` centraliza la función `f(x) = x**2 + 1`, el intervalo `a = 0.0`, `b = 2.0`, la lista `n_values = [4, 8, 16, 32]` y el tipo de muestreo `sample_type = "center"` (con soporte para `"left"`, `"center"` y `"right"`):
* **¿Qué pasa si usamos extremos izquierdos o derechos en vez de puntos medios?**  
  Como la función $f(x)=x^2+1$ es creciente en $[0,2]$, si usamos extremos izquierdos todos los rectángulos quedan completamente por debajo de la curva (subestimación). Si usamos extremos derechos, sobresalen por arriba (sobreestimación). En ambos casos la convergencia es más lenta (lineal $1/n$), pero al tomar el límite cuando $n \to \infty$ ambos métodos llegan al mismo valor exacto: $\frac{14}{3}$. En el código solo bastaría cambiar `sample_type = "left"` o `"right"`.
* **¿Qué pasa si cambiamos el intervalo a $[0,4]$?**  
  Para un mismo número de rectángulos, el ancho $\Delta x = \frac{4-0}{n}$ se duplicaría. Los rectángulos serían el doble de anchos, por lo que el error inicial sería mayor y se necesitarían más subdivisiones para lograr la misma cercanía. En el código simplemente se modifica `b = 4.0`.

---

## 7. Fuentes y Referencias Consultadas (Criterios V7a, V7b, V7c)

*(Detalle completo en [`docs/referencias.md`](https://github.com/sofiarodrigueznog/EID-Grupo-3/blob/main/docs/referencias.md))*

1. **Apunte de la Asignatura:** Higueras Cheuquepan, N. (2026). *Introducción a la integral*. MAT1188 Cálculo Intermedio, Universidad Católica de Temuco.
2. **Libro Complementario 1:** Stewart, J. (2012). *Cálculo de una variable. Trascendentes tempranas* (7.ª ed.). Cengage Learning. ISBN 978-607-481-881-9. Secciones 5.1 ("Áreas y distancias", p. 360) y 5.2 ("La integral definida", p. 371).
3. **Libro Complementario 2:** Strang, G. y Herman, E. (2022). *Cálculo*, vol. 1, §5.1 ("Aproximación de áreas"). OpenStax. Disponible en: [https://openstax.org/books/cálculo-volumen-1/pages/5-1-aproximacion-de-areas](https://openstax.org/books/c%C3%A1lculo-volumen-1/pages/5-1-aproximacion-de-areas).
4. **Referencia Visual:** Sanderson, G. [3Blue1Brown]. (2017). *Integration and the fundamental theorem of calculus* [Video]. YouTube (min. 8:20–11:18). Disponible en: [https://www.youtube.com/watch?v=rfG8ce4nNh0](https://www.youtube.com/watch?v=rfG8ce4nNh0).
5. **Documentación de Software:** The Manim Community Developers (2026). *CoordinateSystem* (v0.22.0) – Método `get_riemann_rectangles`. Disponible en: [https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html).

---

## 8. Declaración de Uso de Inteligencia Artificial (Criterios V7d, V7e)

*(Detalle completo en [`docs/declaracion_ia.md`](https://github.com/sofiarodrigueznog/EID-Grupo-3/blob/main/docs/declaracion_ia.md))*

El equipo utilizó herramientas de Inteligencia Artificial como asistentes técnicos con supervisión y validación humana directa:
* **Denys Sofía Rodríguez Noguera:** Claude (Anthropic) para organizar carpetas del repositorio, configurar la validación de ramas en GitHub Actions y coordinar tareas en Jira. *Verificación:* Pruebas manuales de ejecución y revisión de PRs antes de incorporar a `main`.
* **Paulo Villalobos Aravena:** GitHub Copilot para apoyo con comandos de Git y ChatGPT (OpenAI) para revisar redacción en `teoria.md` y `ejemplo.md`. *Verificación:* Deducción de cálculos hecha a mano y contrastada con los libros de texto.
* **Antonio Ignacio Lara Fuentealba:** ChatGPT (OpenAI) para dudas sobre sintaxis de Manim Community (`config.py` y escenas 1 y 2) y diseño de tests unitarios. *Verificación:* Inspección visual de animaciones cuadro a cuadro y ejecución de `unittest`.
* **Renato Misrrain Carrasco Oviedo:** Antigravity / Gemini (Google DeepMind) para estructurar el script de auditoría (`verify.py`), el runner `render.py`, la Escena 3 y apoyar la locución. *Verificación:* Comprobación con aritmética de fracciones exactas y renderizado local de todas las escenas.
