# DevSecOps Secure CI/CD

Proyecto práctico de DevSecOps diseñado para integrar controles de seguridad automatizados dentro de un pipeline CI/CD moderno.

## Tecnologías

- Docker
- GitHub Actions
- Trivy
- Semgrep
- OWASP ZAP
- FastAPI

## Objetivos

- Automatizar la construcción de imágenes Docker
- Detectar vulnerabilidades en dependencias y contenedores
- Realizar análisis SAST del código fuente
- Ejecutar pruebas DAST sobre la aplicación desplegada
- Generar informes automáticos de seguridad
- Implementar controles de calidad antes del despliegue

## Pipeline

```text
Git Push
   │
   ▼
Build Docker Image
   │
   ▼
Trivy Scan
   │
   ▼
Semgrep Scan
   │
   ▼
OWASP ZAP Scan
   │
   ▼
Security Reports
```

## Estructura del proyecto

```text
devsecops-secure-ci-cd/
├── app/
├── docs/
├── reports/
├── .github/
│   └── workflows/
├── README.md
└── .gitignore
```

## Estado

🚧 En desarrollo

## Próximas funcionalidades

- [ ] Aplicación FastAPI vulnerable para pruebas
- [ ] Pipeline GitHub Actions
- [ ] Escaneo con Trivy
- [ ] Análisis SAST con Semgrep
- [ ] Escaneo DAST con OWASP ZAP
- [ ] Generación de reportes SARIF
- [ ] Security Gates basados en severidad
