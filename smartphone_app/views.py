from django.http import JsonResponse
from django.shortcuts import render
from .models import Product

# Define the function convert_to_json

def convert_to_json(product):
    """
    Convert a product to a JSON object
    args:
        product: a product object
    returns:
        a JSON object
    """
    product_json = {
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
    }
    return product_json

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
        products_json.append(convert_to_json(product))
    companes = Product.objects.all()
    set_company = set([company.company for company in companes])
    product_dict = {'data':products_json, 'company':set_company}

    return render(request, 'color.html', context=product_dict)

def get_product(request, id):
    """
    Get a product
    args:
        request: the request object
        id: the id of the product
    return:
        JsonResponse: the product
    """
    if request.method == 'GET':

        product = Product.objects.get(id=id)

        # Check if the product exists using the id
        product_json = convert_to_json(product)
        companes = Product.objects.all()
        set_company = set([company.company for company in companes])
        product_dict = {'data':product_json, 'company':set_company}

    return render(request, 'color.html', context=product_dict)

def add_product(request):
    """
    Create a product
    args:
        request: the request object
    return:
        JsonResponse: the product
    """
    if request.method == 'POST':
        product = Product.objects.create(
            name=request.POST['name'],
            company=request.POST['company'],
            color=request.POST['color'],
            RAM=request.POST['RAM'],
            memory=request.POST['memory'],
            price=request.POST['price'],
            img_url=request.POST['img_url'],
        )
        product_json = convert_to_json(product)
        product.save()  # save the product to the database

        return JsonResponse({'product': product_json})

    return JsonResponse({'product': {}})

def update_product(request, id):
    """
    Update a product
    args:
        request: the request object
        id: the id of the product
    return:
        JsonResponse: the product
    """
    if request.method == 'POST':
        product = Product.objects.get(id=id)
        # product.name = request.POST['name']
        # product.company = request.POST['company']
        # product.color = request.POST['color']
        # product.RAM = request.POST['RAM']
        # product.memory = request.POST['memory']
        product.price = request.POST['price']
        # product.img_url = request.POST['img_url']
        product.save()
    return JsonResponse({'product': {}})

def delete_product(request, id):
    """
    Delete a product
    args:
        request: the request object
        id: the id of the product
    return:
        JsonResponse: the product
    """
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        product.delete()
    return JsonResponse({'product': {}})

def get_products_by_company(request, company):
    """
    Get all products by company
    args:
        request: the request object
        company: the company of the product
    return:
        JsonResponse: the list of products
    """
    if request.method == 'GET':
        products = Product.objects.filter(company=company)
        products_json = []
        for product in products:
            products_json.append(convert_to_json(product))
        companes = Product.objects.all()
        set_company = set([company.company for company in companes])
        product_dict = {'data':products_json, 'company':set_company}

    return render(request, 'color.html', context=product_dict)

def get_products_by_memory_range(request, memory):
    """
    Get all products by memory range
    args:
        request: the request object
        min_memory: the min memory of the product
        max_memory: the max memory of the product
    """
    if request.method == 'GET':
        products = Product.objects.filter(memory__gte=memory)
        products_json = []
        for product in products:
                products_json.append(convert_to_json(product))
        companes = Product.objects.all()
        set_company = set([company.company for company in companes])
        product_dict = {'data':product_json, 'company':set_company}

    return render(request, 'color.html', context=product_dict)

def get_products_by_RAM(request, RAM):
    """
    Get all products by RAM
    args:
        request: the request object
        RAM: the RAM of the product
    """
    if request.method == 'GET':
        products = Product.objects.filter(RAM__gte=RAM)
        product_json = []
        for product in products:
            product_json.append(convert_to_json(product))
        companes = Product.objects.all()
        set_company = set([company.company for company in companes])
        product_dict = {'data':product_json, 'company':set_company}

    return render(request, 'color.html', context=product_dict)

