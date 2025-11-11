from django.urls import path
from . import views  # ดึง views.py มาจากโฟลเดอร์เดียวกัน

urlpatterns = [
    # ถ้า URL เป็น 'ว่างเปล่า' (หน้าแรก) 
    # ให้ไปเรียกฟังก์ชัน 'home_page' จาก views.py
    path('', views.home_page, name='home'),
]