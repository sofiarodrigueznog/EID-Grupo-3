# Declaración de Uso de Inteligencia Artificial

**MAT1188 – Cálculo Intermedio · Grupo 3**  
*Evaluación Integrada de Desempeño (EID) – Semestre 2026-2*

En cumplimiento de la pauta oficial del proyecto EID y del Código de Ética del equipo, los cuatro integrantes del Grupo 3 declaran de forma transparente las herramientas de Inteligencia Artificial generativa utilizadas durante el desarrollo del trabajo, sus finalidades específicas y los métodos de verificación humana aplicados.

---

## 1. Resumen de herramientas utilizadas por integrante

| Integrante | Rol en el Proyecto | Herramientas de IA | Áreas de Apoyo |
| :--- | :--- | :--- | :--- |
| **Denys Sofía Rodríguez Noguera** | Líder / Integración del video | **Claude** (Anthropic) | Estructura del repositorio, automatización CI y vinculación con Jira. |
| **Paulo Villalobos Aravena** | Matemática y explicación | **GitHub Copilot** y **ChatGPT** (OpenAI) | Gestión de ramas/commits en Git; revisión pedagógica y tecnicismo de la teoría y ejemplo. |
| **Antonio Ignacio Lara Fuentealba** | Visualización y código | **ChatGPT** (OpenAI) | Parametrización en Manim Community y diseño de pruebas unitarias. |
| **Renato Misrrain Carrasco Oviedo** | Apoyo técnico y auditoría | **Antigravity / Gemini** (Google DeepMind) | Script de auditoría (`verify.py`), runner multiplataforma (`render.py`), Escena 3 y locución del guion. |

---

## 2. Desglose detallado por integrante

### A. Denys Sofía Rodríguez Noguera
* **Herramienta empleada:** Claude (Anthropic).
* **Finalidad y componentes apoyados:**
  * Diseño de la arquitectura base del repositorio (`scenes/`, `docs/`, `assets/`, `requirements.txt`).
  * Configuración del flujo de automatización y validación de nombres de ramas en GitHub Actions (`.github/workflows/nombre-de-rama.yml`).
  * Estructuración del seguimiento de tareas y pruebas de integración con el tablero de Jira.
* **Verificación humana:** Supervisión y ejecución manual de los workflows en GitHub, revisión de cada Pull Request y aprobación formal antes de cada merge hacia la rama `main`.

### B. Paulo Villalobos Aravena
* **Herramientas empleadas:** GitHub Copilot y ChatGPT (OpenAI).
* **Finalidad y componentes apoyados:**
  * Asistencia técnica en la consola de Git para la resolución de comandos, prevención de conflictos y buenas prácticas en los mensajes de commit.
  * Revisión pedagógica y crítica de estilo en `docs/teoria.md` y `docs/ejemplo.md`, evaluando la claridad explicativa y calibrando el nivel de tecnicismo adecuado para compañeros de segundo año.
* **Verificación humana:** Todo el desarrollo matemático (deducción analítica del área bajo la curva, la fórmula cerrada $S_n = \frac{14}{3} - \frac{2}{3n^2}$ y el límite hacia la integral) fue resuelto analíticamente a mano y contrastado directamente con la bibliografía de referencia (*Stewart* y *OpenStax*).

### C. Antonio Ignacio Lara Fuentealba
* **Herramienta empleada:** ChatGPT (OpenAI).
* **Finalidad y componentes apoyados:**
  * Orientación en la sintaxis de Manim Community para centralizar los parámetros en `scenes/config.py`.
  * Apoyo en la lógica de las escenas 1 y 2 (`escena1_construccion.py` y `escena2_refinamiento.py`) y creación de la suite de pruebas unitarias (`tests/test_config.py`).
* **Verificación humana:** Renderizado e inspección visual frame a frame de las animaciones, ajuste manual de las posiciones de ejes, etiquetas y márgenes en pantalla para evitar cortes de texto, y ejecución exitosa de la suite de pruebas con `unittest`.

### D. Renato Misrrain Carrasco Oviedo
* **Herramienta empleada:** Antigravity / Gemini (Google DeepMind).
* **Finalidad y componentes apoyados:**
  * Apoyo en la arquitectura del script independiente de verificación matemática exacta en fracciones (`verify.py`).
  * Diseño del runner multiplataforma `render.py` con menú interactivo y CLI para facilitar la ejecución en Linux, macOS y Windows sin conflictos de `PYTHONPATH`.
  * Estructuración visual de la Escena 3 (`escena3_integral.py`) para conectar el límite con la integral y responder la Pregunta Central.
  * Asistencia en la adaptación del guion a una locución hablada natural y fluida.
* **Verificación humana:** Ejecución y auditoría independiente de todos los cálculos matemáticos, compilación de las escenas en 480p y 1080p en entorno local CachyOS, y comprobación de que cada valor visualizado coincide con la teoría.

---

## 3. Compromiso ético y defensa oral

El equipo declara que las herramientas de Inteligencia Artificial se utilizaron como apoyo metodológico y técnico. Ningún integrante incorporó código, demostraciones ni afirmaciones teóricas que no comprenda a cabalidad. Los cuatro integrantes dominan el proyecto completo y están plenamente capacitados para explicar y defender de forma oral cualquier aspecto conceptual, numérico o de programación durante la evaluación final.
