from django.urls import path
from withcrop.views import image_upload_view

app_name = "withcrop"

urlpatterns = [
    path('img/', image_upload_view, name="img_uploader"),
]
