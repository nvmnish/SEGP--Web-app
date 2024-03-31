from django.shortcuts import render


# Create your views here.
def admin_page(request):
    return render(request, 'segppt1/admin_page.html')

def options_page(request):
    return render(request, 'segppt1/options_page.html')



def add_new_image_options(request):
    return render(request, 'segppt1/add_new_image_options.html')

def delete_image_options(request):
    return render(request, 'segppt1/delete_image_options.html')

def update_image_options(request):
    return render(request, 'segppt1/update_image_options.html')

def search_image_options(request):
    return render(request, 'segppt1/search_image_options.html')




def add_WSI(request):
    return render(request, 'segppt1/add_WSI.html')

def add_IHC(request):
    return render(request, 'segppt1/add_IHC.html')

def add_tumor_mask(request):
    return render(request, 'segppt1/add_tumor_mask.html')

def add_HandE(request):
    return render(request, 'segppt1/add_HandE.html')



def delete_WSI(request):
    return render(request, 'segppt1/delete_WSI.html')

def delete_IHC(request):
    return render(request, 'segppt1/delete_IHC.html')