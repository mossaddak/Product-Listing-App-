from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from .models import (
    Products,
    User
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import(
    AddProduct,
    UpdateProductForm
)
from django.http import HttpResponseRedirect
from userProfileApp.forms import (
    UserProfileUpdateForm,
    ProfilePictureUpdateForm
)

# Create your views here.
def AllProducts(request):
    allProducts = Products.objects.all()
    context = {
        "allProducts":allProducts,
        "TotalProduct":allProducts.count
    }
    return render(request, 'products.html', context)


def ProductDetails(request,pk):
    productDetails = get_object_or_404(Products, pk=pk)
    context = {
        "productDetails":productDetails,
    }
    return render(request, 'product_details.html', context)


@login_required(login_url='siungIn')  
def MyProducts(request):
    MyProducts = request.user.productsRelatedName.all()

    context = {
        "MyProducts":MyProducts,
        "TotalMyProduct":MyProducts.count
    }
    return render(request, "my_products.html", context)

@login_required(login_url='siungIn')
def addProduct(request):
    submitted = False
    if request.method == "POST":
        form = AddProduct(request.POST)
        form = AddProduct(request.POST, request.FILES)

        if form.is_valid():
            form.instance.user = request.user

            if form.instance !='':
                form.save()
                messages.success(request,"Successfully product added.")
                return redirect("addProduct")
        else:
            form = AddProduct()
            if 'submitted' in request.GET:
                submitted = True


    form = AddProduct
    context = {
        "form":form 
    }

    return render(request, "add_product.html", context)


#update product==========================================================

def UpdateProduct(request,pk):
    product = Products.objects.get(pk=pk)
    form = UpdateProductForm(request.POST or None, instance=product)
    
    if request.method == 'POST' and form.is_valid() and product.user==request.user:
        form = UpdateProductForm(request.POST, request.FILES, instance=product)
        form.save()
        print(form.errors)
        messages.success(request,"Successfully product information updated.")
        return redirect("MyProducts")

    context = {
        'product':product,
        "form":form
    }
    
    return render(request, "update_product.html", context)

#delete product==========================================================
@login_required(login_url='siungIn')
def DeleteProduct(request,pk):
    Products.objects.get(pk=pk).delete()
    messages.success(request,"Successfully product deleted.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 


#user's product for admin================================================
@login_required(login_url='siungIn')
def UserProductsForAdmin(request):
    AllUserProducts = Products.objects.all()

    context = {
        "AllUserProducts":AllUserProducts,
        "TotalUserProduct":AllUserProducts.count,
    }
    return render(request, 'all_user_product_for_admin.html', context)

@login_required(login_url='siungIn')
def AllUsers(request):
    #from django.contrib.auth.models import User
    AllUsers = User.objects.filter(is_superuser=False)
    context = {
        "AllUsers":AllUsers
    }

    return render(request, 'all_sellers.html', context)


#user profile================================================
@login_required(login_url='siungIn')  
def UserProfile(request, pk):
    UserDetails = get_object_or_404(User, pk=pk)


    #profile info ====================
    form = UserProfileUpdateForm(instance=UserDetails)
    if request.method == "POST":
        if request.user.pk != UserDetails.pk:
            redirect("/")
        form = UserProfileUpdateForm(request.POST, instance=UserDetails)  

        if form.is_valid():
            form.save()
            messages.success(request, "Profile has been updated.")
            
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
        else:
            #messages.warning(request, form.errors)
            print(form.errors)


    #profile picture ====================


    context = {
        "UserDetails":UserDetails,
        "form":form,
    }

    return render(request, 'user_profile.html', context)

@login_required(login_url='siungIn')
def ProfilePictureChngeForAdmin(request, pk):
    UserDetails = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = ProfilePictureUpdateForm(request.POST, request.FILES)
        if form.is_valid():

            image = request.FILES['profile_image']
            user = get_object_or_404(User, pk=UserDetails.pk)
            

            # if request.user.is_superuser :
            #     return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 

            user.profile_image = image
            user.save()
            messages.success(request,"Profile picture update success!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





@login_required(login_url='siungIn')
def SpecificUsersProductForAdmin(request,pk):
    user = get_object_or_404(User, pk=pk)
    SpecificUserProductsForAdmin = user.productsRelatedName.all()
    context = {
        "SpecificUserProductsForAdmin":SpecificUserProductsForAdmin
    }
    return render(request, 'specific_user_product_for_admin.html', context)
