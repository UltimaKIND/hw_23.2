from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ContactsPageView, ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

# урлы приложения catalog
urlpatterns = [
    path('create', ProductCreateView.as_view(), name='create'),
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
]
