from rest_framework import serializers
import re


class URLValidator:
    """
    Валидация для сохранения уроков и курсов, проверка на отсутствие в материалах ссылок на сторонние ресурсы
    """
    def __init__(self, fields):
        self.fields = fields

    def __call__(self, fields, *args, **kwargs):
        url = 'youtube.com'
        val_url = dict(fields).get(self.fields)
        if val_url:
            if url not in val_url:
                raise serializers.ValidationError("Нельзя использовать ссылки на сторонние "
                                                  "образовательные платформы или личные сайты.")


