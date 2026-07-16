"""Static content for the CIME landing page.

Kept here (instead of hard-coded in templates) so it is structured and
easy to migrate into database models when the platform scales into a
full back-office system. Source: CIME 2025 corporate brochure.
"""

# Each service: icon (inline SVG name), title, and short description.
SERVICES = [
    {
        "icon": "handshake",
        "title": "Representación Comercial y Entrada al Mercado",
        "summary": (
            "Solución integral para establecer presencia operativa en América "
            "Latina sin constituir de inmediato una entidad legal: rutas de "
            "expansión, representación de marca y constitución de sociedades."
        ),
    },
    {
        "icon": "shield",
        "title": "Estudios de Seguridad y Verificación de Antecedentes",
        "summary": (
            "Due diligence de personas y empresas: verificación de antecedentes, "
            "estudios de confiabilidad, poligrafía profesional y evaluación de "
            "proveedores para decisiones seguras."
        ),
    },
    {
        "icon": "calculator",
        "title": "Contabilidad, Auditoría Fiscal y Precio de Transferencia",
        "summary": (
            "Servicios contables y fiscales bajo NIIF y GAAP: estados financieros, "
            "auditorías internas y externas, nómina, impuestos y planificación "
            "tributaria eficiente."
        ),
    },
    {
        "icon": "scale",
        "title": "Asesoría Legal Corporativa",
        "summary": (
            "Desde contratos laborales hasta fusiones y adquisiciones: derecho "
            "comercial, tributario, laboral, migratorio y civil, con "
            "representación en todas las instancias."
        ),
    },
    {
        "icon": "coins",
        "title": "Gestión de Cobranza y Recuperación de Cartera",
        "summary": (
            "Recuperación de deudas vencidas cuidando la relación comercial: "
            "gestión temprana, cobro pre-jurídico y cobro jurídico con "
            "representación legal."
        ),
    },
    {
        "icon": "users",
        "title": "Reclutamiento, Selección de Personal y Call Center",
        "summary": (
            "Búsqueda, evaluación y contratación de talento, equipo de call center "
            "especializado y consultoría integral en recursos humanos y "
            "gestión del capital humano."
        ),
    },
    {
        "icon": "briefcase",
        "title": "Servicios PEO y EOR",
        "summary": (
            "Actuamos como Empleador de Registro (EOR) y Organización Profesional "
            "de Empleadores (PEO): contrate en distintos países sin establecer "
            "una entidad legal local."
        ),
    },
    {
        "icon": "passport",
        "title": "Asesoría Migratoria y Gestión de Visas",
        "summary": (
            "Acompañamiento personalizado a empresas y particulares para visas y "
            "permisos de residencia, con consulta inicial sin costo y gestión "
            "completa de trámites."
        ),
    },
    {
        "icon": "chart",
        "title": "Soporte Administrativo y Consultoría Financiera",
        "summary": (
            "Apoyo administrativo y asesoría financiera: inscripciones ante "
            "entidades estatales, planes de negocio, presupuestos, facturación "
            "y control de flujo de caja."
        ),
    },
    {
        "icon": "globe",
        "title": "Comercio Exterior",
        "summary": (
            "Internacionalización de principio a fin: importación y exportación, "
            "gestión de proveedores, control logístico, inspección de calidad y "
            "soporte legal comercial."
        ),
    },
]

# Reasons / value proposition (from "Razones para elegirnos").
REASONS = [
    {
        "icon": "globe",
        "title": "Atención en múltiples idiomas",
        "text": (
            "Trabajamos en estrecha colaboración con sus equipos para garantizar "
            "una comunicación efectiva y fluida en cada mercado."
        ),
    },
    {
        "icon": "puzzle",
        "title": "Soluciones a la medida",
        "text": (
            "Cada solución se personaliza para su situación, acompañando su "
            "inversión y desarrollo de negocios en Latinoamérica."
        ),
    },
    {
        "icon": "layers",
        "title": "Enfoque integral",
        "text": (
            "Asesoría legal, fiscal, administrativa, contable y de reclutamiento "
            "coordinada, para avanzar con rapidez y seguridad."
        ),
    },
    {
        "icon": "star",
        "title": "Excelencia en el servicio",
        "text": (
            "Atención personalizada, gestión eficiente de proyectos y altos "
            "estándares de calidad en cada etapa."
        ),
    },
]

# Office network (from "eje corporativo - Paraguay").
OFFICES = [
    {
        "city": "Asunción",
        "role": "Casa matriz · Eje corporativo",
    },
    {
        "city": "Coronel Oviedo",
        "role": "Oficina regional",
    },
    {
        "city": "Ciudad del Este",
        "role": "Oficina regional",
    },
]

# Headline metrics.
STATS = [
    {"value": "+25", "label": "Años de trayectoria"},
    {"value": "3", "label": "Oficinas en Paraguay"},
    {"value": "10", "label": "Áreas de servicio"},
    {"value": "100%", "label": "Enfoque integral"},
]

# Interior gallery (files under static/landing/img/gallery/).
GALLERY = [
    ("interior-1.jpg", "Recepción principal"),
    ("interior-3.jpg", "Área de trabajo"),
    ("interior-7.jpg", "Doble altura y hall central"),
    ("interior-4.jpg", "Sala de espera"),
    ("interior-2.jpg", "Oficinas con vista panorámica"),
    ("interior-6.jpg", "Mezanine y salas de reunión"),
]
