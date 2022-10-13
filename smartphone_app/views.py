from django.http import JsonResponse

def get_products(request):
    """
    Get all products
    args:
        request: the request object
    return:
        JsonResponse: the list of products
    """
    

    return JsonResponse({'products': []})

