from django.urls import path

from webapp.views import  result

urlpatterns = [
    path('', result),
    path('/story/', result),
]