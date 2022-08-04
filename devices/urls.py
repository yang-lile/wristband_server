from django.urls import path
from . import views

urlpatterns = [
    path('reflesh', view=views.reflesh, name='reflesh'),
    path('heartrate/<str:uid>/',view = views.heartrate, name = 'heartrate'),
    path('blood/<str:uid>/',view = views.blood, name = 'blood'),
    path('oxstart/<str:uid>/',view = views.oxstart, name = 'oxstart'),
    path('state/<str:uid>/',view = views.state, name = 'state'),
    # path('location/<str:uid>/',view = views.location, name = 'location'),
]
