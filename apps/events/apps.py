from cms.models import PageBaseSearchAdapter
from django.apps import AppConfig
from watson import search as watson


class EventsConfig(AppConfig):
    name = 'events'

    def ready(self):
        Event = self.get_model('Event')
        watson.register(Event, adapter_cls=PageBaseSearchAdapter)
