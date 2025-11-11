# core/views.py

from django.shortcuts import render

def index_page_view(request):
    # Django จะหาไฟล์ 'core/index.html'
    # จากในโฟลเดอร์ 'core/templates/' ที่เราสร้างไว้ในขั้นตอนที่ 1
    return render(request, 'core/index.html')