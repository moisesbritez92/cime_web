import logging

from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render

from . import content
from .forms import ContactForm

logger = logging.getLogger(__name__)


def home(request):
    """Render the one-page landing and handle the contact form."""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            if not form.is_spam():
                # For now we just log the lead. When the backend grows,
                # persist it to a model and/or send an email/CRM webhook.
                logger.info("Nuevo contacto CIME: %s", form.cleaned_data)
            messages.success(
                request,
                "¡Gracias por contactarnos! Le responderemos a la brevedad.",
            )
            return redirect(f"{request.path}#contacto")
        messages.error(request, "Por favor revise los datos del formulario.")
    else:
        form = ContactForm()

    context = {
        "site_name": settings.SITE_NAME,
        "tagline": settings.SITE_TAGLINE,
        "contact_email": settings.CONTACT_EMAIL,
        "contact_phone": settings.CONTACT_PHONE,
        "contact_whatsapp": settings.CONTACT_WHATSAPP,
        "services": content.SERVICES,
        "reasons": content.REASONS,
        "offices": content.OFFICES,
        "stats": content.STATS,
        "gallery": content.GALLERY,
        "form": form,
    }
    return render(request, "landing/index.html", context)
