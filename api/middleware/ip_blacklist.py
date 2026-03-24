from django.conf import settings
from django.core.exceptions import PermissionDenied
from ..models import BannedIp

class IpBlackListMiddlware:

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        """
            check whether the incoming request is from remote address that is in the banned ip list,
            there are two implementations here, one using BANNED_IPS setting in the settings.py file
            and the second referencing the model of banned ips for a list stored in the db
        """

        # Check agains the settings file
        if hasattr(settings, 'BANNED_IPS') and settings.BANNED_IPS is not None:
            # check incoming request ip against banned ips
            if request.META['REMOTE_ADDR'] in settings.BANNED_IPS:
                raise PermissionDenied()
        

        # check against the db
        if BannedIp.objects.filter(ip_address=request.META["REMOTE_ADDR"]).exists():
            raise PermissionDenied()

        response = self.get_response(request)

        return response