from .views import home_view, detail_view, category_view
from django.urls import path

app_name = 'shop'

urlpatterns = [
    path('', home_view, name='all'),
    path('<name>/', detail_view, name='detail'),
    path('list/<cat>/', category_view, name='list_cat')
]