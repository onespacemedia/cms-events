import datetime

from .models import Event


def featured_event(page=None):
    """Returns the first upcoming event that is set as featured, if there is
    one. Otherwise it returns the first upcoming event, or None if there are
    no upcoming events."""
    filter_kwargs = {
        "date__gte": datetime.date.today()
    }

    # Allow an optional page to be specified.
    if page:
        filter_kwargs.update({
            "page__page": page,
        })
    try:
        return Event.objects.all().filter(
            featured=True,
            **filter_kwargs
        )[0]
    except IndexError:
        try:
            return Event.objects.all().filter(
                **filter_kwargs
            )[0]
        except IndexError:
            return None
