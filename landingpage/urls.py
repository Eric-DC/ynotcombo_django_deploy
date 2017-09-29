from django.conf.urls import url
from landingpage.views import HomePageView
#changed to django 1.10 + 
urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
]
