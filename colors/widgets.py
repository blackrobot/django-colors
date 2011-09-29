# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

class ColorPickerException(Exception):
    pass

class ColorPickerWidget(forms.TextInput):
    class Media:
        css = {
            'all': (
                '%scss/colorpicker.css' % settings.COLORS_STATIC_URL,
            )
        }
        js = (
            '%sjs/colorpicker.js' % settings.COLORS_STATIC_URL,
        )

    def __init__(self, language=None, attrs=None):
        self.static_url = getattr(settings, 'COLORS_STATIC_URL', None)
        if not self.static_url:
            raise ColorPickerException('You must define COLOR_STATIC_URL in your settings.py')
        self.language = language or settings.LANGUAGE_CODE[:2]
        super(ColorPickerWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        rendered = super(ColorPickerWidget, self).render(name, value, attrs)
        return "%s%s" % (rendered, mark_safe(render_to_string('colors/widget.html', {
            'value': value, 'name': name,
        })))
