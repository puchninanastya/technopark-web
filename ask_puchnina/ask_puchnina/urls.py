"""ask_puchnina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from ask import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^hello/$', views.hello, name='hello'),
    url(r'^about/$', views.about, name='about'),
    #url(r'^new/(?P<page>\w+)/', views.newQuestions, name='new-questions-page'),
    url(r'^new/$', views.newQuestions, name='new-questions'),
    url(r'^hot/$', views.hotQuestions, name='hot-questions'),
    url(r'^tag/(?P<tagname>\w+)/', views.tagQuestions, name='tag-questions'),
    url(r'^question/(?P<qid>\w+)/', views.question, name='question'),
    url(r'^ask/$', views.ask, name='ask'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.newQuestions, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
