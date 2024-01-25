from django .urls import path
from . import views

urlpatterns = [
    path('', views.ProductMixinViews.as_view()),
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('<int:pk>/update/', views.ProductMixinViews.as_view()), # Reterieve Mode
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view()),
]
