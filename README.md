<<<<<<< Updated upstream
# MicroservicioColaborativo
Evaluación Parcial 1 DOY0101 Docente: Crisrian Bugueno Pantoja
# 🛠️ Microservicio de Gestión de Tareas

Microservicio desarrollado en Python como base para el pipeline DevOps de la asignatura **Ingeniería DevOps (DOY0101)**.

---

##  Descripción del Proyecto

API simple de gestión de tareas que permite agregar, listar y completar tareas.
Este repositorio implementa buenas prácticas de control de versiones y flujos de trabajo colaborativo usando Git, GitHub y GitHub Actions.

---

##  Estrategia de Ramificación: GitFlow

Se eligió **GitFlow** como estrategia de ramificación por las siguientes razones:

- Permite separar claramente el código en producción (`main`) del código en desarrollo (`develop`).
- Facilita el trabajo en equipo mediante ramas específicas para cada funcionalidad (`feature/`) y correcciones urgentes (`hotfix/`).
- Es ideal para proyectos con ciclos de entrega definidos, como este proyecto académico.
- Proporciona mayor trazabilidad del código, cumpliendo con los estándares de CI/CD.

### Comparación con Trunk-Based Development

| Característica | GitFlow | Trunk-Based |
|---|---|---|
| Ramas principales | main + develop | Solo main |
| Ideal para | Equipos medianos, releases programados | Equipos grandes, despliegue continuo |
| Complejidad | Media | Baja |
| Trazabilidad | Alta | Media |

---

##  Estructura de Ramas

| Rama | Propósito |
|---|---|
| `main` | Código en producción, estable |
| `develop` | Integración de nuevas funcionalidades |
| `feature/<Matias>` | Desarrollo de nuevas funcionalidades |
| `hotfix/<Gabriel >` | Correcciones urgentes en producción |

---

### Tipos permitidos:

| Tipo | Uso |
|---|---|
| `feat` | Nueva funcionalidad |
| `fix` | Corrección de bug |
| `docs` | Cambios en documentación |
| `refactor` | Refactorización de código |
| `test` | Añadir o modificar tests |
| `chore` | Tareas de mantenimiento |

### Ejemplos:
feat: agregar endpoint para completar tarea
fix: corregir asignación de ID duplicado
docs: actualizar README con convenciones de commits

---

##  Flujo de Merge

### Para features:
1. Crear rama desde `develop`: `git checkout -b feature/nombre develop`
2. Desarrollar y hacer commits
3. Abrir Pull Request hacia `develop`
4. Revisión de al menos 1 compañero
5. Merge a `develop` y eliminar rama feature

### Para hotfix:
1. Crear rama desde `main`: `git checkout -b hotfix/nombre main`
2. Aplicar corrección
3. Abrir Pull Request hacia `main` Y hacia `develop`
4. Merge en ambas ramas

---

##  GitHub Actions — CI/CD

Se configuró un workflow de GitHub Actions que se ejecuta automáticamente en:
- Cada `push` a la rama `develop`
- Cada Pull Request hacia `main`

### ¿Qué hace el workflow?
1. Instala las dependencias del proyecto
2. Ejecuta tests automáticos
3. Verifica que el código no tiene errores de sintaxis

### Rol en CI/CD:
- **CI (Integración Continua):** Valida automáticamente cada cambio antes de integrarlo, evitando que código con errores llegue a producción.
- **CD (Despliegue Continuo):** Prepara la base para automatizar el despliegue cuando el código pasa todas las validaciones.

---

##  Estructura del Proyecto
microservicio-tareas/
│
├── app.py              # Lógica principal del microservicio
├── requirements.txt    # Dependencias del proyecto
├── README.md           # Documentación del repositorio
└── .github/
└── workflows/
└── ci.yml      # Pipeline de GitHub Actions


##  Integrantes

