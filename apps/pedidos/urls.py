from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.PedidoCreateView.as_view(), name='pedidos__cria'),
    path('<int:pk>/atualizar/', views.PedidoUpdateView.as_view(), name='pedido__atualiza'),
    path('item/<int:pedido>/', views.ItemCreateView.as_view(), name='pedidos__add__item'),
    path('item/<int:pk>/atualizar', views.ItemUpdateView.as_view(), name='pedidos__atualiza__item'),
    path('item/<int:pk>/excluir', views.ItemDeleteView.as_view(), name='pedidos__excluir__item'),
    path('<int:pk>/excluir/', views.PedidoDeleteView.as_view(), name='pedidos__delete'),
    path('<int:pk>/', views.PedidoDetailView.as_view(), name='pedidos__detail'),
    path('', views.PedidoListView.as_view(), name='pedidos__list'),

]