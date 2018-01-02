
from django.conf.urls import include, url
from django.contrib import admin
from app import views
from django.conf.urls.static import static
from django.conf import settings


from app.forms import AuthenticationForm
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^', include('app.urls')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'^accounts/login/$', login, {
        'template_name': 'login.html', 
        'authentication_form': AuthenticationForm
    }, name='login'),
    url(r'^accounts/logout/$', logout, {
        'next_page': '/'
    }, name='logout'),
]

