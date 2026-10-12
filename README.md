# EID — Cálculo Intermedio · Grupo 3 (N3)

Tablero de tareas: [Jira EID](https://eid-conicas-y-limites.atlassian.net/jira/software/projects/EID/boards/34)

## Cómo trabajar

Cada tarea es un ticket de Jira (`EID-1`, `EID-2`, …). Todo trabajo se hace en una rama con el ticket:

```
EID-<número>/<descripcion-en-minusculas-con-guiones>
```

Ejemplos: `EID-1/teoria-del-tema`, `EID-8/escena-1-riemann`.

### Paso a paso

```bash
git checkout main
git pull
git checkout -b EID-1/teoria-del-tema
# ... trabajas ...
git add .
git commit -m "EID-1 agrega teoría de particiones"
git push -u origin EID-1/teoria-del-tema
```

Luego abre un Pull Request hacia `main` (GitHub te muestra el botón) con el título `EID-1 Teoría del tema`.

### Reglas

- **No se puede pushear directo a `main`.** Todo entra por Pull Request.
- **Ramas con otro nombre son rechazadas** al hacer push, y el PR falla el check si la rama no cumple el formato.
- Cada PR necesita la **aprobación de Sofía** antes de mergearse.
- Al crear la rama, el ticket pasa solo a **En curso** en Jira; al mergear el PR pasa a **Listo**.
