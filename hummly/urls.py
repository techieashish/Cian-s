from django.conf.urls import url
from . import views

app_name = "hummly"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^form$', views.gen_form, name="form"),
    url(r'^add$', views.candi_add, name="candi_add"),
    url(r'^search$', views.candi_search, name="candi_search"),
    url(r'^login$', views.user_login, name="login"),
    url(r'signup', views.user_registration, name="signup"),
    url(r'^register', views.user_registration, name="register"),
    url(r"^logout", views.user_logout, name="logout")
    #url(r'export/(?P<result>\w+)/', views.export_csv, name="export")
]
