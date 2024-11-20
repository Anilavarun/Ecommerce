from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('about',views.about,name='about'),
    path('success',views.success,name='success'),
    path('<slug:c_slug>/<slug:product_slug>',views.proddetails,name='details')
]