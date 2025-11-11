# core/urls.py (สร้างไฟล์นี้)

from django.urls import path
from . import views  # . คือการ import จากโฟลเดอร์เดียวกัน

urlpatterns = [
    # path ว่าง ('') จะถูกจับคู่โดยฟังก์ชัน views.index_page_view
    path('', views.index_page_view, name='index'),
]