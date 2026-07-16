# CIME — Consultoría Integral del Mercosur

Landing page corporativa construida con **Django 5**, pensada para escalar
hacia un sistema de back-office (gestión de clientes, leads, servicios, etc.).

## Requisitos

- Python 3.11+
- Windows / macOS / Linux

## Puesta en marcha

```bash
# 1. Crear y activar el entorno virtual
python -m venv venv
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# macOS / Linux:
source venv/bin/activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Migraciones (base de datos SQLite por defecto)
python manage.py migrate

# 4. Levantar el servidor de desarrollo
python manage.py runserver
```

Luego abrir http://127.0.0.1:8000/

## Estructura

```
016_CIME/
├── cime_project/        # Configuración del proyecto (settings, urls, wsgi)
├── landing/             # App de la landing
│   ├── content.py       # Contenido (servicios, oficinas, stats) — fácil de migrar a BD
│   ├── forms.py         # Formulario de contacto
│   ├── views.py         # Vista principal
│   ├── urls.py
│   ├── templates/landing/index.html
│   └── static/landing/  # CSS, JS e imágenes optimizadas
├── static/              # Estáticos globales del proyecto
├── media/               # Subidas de usuarios (para el futuro backend)
├── manage.py
└── requirements.txt
```

## Configuración por variables de entorno

El proyecto lee estas variables (con valores por defecto para desarrollo):

| Variable | Descripción |
|----------|-------------|
| `DJANGO_SECRET_KEY` | Clave secreta (obligatoria en producción) |
| `DJANGO_DEBUG` | `True` / `False` |
| `DJANGO_ALLOWED_HOSTS` | Hosts separados por coma |
| `CIME_CONTACT_EMAIL` | Correo de contacto mostrado en la web |
| `CIME_CONTACT_PHONE` | Teléfono de contacto |
| `CIME_CONTACT_WHATSAPP` | Número de WhatsApp (formato internacional, solo dígitos) |

## Próximos pasos para escalar a un sistema de back-office

- Convertir `landing/content.py` en modelos (`Service`, `Office`, etc.) editables
  desde el admin de Django (`/admin/`).
- Persistir los leads del formulario de contacto en un modelo `Lead` y notificar
  por correo / integrar con un CRM.
- Añadir apps por dominio (clientes, expedientes, facturación) montadas en
  `cime_project/urls.py`.
- Servir estáticos en producción con WhiteNoise o un CDN (`collectstatic`).

---

Contenido e imágenes: brochure corporativo CIME 2025.
