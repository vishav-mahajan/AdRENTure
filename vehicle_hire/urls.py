"""vehicle_hire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from front_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^logout/',views.logout ),
    url(r'^', include('front_app.urls')),
    url(r'^superuser/', include('adminapp.urls',namespace="superuser")),
    url(r'^manager/', include('managerapp.urls')),
    url(r'^businessuser/', include('businessuserapp.urls')),
    url(r'^changepassword/',views.updatepassword),
    url(r'^profileupdate/',views.profile),
    url(r'^feepolicy/',views.feepolicy),
    url(r'^eligibilty/',views.eligibilty),
    url(r'^dskjgheriugiurefhkusdjdowieuqhiurehf/',views.verify),
    url(r'^paypal/',include('paypal.standard.ipn.urls')),
    url(r'^confirmation',views.confirmation_messages),
    url(r'^payment_done/',views.payment_done, name='payment_done'),
    url(r'^payment_cancelled/', TemplateView.as_view(template_name='payment_canceled'), name='payment_canceled')

    #url(r'^fpassword/',views.fpassword)

]\
              +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 