- Gabriel Ferrufino
- Matias Pulgar
=======
\# 🛠️ Microservicio de Gestión de Tareas



Microservicio desarrollado en Python como base para el pipeline DevOps de la asignatura \*\*Ingeniería DevOps (DOY0101)\*\*.



\---



\##  Descripción del Proyecto



API simple de gestión de tareas que permite agregar, listar y completar tareas.

Este repositorio implementa buenas prácticas de control de versiones y flujos de trabajo colaborativo usando Git, GitHub y GitHub Actions.



\---



\##  Estrategia de Ramificación: GitFlow



Se eligió \*\*GitFlow\*\* como estrategia de ramificación por las siguientes razones:



\- Permite separar claramente el código en producción (`main`) del código en desarrollo (`develop`).

\- Facilita el trabajo en equipo mediante ramas específicas para cada funcionalidad (`feature/`) y correcciones urgentes (`hotfix/`).

\- Es ideal para proyectos con ciclos de entrega definidos, como este proyecto académico.

\- Proporciona mayor trazabilidad del código, cumpliendo con los estándares de CI/CD.



\### Comparación con Trunk-Based Development



| Característica | GitFlow | Trunk-Based |

|---|---|---|

| Ramas principales | main + develop | Solo main |

| Ideal para | Equipos medianos, releases programados | Equipos grandes, despliegue continuo |

| Complejidad | Media | Baja |

| Trazabilidad | Alta | Media |



\---



\##  Estructura de Ramas



| Rama | Propósito |

|---|---|

| `main` | Código en producción, estable |

| `develop` | Integración de nuevas funcionalidades |

| `feature/<Matias>` | Desarrollo de nuevas funcionalidades |

| `hotfix/<Gabriel >` | Correcciones urgentes en producción |



\---



\### Tipos permitidos:



| Tipo | Uso |

|---|---|

| `feat` | Nueva funcionalidad |

| `fix` | Corrección de bug |

| `docs` | Cambios en documentación |

| `refactor` | Refactorización de código |

| `test` | Añadir o modificar tests |

| `chore` | Tareas de mantenimiento |



\### Ejemplos:

feat: agregar endpoint para completar tarea

fix: corregir asignación de ID duplicado

docs: actualizar README con convenciones de commits



\---



\##  Flujo de Merge



\### Para features:

1\. Crear rama desde `develop`: `git checkout -b feature/nombre develop`

2\. Desarrollar y hacer commits

3\. Abrir Pull Request hacia `develop`

4\. Revisión de al menos 1 compañero

5\. Merge a `develop` y eliminar rama feature



\### Para hotfix:

1\. Crear rama desde `main`: `git checkout -b hotfix/nombre main`

2\. Aplicar corrección

3\. Abrir Pull Request hacia `main` Y hacia `develop`

4\. Merge en ambas ramas



\---



\##  GitHub Actions — CI/CD



Se configuró un workflow de GitHub Actions que se ejecuta automáticamente en:

\- Cada `push` a la rama `develop`

\- Cada Pull Request hacia `main`



\### ¿Qué hace el workflow?

1\. Instala las dependencias del proyecto

2\. Ejecuta tests automáticos

3\. Verifica que el código no tiene errores de sintaxis



\### Rol en CI/CD:

\- \*\*CI (Integración Continua):\*\* Valida automáticamente cada cambio antes de integrarlo, evitando que código con errores llegue a producción.

\- \*\*CD (Despliegue Continuo):\*\* Prepara la base para automatizar el despliegue cuando el código pasa todas las validaciones.



\---



\##  Estructura del Proyecto

microservicio-tareas/

│

├── app.py              # Lógica principal del microservicio

├── requirements.txt    # Dependencias del proyecto

├── README.md           # Documentación del repositorio

└── .github/

└── workflows/

└── ci.yml      # Pipeline de GitHub Actions





\##  Integrantes



\- Gabriel Ferrufino

\- Matias Pulgar


