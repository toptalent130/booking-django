from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    # url(r'^$', 'home'),
    # api
    url(r'^api/v1/units/$', views.ListingView.as_view()),
    url(r'^api/v1/units/(?P<pk>[0-9]+)$', views.ListingDetail.as_view())
]
# router.register(r'accounts', AccountViewSet)