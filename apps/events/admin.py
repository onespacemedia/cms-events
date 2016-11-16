from cms.admin import PageBaseAdmin
from django.contrib import admin

from .models import Event, Events


@admin.register(Event)
class EventAdmin(PageBaseAdmin):
    fieldsets = [
        (None, {
            'fields': ['title', 'slug', 'page'],
        }),
        ('Sidebar', {
            'fields': ['sidebar']
        }),
        ('Date', {
            'fields': [('start_date', 'end_date')]
        }),
        ('Content', {
            'fields': ['key_info', 'image', 'description'],
        })
    ]

    fieldsets.extend(PageBaseAdmin.fieldsets)
    fieldsets.remove(PageBaseAdmin.TITLE_FIELDS)

    def get_form(self, request, obj=None, **kwargs):
        form = super(EventAdmin, self).get_form(request, obj, **kwargs)
        try:
            form.base_fields['page'].initial = Events.objects.all()[0]
        except IndexError:
            pass
        return form
