from django.urls import path
from .views import StudentAdd,StudentGet,StudentGetOne,StudentPatch,StudentUpdate,StudentDelete

urlpatterns = [
    path("add/",StudentAdd.as_view(),name="Add"),
    path("get/",StudentGet.as_view(),name="Get"),
    path("getone/<int:id>/",StudentGetOne.as_view(),name="getone"),
    path("patch/<int:id>/",StudentPatch.as_view(),name="patch"),
    path("update/<int:id>/",StudentUpdate.as_view(),name="update"),
    path("delete/<int:id>/",StudentDelete.as_view(),name="delete")

]
