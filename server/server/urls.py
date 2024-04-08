from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls', namespace="products")),
    path('cart/', include('cart.urls', namespace="cart")),
    path('account/', include('account.urls', namespace="account")),
    path('profile/', include('profiles.urls', namespace="profiles")),
    path('addres/', include('addreses.urls', namespace="addres")),
    path('order/', include('orders.urls', namespace="orders")),
    path('payment/', include('payment.urls', namespace="payment")),
    path('contact', include('contactus.urls', namespace="contactus")),
    path('', include('home.urls', namespace="home")),
    
    # PWA url
    path('', include('pwa.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
