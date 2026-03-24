from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from http import HTTPStatus

import logging

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        logger.info("Request Recieved")

        if settings.MAINTENENCE_MODE:
            template = "api/maintenence.html"
            return render(request, template, status=HTTPStatus.NOT_FOUND)

        response = self.get_response(request)

        return response
        