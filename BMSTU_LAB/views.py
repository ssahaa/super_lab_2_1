from django.shortcuts import render
from datetime import date
from BMSTU_LAB.models import Product
# Create your views here.
orders = [{'title': 'Iphone','id': 1, 'price': '10000', 'img': 'https://appleinsider.ru/wp-content/uploads/2021/09/iPhone_13_i_iPhone_13_mini_00007-750x481.jpg', 'inform': 'Это телефон в случае необхожимости можете его приобрести у нас'},
              {'title': 'Ноутбук','id': 2, 'price': '200000', 'img': 'https://3dnews.ru/assets/external/illustrations/2017/10/05/959519/msi1.jpg',
                'inform': 'Это ноутбук в случае необхожимости можете его приобрести у нас тут еще должны быть его технические характеритиски но их нет'}
              ]
def GetOrders(request):
    return render(request, 'orders.html', {'data': {
        'current_date': date.today(),
        'product': Product.objects.all()
    }})

def To_Order(request):
    return render(request,'Main_page.html')


def GetOrder(request, id):
    return render(request, 'order.html', {'data': {
        'current_date': date.today(),
        'product': Product.objects.filter(id=id)[0]
    }})