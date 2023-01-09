from django.urls import path
from .views import AllDataView, CertainDataView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('', AllDataView.as_view()),
    path('get/<int:pk>', CertainDataView.as_view()),
    path('create/', CreateView.as_view()),
    path('update/<int:pk>', UpdateView.as_view()),
    path('delete/<int:pk>', DeleteView.as_view()),

]