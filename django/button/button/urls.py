"""button URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.button1),
    url(r'^output',views.output,name='output'),
    url(r'^spellc', views.spellc,name='spellc'),
    url(r'^transf',views.transf,name='transf'),
    url(r'^transh',views.transh,name='transh'),
    url(r'^transs',views.transs,name='transs'),
    url(r'^transg',views.transg,name='transg'),
    url(r'^summ',views.summ,name='summ'),
    url(r'^upload',views.upload,name='upload'),
    url(r'^textarea',views.textarea,name='textarea'),
    url(r'^textm',views.textm,name='textm'),
    url(r'^button1',views.button1,name='button1'),
    # url(r'^texte', views.texte, name='texte'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
    