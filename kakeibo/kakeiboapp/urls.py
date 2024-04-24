from django.urls import path,include

from . import views

urlpatterns = [
    path('list/',views.RecordListView.as_view(),name='list'),
    path('detail/<int:pk>/',views.RecordDetailView.as_view(),name='detail'),
    path('create/',views.RecordCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.RecordUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.RecordDeleteView.as_view(),name='delete'),
]