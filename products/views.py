from django.shortcuts import render,redirect
from .models import Product,Category
from django.contrib.auth.decorators import login_required
from .forms import ProductForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def profile(request):

    products=Product.objects.filter(user=request.user)
    return render(request,'profile.html',{'products':products})

def product_list(request):
    products = Product.objects.all()
    # return render(request, 'products/product_list.html', {'products': products})
    return render(request, 'products.html',{'products': products})

@login_required
def add_product(request):

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)  
            product.user = request.user      
            product.save()       
            category_id = request.POST.get('category')
            product.category = Category.objects.get(id=category_id)           
            return redirect('product_list')        
    else:
        
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})



@login_required
def delete_product(request,id):

     product=Product.objects.get(id=id,user=request.user)
     product.delete()
     return redirect('profile')  