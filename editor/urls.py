# text_editor_app/urls.py

from django.urls import path
from .views import *
from django.http import request,HttpResponseRedirect


urlpatterns = [
    path('<int:pk>/', document_detail, name='document_detail'),
    path('document_detail_json/<int:pk>/', document_detail_json, name='document_detail_json'),
    path('new/', document_new, name='document_new'),
    path('<int:pk>/edit/', document_edit, name='document_edit'),
    path('<int:pk>/delete/', document_delete, name='document_delete'),
    path('<int:document_id>/download/', download_document, name='download_document'),

    # Authentication URLs
    path('logout/',log_out, name="logout" ),
]
