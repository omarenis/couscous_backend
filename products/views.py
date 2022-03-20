from django.shortcuts import render

from common.views import ViewSet


class ProdictViewSet(ViewSet):

    def __init__(self, fields: dict, serializer_class, service, **kwargs):
        super().__init__(fields, serializer_class, service, **kwargs)
