from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home_page(request):
    # คุณสามารถดึงข้อมูลจาก Database หรือทำอะไรก็ได้ตรงนี้
    # เราจะสร้างตัวแปร 'message' เพื่อส่งไปให้ Template

    context = {
        'message': 'นี่คือข้อความที่ส่งมาจาก View!'
    }

    # นี่คือคำสั่ง "เรนเดอร์"
    # Django จะไปหา 'index.html' แล้วเอา 'context' ไปเติม
    return render(request, 'index.html', context)