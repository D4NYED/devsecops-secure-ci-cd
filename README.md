# DevSecOps Secure CI/CD

Proyecto práctico de DevSecOps orientado a la integración de controles de seguridad automatizados dentro de un pipeline CI/CD moderno.

El objetivo es demostrar cómo incorporar pruebas automatizadas, análisis de seguridad, escaneo de contenedores y generación de artefactos de seguridad desde las primeras fases del ciclo de desarrollo.

---

## Arquitectura

```text
Developer
    │
    ▼
Git Push / Pull Request
    │
    ▼
GitHub Actions
    │
    ├── Pytest
    ├── Bandit
    ├── Semgrep
    ├── Docker Build
    ├── Trivy
    ├── SBOM Generation
    └── Artifact Upload
```

---

## Tecnologías implementadas

* FastAPI
* Docker
* GitHub Actions
* Pytest
* Bandit
* Semgrep
* Trivy
* Syft
* CycloneDX

## Tecnologías planificadas

* OWASP ZAP
* SARIF Reports
* Security Gates
* Container Registry Integration

---

## Funcionalidades actuales

### Aplicación web

API desarrollada con FastAPI que expone endpoints básicos para validación y monitorización.

Endpoints disponibles:

```http
GET /
GET /health
```

### Contenerización

La aplicación se ejecuta dentro de un contenedor Docker basado en una imagen Python Slim.

### Hardening básico

Se aplica el principio de mínimo privilegio ejecutando la aplicación mediante un usuario dedicado no privilegiado.

```dockerfile
RUN useradd -m appuser

USER appuser
```

### Pruebas automatizadas

La aplicación dispone de pruebas automatizadas utilizando Pytest.

Actualmente se validan:

* Endpoint raíz
* Endpoint de salud

### Análisis SAST

La pipeline ejecuta análisis estático de seguridad mediante:

* Bandit
* Semgrep (OWASP Top 10 Ruleset)

### Seguridad de contenedores

Las imágenes Docker generadas son analizadas automáticamente mediante Trivy para detectar vulnerabilidades conocidas.

### Generación de SBOM

La pipeline genera automáticamente un Software Bill of Materials (SBOM) en formato CycloneDX utilizando Syft.

Los artefactos son publicados automáticamente en GitHub Actions para su descarga y auditoría.

### Integración continua

Cada push y pull request sobre la rama principal ejecuta automáticamente:

```text
Git Push / Pull Request
        │
        ▼
      Pytest
        │
        ▼
      Bandit
        │
        ▼
     Semgrep
        │
        ▼
   Docker Build
        │
        ▼
      Trivy
        │
        ▼
   Generate SBOM
        │
        ▼
   Upload Artifacts
        │
        ▼
      Success
```

---

## Evidencias

### Pipeline DevSecOps funcionando

![GitHub Actions Success](docs/screenshots/github-actions-success.png)

La pipeline ejecuta automáticamente:

* Instalación de dependencias
* Ejecución de pruebas
* Análisis SAST con Bandit
* Análisis SAST con Semgrep
* Construcción de imagen Docker
* Escaneo de vulnerabilidades con Trivy
* Generación de SBOM CycloneDX
* Publicación de artefactos

---

## Estructura del proyecto

```text
devsecops-secure-ci-cd/
├── .github/
│   └── workflows/
├── app/
├── docs/
│   └── screenshots/
├── reports/
├── tests/
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Estado actual

### Completado

* [x] Aplicación FastAPI
* [x] Contenerización con Docker
* [x] Usuario no privilegiado en contenedor
* [x] Tests automatizados con Pytest
* [x] Pipeline CI con GitHub Actions
* [x] Análisis SAST con Bandit
* [x] Análisis SAST con Semgrep
* [x] Escaneo de vulnerabilidades con Trivy
* [x] Generación de SBOM con Syft
* [x] Publicación de artefactos de seguridad

### Próximas fases

* [ ] OWASP ZAP (DAST)
* [ ] Informes SARIF
* [ ] Security Gates basados en severidad
* [ ] Publicación automática de imágenes
* [ ] GitHub Container Registry (GHCR)

---

## Objetivos de aprendizaje

* Integración Continua (CI)
* DevSecOps
* Container Security
* Static Application Security Testing (SAST)
* Dynamic Application Security Testing (DAST)
* Software Supply Chain Security
* SBOM Generation
* Automatización de controles de seguridad
* Hardening de contenedores

---

## Licencia

Proyecto desarrollado con fines educativos y de demostración técnica.
