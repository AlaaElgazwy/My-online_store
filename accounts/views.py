from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.utils import IntegrityError # استيراد خطأ قاعدة البيانات

# Create your views here.

def register_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # 1. التحقق من وجود اسم المستخدم أو البريد الإلكتروني مسبقاً
        if User.objects.filter(username=username).exists():
            messages.error(request, 'هذا المستخدم موجود بالفعل. اختر اسماً آخر.')
            return render(request, 'register.html')
        
        #if User.objects.filter(email=email).exists():
          #  messages.error(request, 'هذا البريد الإلكتروني مسجل بالفعل.')
          #  return render(request, 'register.html')

        try:
            # 2. إنشاء المستخدم وتخزينه في قاعدة البيانات
            # ملاحظة: create_user يقوم بالحفظ تلقائياً، لذا user.save() غير ضرورية.
            user = User.objects.create_user(username=username, email=email, password=password)
            
            # 3. تسجيل الدخول مباشرة بعد التسجيل (اختياري)
            login(request, user)
            
            messages.success(request, 'تم التسجيل بنجاح! نرحب بك.')
            return redirect('profile') # يتم التحويل إلى صفحة ملف المستخدم
            
        except IntegrityError:
            # هذا الخطأ يتم رفعه إذا حدث انتهاك آخر لقيود القاعدة (نادر بعد التحقق أعلاه)
            messages.error(request, 'حدث خطأ في قاعدة البيانات أثناء التسجيل.')
            
        except Exception as e:
            # أي خطأ آخر لم نتوقعه
            messages.error(request, f'حدث خطأ غير متوقع: {e}')
            
    # إذا لم يكن الطلب POST، أو إذا حدث خطأ وتم العرض مرة أخرى
    return render(request, 'register.html') 

def login_view(request):
    
    if request.method=='POST':

        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password) 
        if user is not None:
            login(request,user)
            messages.success(request, f'مرحباً بك مجدداً، {username}')
            return redirect('profile')
        else:
            # يجب أن يكون messages.error داخل الـ else
            messages.error(request,'بيانات تسجيل الدخول غير صحيحة.')
            
    return render(request,'login.html')

def logout_view(request):

    logout(request)
    messages.info(request, 'تم تسجيل الخروج بنجاح.')
    return redirect('login')