def get_products_by_color(request, color):
    """
    Get all products by color
    args:
        request: the request object
        color: the color of the product
    return:
        JsonResponse: the list of products
    """
    if request.method == 'GET':
        product = Product.objects.filter(color__contains = color)
        product_json = []
        for i in product:
            product_json.append(convert_to_json(i))
        companes = Product.objects.all()
        set_company = set([company.company for company in companes])
        product_dict = {'data':product_json, 'company':set_company}

    return render(request, 'color.html', context=product_dict)

def get_products_by_memory(request, memory):
    """
    Get all products by memory
    args:
        request: the request object
        memory: the memory of the product
    return:
        JsonResponse: the list of products
    """
    if request.method == 'GET':
        product = Product.objects.filter(memory__gte = memory)
        product_json = []
        for i in product:
            product_json.append(convert_to_json(i))
        companes = Product.objects.all()
        set_company = set([company.company for company in companes])
        product_dict = {'data':product_json, 'company':set_company}

    return render(request, 'color.html', context=product_dict)

def get_products_by_price(request, price):
    """
    Get all products by price
    args:
        request: the request object
        price: the price of the product
    return:
        JsonResponse: the list of products
    """
    if request.method == 'GET':
        product = Product.objects.filter(price__lte = price)
        product_json = []
        for i in product:
            product_json.append(convert_to_json(i))
        companes = Product.objects.all()
        set_company = set([company.company for company in companes])
        product_dict = {'data':product_json, 'company':set_company}

    return render(request, 'color.html', context=product_dict)

def get_products_by_price_range(request, min_price, max_price):
    """
    Get all products by price range
    args:
        request: the request object
        min_price: the min price of the product
        max_price: the max price of the product
    return:
        JsonResponse: the list of products
    """
    if request.method == 'GET':
        product_min = Product.objects.filter(price__gte = min_price)
        product_max = product_min.filter(price__lte = max_price)
        product_json = []
        for i in product_max:
            product_json.append(convert_to_json(i))
        companes = Product.objects.all()
        set_company = set([company.company for company in companes])
        product_dict = {'data':product_json, 'company':set_company}

    return render(request, 'color.html', context=product_dict)

def get_products_by_RAM_and_memory(request, RAM, memory):
    """
    Get all products by RAM and memory
    args:
        request: the request object
        RAM: the RAM of the product
        memory: the memory of the product
    return:
        JsonResponse: the list of products
    """
    if request.method == 'GET':
        product_RAM = Product.objects.filter(RAM__gte = RAM)
        product_memory = product_RAM.filter(memory__gte = memory)
        product_json = []
        for i in product_memory:
            product_json.append(convert_to_json(i))
        companes = Product.objects.all()
        set_company = set([company.company for company in companes])
        product_dict = {'data':product_json, 'company':set_company}

    return render(request, 'color.html', context=product_dict)

def get_products_by_RAM_range(request, min_RAM, max_RAM):
    """
    Get all products by RAM range
    args:
        request: the request object
        min_RAM: the min RAM of the product
        max_RAM: the max RAM of the product
    return:
        JsonResponse: the list of products
    """
    if request.method == 'GET':
        product_minRAM = Product.objects.filter(RAM__gte = min_RAM)
        product_maxRAM = product_minRAM.filter(RAM__lte = max_RAM)
        product_json = []
        for i in product_maxRAM:
            product_json.append(convert_to_json(i))
        companes = Product.objects.all()
        set_company = set([company.company for company in companes])
        product_dict = {'data':product_json, 'company':set_company}

    return render(request, 'color.html', context=product_dict)

def get_products_by_memory_range(request, min_memory, max_memory):
    """
    Get all products by memory range
    args:
        request: the request object
        min_memory: the min memory of the product
        max_memory: the max memory of the product
    return:
        JsonResponse: the list of products
    """
    if request.method == 'GET':
        product_min_memory = Product.objects.filter(memory__gte = min_memory)
        product_max_memory = product_min_memory.filter(memory__lte = max_memory)
        product_json = []
        for i in product_max_memory:
            product_json.append(convert_to_json(i))
        companes = Product.objects.all()
        set_company = set([company.company for company in companes])
        product_dict = {'data':product_json, 'company':set_company}

    return render(request, 'color.html', context=product_dict)