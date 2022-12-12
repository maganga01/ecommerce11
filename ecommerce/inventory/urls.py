from django.urls import path
from ecommerce.inventory import views

urlpatterns = [
    path('get_post', views.ListCreateCategoryAPIView.as_view(), name='get_post_category'),
    path('<int:pk>/', views.RetrieveUpdateDestroyCategoryAPIView.as_view(), name='get_delete_update_category'),
     path('get_post', views.ListCreateProductAPIView.as_view(), name='get_post_product'),
    path('<int:pk>/', views.RetrieveUpdateDestroyProductAPIView.as_view(), name='get_delete_update_product'),
]