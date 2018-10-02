from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from core import views 


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^javaq/$', views.javaq, name='javaq'),
    url(r'^javar/$', views.javar, name='javar'),
    url(r'^csq/$', views.csq, name='csq'),
    url(r'^csr/$', views.csr, name='csr'),
    url(r'^cq/$', views.cq, name='cq'),
    url(r'^cr/$', views.cr, name='cr'),
    url(r'^cppq/$', views.cppq, name='cppq'),
    url(r'^cppr/$', views.cppr, name='cppr'),
    url(r'^pythonq/$', views.pythonq, name='pythonq'),
    url(r'^pythonr/$', views.pythonr, name='pythonr'),
    url(r'^mini/$', views.mini, name='mini'), 
    

    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),

    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]
