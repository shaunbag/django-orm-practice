from django.test import TestCase, override_settings
from django.test import Client
from http import HTTPStatus

class IPBlacklistMiddlewareTest(TestCase):
    def setUp(self):
        self.client = Client()

    @override_settings(BANNED_IPS=None,MAINTENENCE_MODE=False)
    def test_request_successful_without_ip_list_in_settings(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @override_settings(BANNED_IPS=['192.64.129.2'],MAINTENENCE_MODE=False)
    def test_request_successful_with_ip_addres_not_in_settings(self):
        response = self.client.get('/api/', REMOTE_ADDR='127.0.0.1')
        self.assertEqual(response.status_code, HTTPStatus.OK)


    @override_settings(BANNED_IPS=['192.64.129.2'],MAINTENENCE_MODE=False)
    def test_request_unsuccessful_with_ip_addres_in_settings(self):
        response = self.client.get('/api/', REMOTE_ADDR='192.64.129.2')
        self.assertEqual(response.status_code, HTTPStatus.FORBIDDEN)



class MaintenenceModeTest(TestCase):
    def setUp(self):
        self.client = Client('/')

    @override_settings(MAINTENENCE_MODE=True)
    def test_template_shown_when_maintence_mode_true(self):
        response = self.client.get('/api/')
        self.assertTemplateUsed(response, 'api/maintenence.html')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    @override_settings(MAINTENENCE_MODE=False)
    def test_success_shown_when_maintence_mode_false(self):
        response = self.client.get('/api/')
        self.assertTemplateNotUsed(response, 'api/maintenence.html')
        self.assertEqual(response.status_code, HTTPStatus.OK)