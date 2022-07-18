from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
  path('products/<int:pk>/', views.productdetail, name='productdetail'),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('register/', views.register, name='register'),

	path('add_product/', views.add_product, name='add_product'),
	path('unauthorized/', views.unauthorized, name="unauthorized")
]
