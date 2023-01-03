from rest_framework.throttling import UserRateThrottle
import random


class MyCustomRandomThrotle(UserRateThrottle):
    def allow_request(self, request, view):
        return random.randint(1, 10) != 1