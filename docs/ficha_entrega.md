# Ficha de Entrega – Evaluación Integrada de Desempeño (EID)

**Curso / Asignatura:** MAT1188 – Cálculo Intermedio (Ingeniería Civil Informática · 2.º Año · Semestre 2026-2)  
**Grupo:** Grupo 3 (`G03`)  
**Tema:** Eje 3 · Aproximación y refinamiento — *«De pocos rectángulos a una mejor aproximación»*  
**Integrantes:**  
- **Denys Sofía Rodríguez Noguera** (`@sofiarodrigueznog`) — *Líder / Revisión e integración del video*  
- **Paulo Villalobos Aravena** (`@notKechai`) — *Matemática y explicación*  
- **Antonio Ignacio Lara Fuentealba** (`@alara2024uct`) — *Visualización y código Manim*  
- **Renato Misrrain Carrasco Oviedo** (`@RCarrascoO`) — *Apoyo matemática, visualización y auditoría*  

**Fecha de entrega:** 18 de octubre de 2026  

---

## 1. Identificación y Metadatos de Entrega (Criterio V8)

| Campo | Información Oficial |
| :--- | :--- |
| **Código y Asignatura** | MAT1188 – Cálculo Intermedio |
| **Número de Grupo** | Grupo 3 (`G03`) |
| **Integrantes del Equipo** | Denys Sofía Rodríguez Noguera, Paulo Villalobos Aravena, Antonio Ignacio Lara Fuentealba y Renato Misrrain Carrasco Oviedo |
| **Repositorio Público de GitHub** | [https://github.com/sofiarodrigueznog/EID-Grupo-3](https://github.com/sofiarodrigueznog/EID-Grupo-3) |
| **SHA del Commit Entregado** | `[PENDIENTE: Se completa mañana domingo al congelar código (EID-14)]` |
| **Nombre del Archivo de Video** | `MAT1188_EID_G03_2026.mp4` |
| **Duración Exacta del Video** | `[PENDIENTE: Se completa mañana domingo con el render final (EID-20)]` *(Rango exigido: 4:00 a 6:00 min)* |
| **Nombre de la Ficha PDF** | `MAT1188_EID_G03_2026.pdf` |
| **Código de Ética** | Entregado en Blackboard (`MAT1188_ETICA_G03_2026.pdf`) el 06 de octubre de 2026 |

### Mapa de Localización Documental en el Repositorio (V8d, V8e)

Para facilitar la revisión del equipo docente, todos los respaldos exigidos por la pauta se encuentran en rutas directas dentro del repositorio:

| Documento / Recurso | Ruta en el Repositorio | Propósito y Contenido |
| :--- | :--- | :--- |
| **Guion Técnico y Notas Matemáticas** | [`docs/guion.md`](https://github.com/sofiarodrigueznog/EID-Grupo-3/blob/main/docs/guion.md) | Guion completo sincronizado por escena, tiempos, locutores y desarrollo matemático hablado. |
| **Marco Teórico** | [`docs/teoria.md`](https://github.com/sofiarodrigueznog/EID-Grupo-3/blob/main/docs/teoria.md) | Definición formal de partición, puntos muestra, suma de Riemann, refinamiento e integral definida. |
| **Desarrollo Analítico del Ejemplo** | [`docs/ejemplo.md`](https://github.com/sofiarodrigueznog/EID-Grupo-3/blob/main/docs/ejemplo.md) | Cálculos paso a paso para $n=4, 8, 16, 32$, fórmula cerrada $S_n$ y comparación con el valor exacto. |
| **Fuentes y Bibliografía** | [`docs/referencias.md`](https://github.com/sofiarodrigueznog/EID-Grupo-3/blob/main/docs/referencias.md) | Referencias bibliográficas completas (ISBN, secciones, páginas y enlaces verificables). |
| **Declaración de Uso de IA** | [`docs/declaracion_ia.md`](https://github.com/sofiarodrigueznog/EID-Grupo-3/blob/main/docs/declaracion_ia.md) | Registro detallado por integrante de herramientas de IA, finalidades y verificación humana. |
| **Configuración Centralizada** | [`scenes/config.py`](https://github.com/sofiarodrigueznog/EID-Grupo-3/blob/main/scenes/config.py) | Parámetros únicos ($f$, $[a,b]$, $n$, punto medio) consumidos por todas las escenas. |
| **Auditoría Matemática Exacta** | [`verify.py`](https://github.com/sofiarodrigueznog/EID-Grupo-3/blob/main/verify.py) | Script independiente en aritmética racional (`fractions.Fraction`) que valida $S_n$ y la tabla. |
| **Runner Multiplataforma y Pruebas** | [`render.py`](https://github.com/sofiarodrigueznog/EID-Grupo-3/blob/main/render.py) / [`tests/test_config.py`](https://github.com/sofiarodrigueznog/EID-Grupo-3/blob/main/tests/test_config.py) | Automatización de renderizado (480p/1080p) y suite de 9 pruebas unitarias con `unittest`. |

---

## 2. Nómina de Integrantes y Responsabilidades

| Integrante | Cuenta GitHub | Responsabilidad Principal | Aporte Efectivo al Proyecto |
| :--- | :--- | :--- | :--- |
| **Denys Sofía Rodríguez Noguera** *(Líder)* | [@sofiarodrigueznog](https://github.com/sofiarodrigueznog) | Revisión e integración del video | Coordinación general, arquitectura del repositorio, workflows de CI, edición/montaje del MP4 final, locución y entrega en Blackboard. |
| **Paulo Villalobos Aravena** | [@notKechai](https://github.com/notKechai) | Matemática y explicación | Redacción del marco teórico (`teoria.md`), desarrollo analítico del ejemplo (`ejemplo.md`), deducción de la fórmula cerrada $S_n$, guion y locución. |
| **Antonio Ignacio Lara Fuentealba** | [@alara2024uct](https://github.com/alara2024uct) | Visualización y código | Parametrización en `scenes/config.py`, pruebas unitarias (`test_config.py`), programación de Escena 1 ($n=4$) y Escena 2 (refinamiento), y locución. |
| **Renato Misrrain Carrasco Oviedo** | [@RCarrascoO](https://github.com/RCarrascoO) | Apoyo matemática y visualización | Auditoría racional independiente (`verify.py`), runner multiplataforma (`render.py`), programación de Escena 3 (límite e integral), locución y ficha técnica. |

---

## 3. Tema Asignado y Pregunta Central

* **Eje temático:** Eje 3 · Aproximación y refinamiento.
* **Tema oficial:** *De pocos rectángulos a una mejor aproximación*.
* **Pregunta central:**
  > *«¿Por qué una suma de Riemann puede aproximar cada vez mejor una región cuando aumentamos el número de rectángulos?»*

---

## 4. Fundamentos Matemáticos y Desarrollo del Ejemplo (Criterios V1, V2, V3)

### A. Definición Formal y Glosario de Símbolos (V1a, V1b)
Dada una función $f:[a,b] \to \mathbb{R}$ definida en un intervalo cerrado y acotado $[a,b]$, una **partición regular** divide el intervalo en $n \in \mathbb{N}$ subintervalos de igual longitud $[x_{i-1}, x_i]$ mediante los nodos $x_i = a + i\Delta x$ para $i = 0, 1, \dots, n$. La **suma de Riemann** asociada se define formalmente como:

$$S_n = \sum_{i=1}^{n} f(x_i^*)\,\Delta x$$

* **$[a,b]$:** Intervalo cerrado de integración (en nuestro ejemplo, $[0,2]$).
* **$n$:** Número entero positivo de subintervalos (y de rectángulos de aproximación).
* **$\Delta x = \frac{b-a}{n}$:** Ancho uniforme de cada subintervalo (base de cada rectángulo). Representa también la norma de la partición $\|P\|$.
* **$x_i^* \in [x_{i-1}, x_i]$:** Punto muestra elegido dentro del $i$-ésimo subintervalo. En este proyecto utilizamos el **punto medio**:
  $$x_i^* = \frac{x_{i-1} + x_i}{2} = a + \left(i - \frac{1}{2}\right)\Delta x$$
* **$f(x_i^*)$:** Valor de la función en el punto muestra (altura del $i$-ésimo rectángulo).
* **$A_i = f(x_i^*)\,\Delta x$:** Área geométrica del $i$-ésimo rectángulo.
* **$\sum_{i=1}^n$:** Operador de suma finita que acumula las áreas de los $n$ rectángulos.

### B. Condiciones Necesarias y Distinción Conceptual (V1c, V1d)
1. **Condición de integrabilidad (Continuidad):** La función $f(x) = x^2 + 1$ es polinómica y, por tanto, **continua** en todo el intervalo cerrado $[0,2]$. La continuidad en un compacto garantiza que $f$ es integrable en el sentido de Riemann, es decir, que el límite $\lim_{n\to\infty} S_n$ existe, es finito y es único con independencia del criterio de punto muestra elegido.
2. **Condición de positividad (Área geométrica vs. Área neta signada):** En general, una suma de Riemann y la integral definida representan un **área neta con signo** (las regiones bajo el eje $x$ aportan signo negativo). Sin embargo, como $f(x) = x^2 + 1 \geq 1 > 0$ para todo $x \in [0,2]$, cada altura $f(x_i^*) > 0$ y la suma de Riemann coincide exactamente con una aproximación del **área geométrica** bajo la curva.
3. **Distinción conceptual:**
   * **Suma de Riemann ($S_n$):** Aproximación discreta y finita calculada para un número fijo de rectángulos $n$.
   * **Proceso de refinamiento y límite ($\lim_{n\to\infty} S_n$):** Proceso dinámico en el que $n$ crece indefinidamente provocando que $\Delta x = \frac{b-a}{n} \to 0$.
   * **Integral definida ($\int_a^b f(x)\,dx$):** Número real exacto definido como el valor al cual converge dicho límite:
     $$\int_a^b f(x)\,dx = \lim_{n\to\infty} \sum_{i=1}^{n} f(x_i^*)\,\Delta x$$

### C. Desarrollo Analítico del Ejemplo y Deducción de la Fórmula Cerrada (V2a–d)
Para $f(x) = x^2 + 1$ en $[0,2]$, el **valor exacto** mediante el Teorema Fundamental del Cálculo es:
$$\int_0^2 (x^2 + 1)\,dx = \left[ \frac{x^3}{3} + x \right]_0^2 = \frac{2^3}{3} + 2 = \frac{8}{3} + 2 = \frac{14}{3} \approx 4.666667$$

Con partición regular en $[0,2]$, tenemos $\Delta x = \frac{2}{n}$ y puntos medios $x_i^* = \left(i - \frac{1}{2}\right)\frac{2}{n} = \frac{2i-1}{n}$.
* **Cálculo explícito para $n=4$:** $\Delta x = \frac{1}{2}$ y puntos medios $x_1^* = \frac{1}{4}, x_2^* = \frac{3}{4}, x_3^* = \frac{5}{4}, x_4^* = \frac{7}{4}$.
  $$S_4 = \frac{1}{2}\left[\left(\frac{1}{16}+1\right) + \left(\frac{9}{16}+1\right) + \left(\frac{25}{16}+1\right) + \left(\frac{49}{16}+1\right)\right] = \frac{1}{2}\left[\frac{84}{16} + 4\right] = \frac{1}{2}\left[\frac{37}{4}\right] = \frac{37}{8} = 4.625$$
* **Deducción algebraica de la fórmula cerrada para cualquier $n$:**
  Sustituyendo $x_i^* = \frac{2i-1}{n}$ y $\Delta x = \frac{2}{n}$ en la definición de $S_n$:
  $$S_n = \sum_{i=1}^{n} \left[\left(\frac{2i-1}{n}\right)^2 + 1\right]\frac{2}{n} = \frac{2}{n}\left[\frac{1}{n^2}\sum_{i=1}^{n}(4i^2 - 4i + 1) + \sum_{i=1}^{n} 1\right]$$
  Aplicando las identidades de sumas de potencias $\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}$, $\sum_{i=1}^n i = \frac{n(n+1)}{2}$ y $\sum_{i=1}^n 1 = n$, se obtiene la identidad de cuadrados de impares $\sum_{i=1}^n (2i-1)^2 = \frac{n(4n^2-1)}{3}$. Al reemplazar:
  $$S_n = \frac{2}{n}\left[\frac{1}{n^2}\cdot\frac{n(4n^2-1)}{3} + n\right] = \frac{2(4n^2-1)}{3n^2} + 2 = \frac{8n^2 - 2 + 6n^2}{3n^2} = \frac{14n^2 - 2}{3n^2} = \frac{14}{3} - \frac{2}{3n^2}$$

### D. Tabla Comparativa de Refinamiento y Convergencia (V2d, V3a)

| $n$ | Ancho $\Delta x$ | Suma $S_n$ exacta | Suma $S_n$ decimal | Error absoluto $\left|\frac{14}{3} - S_n\right|$ | Error decimal |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **4** | $1/2 = 0.5000$ | $37/8$ | $4.625000$ | $1/24$ | $0.041667$ |
| **8** | $1/4 = 0.2500$ | $149/32$ | $4.656250$ | $1/96$ | $0.010417$ |
| **16** | $1/8 = 0.1250$ | $597/128$ | $4.664063$ | $1/384$ | $0.002604$ |
| **32** | $1/16 = 0.0625$ | $2389/512$ | $4.666016$ | $1/1536$ | $0.000651$ |
| **$n \to \infty$** | $\Delta x \to 0$ | **$\mathbf{14/3}$** | **$4.666667$** | **$0$** | **$0.000000$** |

* **Por qué $S_n$ subestima ligeramente a $\frac{14}{3}$:** Como $f(x) = x^2+1$ tiene segunda derivada positiva ($f''(x) = 2 > 0$, función estrictamente convexa en $[0,2]$), la recta tangente en el punto medio de cada subintervalo queda por debajo de la curva. Por ello, el exceso de área a un lado del punto medio es ligeramente menor que el defecto al otro lado, produciendo el término negativo $-\frac{2}{3n^2}$.
* **Convergencia cuadrática $O(1/n^2)$:** Al usar puntos medios, el error es proporcional a $\frac{1}{n^2}$. Cada vez que duplicamos $n$ ($4 \to 8 \to 16 \to 32$), el error se divide exactamente por $4$ ($\frac{1}{24} \to \frac{1}{96} \to \frac{1}{384} \to \frac{1}{1536}$), convergiendo mucho más rápido que las sumas por extremo izquierdo o derecho ($O(1/n)$).

### E. Respuesta Fundamentada a la Pregunta Central (V3c, V3d, V3e)
> Una suma de Riemann aproxima cada vez mejor la región porque, al mantener fijo el intervalo $[a,b]$ y aumentar el número de rectángulos $n$, el ancho de cada subintervalo $\Delta x = \frac{b-a}{n}$ disminuye hacia cero. En subintervalos cada vez más angostos, una función continua varía muy poco dentro de cada tramo, por lo que la altura constante $f(x_i^*)$ evaluada en el punto muestra representa con mayor fidelidad el comportamiento real de la curva, reduciendo los triángulos curvilíneos de error (espacio sobrante y faltante). Analíticamente, esto se comprueba en nuestra expresión cerrada $S_n = \frac{14}{3} - \frac{2}{3n^2}$: cuando $n \to \infty$, el término de discrepancia $\frac{2}{3n^2} \to 0$, haciendo que las sumas discretas converjan al valor exacto de la integral definida $\int_0^2 (x^2+1)\,dx = \frac{14}{3}$.

---

## 5. Estructura del Video, Escenas de Manim y Participación Oral (Criterios V4, V5, V6)

Todas las escenas fueron programadas en **Manim Community v0.22.0** (Python 3.12) e importan sus parámetros desde `scenes/config.py`, garantizando coherencia matemática y visual absoluta. Cada integrante interviene con su propia voz explicando contenido matemático sustantivo y es identificado en pantalla:

| Bloque / Archivo de Escena | Tiempos Base | Integrante (Voz en Off) | Contenido Matemático y Visualización Sincronizada |
| :--- | :---: | :--- | :--- |
| **Presentación** *(Lámina inicial)* | Intro | **Sofía Rodríguez** | Identificación del curso, Grupo 3, nómina de integrantes, eje temático y título del proyecto. |
| **Escena 1: Construcción ($n=4$)**<br>`scenes/escena1_construccion.py`<br>Clase: `Escena1Construccion` | 0:00 – 0:09<br>0:09 – 0:22<br>0:22 – 0:29.5 | **Paulo Villalobos**<br>**Sofía Rodríguez**<br>**Renato Carrasco** | • **Paulo:** Planteamiento del área bajo $f(x)=x^2+1 \geq 0$ en $[0,2]$ y formulación de la Pregunta Central.<br>• **Sofía:** Partición regular en $n=4$, cálculo de $\Delta x = \frac{2-0}{4} = 0.5$ y criterio de punto medio $x_i^* = \frac{x_{i-1}+x_i}{2}$.<br>• **Renato:** Construcción animada de los 4 rectángulos, cálculo explícito de $A_1 = f(0.25)\cdot 0.5 = 0.53125$ y suma total $S_4 = \frac{37}{8} = 4.625$. |
| **Escena 2: Refinamiento**<br>`scenes/escena2_refinamiento.py`<br>Clase: `Escena2Refinamiento` | 0:00 – 0:17<br>0:17 – 0:35.2 | **Renato Carrasco**<br>**Sofía Rodríguez** | • **Renato:** Transición dinámica manteniendo fijos $f(x)$ y $[0,2]$ para $n=4 \to 8$, reducción de $\Delta x$ ($0.5 \to 0.25$) y mejora a $S_8 = 4.656250$.<br>• **Sofía:** Refinamiento a $n=16$ y $n=32$ ($S_{32} = 4.666016$), llenado de la tabla comparativa, cálculo de $\int_0^2(x^2+1)dx = \frac{14}{3}$ y caída del error de $0.041667$ a $0.000651$. |
| **Escena 3: Límite e Integral**<br>`scenes/escena3_integral.py`<br>Clase: `Escena3Integral` | 0:00 – 0:18<br>0:18 – 0:23<br>0:23 – 0:27.4 | **Antonio Lara**<br>**Paulo Villalobos**<br>**Todos (Cierre)** | • **Antonio:** Interpretación del proceso $n \to \infty \implies \Delta x \to 0$ y paso formal $\lim_{n\to\infty}\sum f(x_i^*)\Delta x = \int_a^b f(x)dx$, distinguiendo la visualización finita ($n=32$) del concepto de límite.<br>• **Paulo:** Análisis algebraico del error $\frac{2}{3n^2} \to 0$ a partir de $S_n = \frac{14}{3} - \frac{2}{3n^2}$.<br>• **Paulo, Sofía, Renato y Antonio:** Respuesta síntesis a la Pregunta Central y créditos bibliográficos. |

---

## 6. Arquitectura del Código y Respuesta ante Variaciones (Criterios D4 y D5)

Para respaldar la trazabilidad técnica del proyecto, todos los cálculos y gráficos dependen de `scenes/config.py`:
* **Parámetros centrales:** `f(x)` define $x^2+1$; `a = 0.0` y `b = 2.0` fijan el intervalo; `n_values = [4, 8, 16, 32]` controla las iteraciones; `sample_type = "center"` define el punto medio mediante un diccionario de desplazamientos (`"left": 0.0`, `"center": 0.5`, `"right": 1.0`).
* **Comportamiento ante variaciones (Criterio D5):**
  1. *Cambio a extremos izquierdos o derechos (`sample_type = "left"` o `"right"`):* Como $f(x)=x^2+1$ es estrictamente creciente en $[0,2]$, con extremos izquierdos todos los rectángulos quedan inscrito bajo la curva (subestimación, $S_n < \frac{14}{3}$), mientras que con extremos derechos sobresalen por encima (sobreestimación, $S_n > \frac{14}{3}$). En ambos casos el orden de convergencia pasa de $O(1/n^2)$ a $O(1/n)$, pero el límite cuando $n \to \infty$ sigue siendo $\frac{14}{3}$.
  2. *Cambio del intervalo (p. ej. $[0,4]$ modificando `b = 4.0`):* Para un mismo $n$, el ancho $\Delta x = \frac{4}{n}$ se duplica, los rectángulos son más anchos y el error para un $n$ fijo aumenta, requiriendo un $n$ mayor para alcanzar la misma precisión.
  3. *Cambio de la función (p. ej. $f(x) = 2x + 1$ lineal):* Con punto medio (`"center"`), el triángulo que sobra a la derecha del punto medio es congruente con el triángulo que falta a la izquierda, por lo que $S_n$ da el área exacta desde $n=1$ (error cero).

---

## 7. Fuentes y Referencias Consultadas (Criterio V7a, V7b, V7c)

*(Detalle completo disponible en el repositorio en [`docs/referencias.md`](https://github.com/sofiarodrigueznog/EID-Grupo-3/blob/main/docs/referencias.md))*

1. **Apunte Base de la Asignatura:** Higueras Cheuquepan, N. (2026). *Introducción a la integral*. MAT1188 Cálculo Intermedio, Universidad Católica de Temuco. Base conceptual común del proyecto.
2. **Fuente Matemática Complementaria 1:** Stewart, J. (2012). *Cálculo de una variable. Trascendentes tempranas* (7.ª ed.; M. C. Rodríguez Pedroza, trad.). Cengage Learning. ISBN 978-607-481-881-9. Secciones 5.1 ("Áreas y distancias", p. 360) y 5.2 ("La integral definida", p. 371).
3. **Fuente Matemática Complementaria 2:** Strang, G., Herman, E. et al. (2022). *Cálculo*, vol. 1, §5.1 ("Aproximación de áreas"). OpenStax. Disponible en: [https://openstax.org/books/cálculo-volumen-1/pages/5-1-aproximacion-de-areas](https://openstax.org/books/c%C3%A1lculo-volumen-1/pages/5-1-aproximacion-de-areas).
4. **Recurso Audiovisual Complementario:** Sanderson, G. [3Blue1Brown]. (2017, 5 de mayo). *Integration and the fundamental theorem of calculus | Chapter 8, Essence of calculus* [Video]. YouTube (min. 8:20–11:18). Disponible en: [https://www.youtube.com/watch?v=rfG8ce4nNh0](https://www.youtube.com/watch?v=rfG8ce4nNh0).
5. **Documentación Oficial de Software:** The Manim Community Developers (2026). *CoordinateSystem* (v0.22.0) – Método `get_riemann_rectangles`. Manim Community Documentation. Disponible en: [https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html).

---

## 8. Declaración de Uso de Inteligencia Artificial y Verificación Humana (Criterio V7d, V7e)

*(Declaración exhaustiva disponible en el repositorio en [`docs/declaracion_ia.md`](https://github.com/sofiarodrigueznog/EID-Grupo-3/blob/main/docs/declaracion_ia.md))*

El equipo declara de forma transparente el uso de herramientas de Inteligencia Artificial generativa como apoyo técnico y metodológico, bajo estricta validación humana:

* **Denys Sofía Rodríguez Noguera:** Utilizó **Claude** (Anthropic) para estructurar la arquitectura del repositorio, configurar el workflow de validación de ramas en GitHub Actions (`.github/workflows/nombre-de-rama.yml`) y diseñar las pruebas de automatización con Jira. *Verificación:* Ejecución manual de pruebas en PRs y revisión humana antes de cada merge a `main`.
* **Paulo Villalobos Aravena:** Utilizó **GitHub Copilot** para asistencia en comandos de Git/GitHub y **ChatGPT** (OpenAI) para revisión crítica de claridad pedagógica y calibración de tecnicismo en `docs/teoria.md` y `docs/ejemplo.md`. *Verificación:* Deducción analítica hecha a mano de todas las sumatorias, de la fórmula cerrada $S_n = \frac{14}{3} - \frac{2}{3n^2}$ y contraste con *Stewart* y *OpenStax*.
* **Antonio Ignacio Lara Fuentealba:** Utilizó **ChatGPT** (OpenAI) para consultar la sintaxis de parametrización en Manim Community (`scenes/config.py`), funciones de las escenas 1 y 2, y estructura de pruebas unitarias (`tests/test_config.py`). *Verificación:* Renderizado local e inspección visual cuadro a cuadro de ejes, escalas y etiquetas, además de ejecución de la suite `unittest`.
* **Renato Misrrain Carrasco Oviedo:** Utilizó **Antigravity / Gemini** (Google DeepMind) como apoyo en el diseño del script de auditoría racional (`verify.py`), el runner multiplataforma (`render.py`), la programación de la Escena 3 y el pulido de fluidez del guion. *Verificación:* Comprobación cruzada con aritmética exacta (`fractions.Fraction`), compilación de las escenas en 480p y 1080p en Linux y validación de concordancia 1:1 entre código, tabla y teoría.
