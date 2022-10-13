from django.http import JsonResponse
from .models import Product
def get_products(request):
    """
    Get all products
    args:
        request: the request object
    return:
        JsonResponse: the list of products
    """
    products = Product.objects.all()
    products_json = []
    for product in products:
        products_json.append({
            'id': product.id,
            'name': product.name,
            'company': product.company,
            'color': product.color,
            'RAM': product.RAM,
            'memory': product.memory,
            'price': product.price,
            'created_at': product.created_at,
            'updated_at': product.updated_at,
            'img_url': product.img_url,
            
        })


    return JsonResponse({'products': products_json})

