from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from .service import SampleService


class SampleAPIViewSet(viewsets.GenericViewSet):
    sample_service = SampleService()

    pass
