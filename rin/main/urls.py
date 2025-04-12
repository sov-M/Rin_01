from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("admin", views.admin, name="admin"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("test/", views.test, name="test"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

