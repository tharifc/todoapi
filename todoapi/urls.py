from django.urls import path
from todoapi import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("todosviewsets", views.TodosViewSetView, basename="TodosViewSets"),
router.register("todosmodelviewsets",views.TodosModelViewSetView,basename="TodosModelViewSets")

urlpatterns = [
                  path("todos", views.TodosView.as_view()),
                  path('todos/<int:todo_id>', views.TodoDetails.as_view()),
                  path("users/accounts/signup", views.UserCreation.as_view()),
                  path("users/accounts/signin", views.SigninView.as_view()),
                  path('todosmixin', views.TodosMixinView.as_view()),
                  path('todo/mixin/<int:todo_id>', views.TodoDetailsMixinView.as_view()),

              ] + router.urls
