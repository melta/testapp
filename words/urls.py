from django.conf.urls import url
from words.views import index


app_name = "words"
urlpatterns = [
    url(r"^$", index, name="index")
]
