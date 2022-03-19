from rest_framework.routers import SimpleRouter

from megafon_api import views

app_name = 'api'

router = SimpleRouter()
router.register(r'tariffs', views.TariffViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'events', views.EventViewSet)

urlpatterns = router.urls
