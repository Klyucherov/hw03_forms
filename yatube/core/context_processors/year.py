from django.utils import dateformat, timezone


def year(request):
    """Добавляет переменную с текущим годом."""
    return {
        'year': dateformat.format(timezone.now(), 'Y'),
    }
