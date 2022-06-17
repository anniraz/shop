from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
from apps.product.forms import ReviewForm

# from django.views import generic

from apps.product.models import *


# class LoginUser(LoginView):
#     form_class=AuthenticationForm
#     template_name='productTemplates/login.html'
#     def get_success_url(self):
#         return reverse_lazy('homepage')

    # success_url=reverse_lazy('homepage')

# class RegisterUser(generic.CreateView):
#     form_class=RegisterUserForm
#     template_name='productTemplates/register_user.html'
#     success_url=reverse_lazy('homepage')

    # def form_valid(self,form):
    #     user=form.save()
    #     login(self.request,user)
    #     return redirect('homepage')

# def logout_user(request):
#     logout(request)
#     return redirect('login')
    



def products(request):

    if 'search_button' in request.GET:
        word = request.GET.get('search_word')
        product = Product.objects.filter(Q(title__icontains=word))
        return render(request, 'productTemplates/products.html', {'product': product})
    else:
        product=Product.objects.all()
        context={'product':product}
        return render(request, 'productTemplates/products.html',context)




def homepageview(request):
    if 'search_button' in request.GET:
        word = request.GET.get('search_word')
        product = Product.objects.filter(Q(title__icontains=word))
        return render(request, 'productTemplates/products.html', {'product': product})
    else:
      
        categories = Category.objects.all()
        products=Product.objects.all()[:3]
        products_all=Product.objects.all()[:1]
        product=Product.objects.all()
        context={
            'categories': categories,
            'products':products,
            'products_all':products_all,
            'product':product
            }

        return render(request, 'index.html', context)

def product_detail(request,id):
    product=Product.objects.get(id=id)
    img=Images.objects.filter(product=id)
    review=Review.objects.filter(product=id)
    # product=get_object_or_404(Product, url=slug )

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        

        if form.is_valid():
            # print(form.cleaned_data)
                form.save()
                form.changed_datachanged_data

    else:
        form = ReviewForm()


    context={
        'product':product,
        'img':img,
        'review':review,
        'form':form
    }   
    return render(request,'productTemplates/product-page.html',context)


# class   ReviewForm(generic.CreateView):
#     form_class=ReviewAdmin
#     template_name='productTemplates/product-page.html'



def reviewForm(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            # print(form.cleaned_data)
                form.save()

    else:
        form = ReviewForm()

    return render(request, 'productTemplates/product-page.html', {'form':form})



def categoryDetail(request,id):

    products_all=Product.objects.filter(id=id)[:1]
    product=Product.objects.filter(id=id)
    context={
        'products_all':products_all,
        'product':product
        }

    return render(request, 'productTemplates/category_detail.html', context)



