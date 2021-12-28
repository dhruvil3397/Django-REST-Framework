from rest_framework.throttling import UserRateThrottle

class MyRateThrottle(UserRateThrottle):
    scope = 'My'   # NOTE : register this 'My' inside the settings.py under the 'DEFAULT_THROTTLE_RATES'