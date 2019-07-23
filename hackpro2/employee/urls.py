from django.contrib import admin
from django.urls import path
from employee import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp', views.emp,name="emp"),
    path('show',views.show,name="show"),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]

urlpatterns += staticfiles_urlpatterns()