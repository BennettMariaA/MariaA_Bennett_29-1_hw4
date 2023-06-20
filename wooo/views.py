from django.shortcuts import render

def product_list(request):
    products = [
        {
            'sunsilk': 'Product 1',
            'description': 'womens shampoo,
            'image': {
                'url': 'https://www.sunsilk.in/content/dam/unilever/sunsilk/india/pack_shot/8901030832420_01-34708277-png.png.ulenscale.460x460.png'
            }
        },
        {
            'dove': 'Product 2',
            'description': 'mens shampoo',
            'image': {
                'url': 'https://m.media-amazon.com/images/I/61M+FAQBrYL.jpg'
            }
        },
        {
            'ligma': 'Product 3',
            'description': 'conditioner',
            'image': {
                'url': 'https://m.media-amazon.com/images/I/61eJ6nDmqTL.jpg'
            }
        }
    ]

    context = {
        'products': products
    }
    return render(request, 'products.html', context)

