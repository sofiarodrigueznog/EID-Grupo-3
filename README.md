# De pocos rectángulos a una mejor aproximación

**MAT1188 – Cálculo Intermedio** · Ingeniería Civil Informática, segundo año
Proyecto de investigación y visualización con Manim · **Grupo 3**

Tablero de tareas: [Jira EID](https://eid-conicas-y-limites.atlassian.net/jira/software/projects/EID/boards/34)

## Integrantes

| Integrante | GitHub |
|---|---|
| Denys Sofía Rodríguez Noguera | [@sofiarodrigueznog](https://github.com/sofiarodrigueznog) |
| Paulo Villalobos Aravena | [@notKechai](https://github.com/notKechai) |
| Renato Misrrain Carrasco Oviedo | [@RCarrascoO](https://github.com/RCarrascoO) |
| Antonio Ignacio Lara Fuentealba | [@alara2024uct](https://github.com/alara2024uct) |

## Tema

**Eje 3 · Aproximación y refinamiento.** A partir del apunte base *Introducción a la integral*, trabajamos con una función y un intervalo fijos, y con un mismo criterio para elegir los puntos muestra. Construimos sumas de Riemann aumentando el número de subintervalos (n = 4, 8, 16 y 32), analizamos la relación

$$\Delta x = \frac{b-a}{n}$$

y comparamos los valores numéricos de cada suma para ver cómo se acercan entre sí y cómo este proceso prepara la idea de integral definida.

## Pregunta central

> ¿Por qué una suma de Riemann puede aproximar cada vez mejor una región cuando aumentamos el número de rectángulos?

## Escenas

| Escena | Contenido | Ticket |
|---|---|---|
| 1 · Construcción (n = 4) | Ejes, gráfica, partición, Δx, puntos muestra y rectángulos uno a uno, con el valor de S₄ | EID-8 |
| 2 · Refinamiento | Transformación de los rectángulos para n = 4 → 8 → 16 → 32: cómo se achica Δx y cambia S_n | EID-9 |
| 3 · Del límite a la integral | n → ∞ y Δx → 0 como proceso, y la conexión entre lím Σ f(xᵢ*)Δx y la integral de a a b | EID-10 |

Todas las escenas leen la función, el intervalo, la lista de n y el criterio de punto muestra desde `scenes/config.py` (EID-7). Así usan exactamente los mismos valores que los cálculos de `docs/ejemplo.md` (EID-3).

## Estructura

```
scenes/          escenas de Manim y config.py con los parámetros del ejemplo
docs/            teoría, ejemplo, referencias y declaración de uso de IA
assets/          imágenes y recursos del video
tests/           pruebas automáticas de scenes/config.py
verify.py        verificación independiente de los valores de S_n
requirements.txt dependencias con versiones fijas
```

## Versiones y dependencias

| Herramienta | Versión |
|---|---|
| Python | 3.12 |
| Manim Community | 0.22.0 |
| Cairo y Pango | las que instale el gestor de paquetes (FFmpeg ya viene incluido con Manim) |
| LaTeX (para `MathTex`) | MacTeX / MiKTeX / TeX Live |

Manim requiere Python 3.11 o superior. Usamos 3.12 para que todo el grupo tenga la misma versión; queda fijada en `.python-version` y Manim en `requirements.txt`.

## Instalación

**macOS**

```bash
brew install python@3.12 cairo pango pkg-config
brew install --cask mactex-no-gui
```

**Windows:** instala Python 3.12 desde python.org y [MiKTeX](https://miktex.org/).

**Linux (Debian/Ubuntu)**

```bash
sudo apt install python3.12-venv build-essential libcairo2-dev libpango1.0-dev pkg-config texlive texlive-latex-extra
```

**Entorno del proyecto (todos los sistemas)**

```bash
python3.12 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Verificar los cálculos

Antes de renderizar, comprueba que los parámetros y los valores de $S_n$ sigan siendo correctos:

```bash
python -m unittest discover -s tests   # pruebas de scenes/config.py
python verify.py                      # recalcula S_n y lo compara con docs/ejemplo.md
```

Ambos comandos se corren desde la raíz del repositorio. `python tests/test_config.py` no funciona, porque desde ahí Python no encuentra la carpeta `scenes`.

## Renderizar

```bash
manim -pql scenes/escena1_construccion.py Escena1Construccion   # vista previa rápida (480p)
manim -pqh scenes/escena1_construccion.py Escena1Construccion   # calidad final (1080p)
```

`-p` abre el video al terminar, `-ql` renderiza en baja calidad y `-qh` en alta. Los videos quedan en `media/videos/`. Para las escenas 2 y 3 se cambia el archivo y la clase (`escena2_refinamiento.py` → `Escena2Refinamiento`, `escena3_integral.py` → `Escena3Integral`).

## Cómo trabajar

Cada tarea es un ticket de Jira (`EID-1`, `EID-2`, …), y todo el trabajo se hace en una rama con este formato:

```
EID-<número>/<descripcion-en-minusculas-con-guiones>
```

Ejemplos: `EID-1/teoria-del-tema`, `EID-8/escena-1-riemann`.

```bash
git checkout main
git pull
git checkout -b EID-1/teoria-del-tema
# ... trabajas ...
git add .
git commit -m "EID-1 agrega teoría de particiones"
git push -u origin EID-1/teoria-del-tema
```

Después abre un Pull Request hacia `main` con un título como `EID-1 Teoría del tema`.

### Reglas

- **No se puede subir directo a `main`.** Todo entra por Pull Request.
- **Las ramas con otro nombre son rechazadas** al hacer push, y el PR falla el check si la rama no cumple el formato.
- Cada PR necesita la **aprobación de Sofía** antes de mergearse.
- Al crear la rama, el ticket pasa solo a **En curso** en Jira; al mergear el PR pasa a **Listo**.
