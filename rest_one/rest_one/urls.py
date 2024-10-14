from django.contrib import admin
from django.urls import path

from rest_app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("create-program", create_program),
    path("get-programs", get_programs),
    path("create-student", create_update_student),
    path("get-students", get_student),
    path("get-student-by-id/<int:id>",get_student_by_id),
    path("get-student-by-program/<int:id>", get_student_by_program),


    path("delete-program/<int:id>", delete_program)


]
