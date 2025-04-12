from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.products_home, name="products_home"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.ProductsDetailView.as_view(), name="products-detail"),
    path("<int:pk>/update/", views.ProductsUpdateView.as_view(), name="products-update"),
    path("<int:pk>/delete/", views.ProductsDeleteView.as_view(), name="products-delete"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
