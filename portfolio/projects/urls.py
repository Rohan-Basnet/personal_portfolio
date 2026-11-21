
from django.urls import path
from . import views
urlpatterns = [
    path("",views.main, name="main" ),
    path("project_one/", views.project_one, name="project_one"),
    path("sql_certification/", views.sql_certification, name="sql_certification")
]