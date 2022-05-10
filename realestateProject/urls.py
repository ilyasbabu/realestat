from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('sales/<int:district>/<int:type>', views.sales, name='sales'),
    path('saleform/', views.saleform, name='saleform'),
    path('rent/<int:district>/<int:type>', views.rent, name='rent'),
    path('rentform/', views.rentform, name='rentform'),
    path('vehcform/', views.vehcform, name='vehcform'),
    path('vehicle/<int:district>/<int:type>', views.vehicle, name='vehicle'),
    path('detail/property/<int:id>', views.prodetail, name='prodetail'),
    path('detail/vehicle/<int:id>', views.vehdetail, name='vehdetail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
