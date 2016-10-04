
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name='static_pages/index.html'),
        name='home'),

    url(r'^admin/', admin.site.urls),
    url(r'^helpdesk/', include('helpdesk.urls')),
]
