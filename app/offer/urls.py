from django.conf.urls import url
from .views import * 

urlpatterns = [
    url(r'^offers/$', OfferAPI.as_view(), name='offer_list'),
    url(r'^resumes/$', ResumeAPI.as_view(), name='resume_list'),
    url(r'^token/$', TokenAPI.as_view(), name='token'),
]

app_name = 'offer'
