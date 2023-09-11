from django.shortcuts import get_object_or_404, render
from .models import Product
from category.models import Category

# STORE
def store(request, category_slug=None):

    categories = None
    products = None

    # Aca dice que si el slug del parametro que se creo en la URL es distinto a nada, se guarda en la variable categories, su contenido sera la categoria y el slug con la categoria del url
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)

        # Filtramos los PRODUCTOS con dos parametros : CATEOGIRES (condicion de si existe el slug) y IS_AVAILABLE
        products = Product.objects.filter(
            category=categories, is_available=True)
        
        #Aca contamos el resultado de products
        product_count = products.count() 

    # Si el slug de la URL ES NADA O NONE, se muestra todo
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {'products': products, 'product_count': product_count}
    return render(request, 'store/store.html', context)

# PRODUCT DETAIL
def product_detail(request, category_slug, product_slug):
    try:
        # El category__slug obtiene el valor del campo de una estructura o sea el slug de category de la db
        single_product = Product.objects.get(category__slug = category_slug, slug=product_slug)
    except Exception as e:
        raise e
    
    context = {'single_product':single_product}


    return render(request, 'store/product_detail.html', context)