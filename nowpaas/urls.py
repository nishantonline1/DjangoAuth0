from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'products', views.ProductList)
router.register(r'suppliers', views.SupplierList)
router.register(r'orders', views.OrderViewSet)
router.register(r'address', views.AddressViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('whatsapp',views.whatsAppmsg),
    path('test',views.testsqs),
    path('api/public', views.public),
    path('api/private', views.private),
    path('api/private-scoped', views.private_scoped),
]
