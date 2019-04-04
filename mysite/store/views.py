from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from .models import Message
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import MessageForm

def expline(request):
    d = {'title': '説明'}
    return render(request, 'expline.html', d)

def home(request):
    d = {
        'title': 'home',
        'qr': request.build_absolute_uri,
    }
    return render(request, 'home.html', d)

def login(request):
    if request.GET.get('user') !="AnonymousUser":
        d = {
            'title': 'login',
            'user': request.GET.get('user'),
            }
    else:
        d = {'title': 'login'}
    return render(request, 'admin/login.html', d)

def index(request):
    peo=0
    sol=0
    cur=0
    car=0
    cho=0
    peo2=0
    sol2=0
    cur2=0
    car2=0
    cho2=0
    for record in Message.objects.filter(status='取引済').annotate(sum=models.Sum('people')):
        if int(record.serial)<2000:
            peo += record.sum
        else:
            peo2 += record.sum
    for record in Message.objects.filter(status='取引済').annotate(sum=models.Sum('solt_butter')):
        if int(record.serial)<2000:
            sol += record.sum
        else:
            sol2 += record.sum
    for record in Message.objects.filter(status='取引済').annotate(sum=models.Sum('curry')):
        if int(record.serial)<2000:
            cur += record.sum
        else:
            cur2 += record.sum
    for record in Message.objects.filter(status='取引済').annotate(sum=models.Sum('caramel')):
        if int(record.serial)<2000:
            car += record.sum
        else:
            car2 += record.sum
    for record in Message.objects.filter(status='取引済').annotate(sum=models.Sum('chocolate')):
        if record.serial<2000:
            cho += record.sum
        else:
            cho2 += record.sum 
    a = sol + cur + car + cho
    b = sol2 + cur2 + car2 + cho2                                   
    d = {
        'title': 'admin',
        'messages': Message.objects.filter(serial__lt=2000),
        'messages2': Message.objects.filter(serial__gte=2000),
        'peo': peo,
        'sol': sol,
        'cur': cur,
        'car': car,
        'cho': cho,
        'peo2': peo2,
        'sol2': sol2,
        'cur2': cur2,
        'car2': car2,
        'cho2': cho2,
        'peo3': peo+peo2,
        'sol3': sol+sol2,
        'cur3': cur+cur2,
        'car3': car+car2,
        'cho3': cho+cho2,
        'sum': a,
        'sum2': b,
        'sum3': a+b,
        'get': (sol + cur + car + cho) * 100,
        'get2': (sol2 + cur2 + car2 + cho2) * 100,
        'get3':(sol + cur + car + cho + sol2 + cur2 + car2 + cho2) * 100,
    }
    return render(request, 'admin/index.html', d)

def order(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        if int(request.POST.get('solt_butter')) + int(request.POST.get('curry')) + int(request.POST.get('caramel')) + int(request.POST.get('chocolate')) == 0:
            d = {
                'title': '注文',
                'form': form,
                'user': request.GET.get('user'),
                'error': '入力して下さい',
                'serial2': request.GET.get('serial2'),
            }
        else:
            Message.objects.create(**form.cleaned_data)
            h = Message.objects.last()
            h.name = request.GET.get('user')
            h.serial = serial(h.id)
            h.status = '注文'
            h.save()
            d = {
                'serial': h.serial,
                'title': '注文',
                'form': MessageForm(None),
                'user': request.GET.get('user'),
                'serial2': request.GET.get('serial2'),
            }
        return render(request, 'admin/order.html', d)
    else:
        d = {
            'title': '注文',
            'form': form,
            'user': request.GET.get('user'),
            'serial2': request.GET.get('serial2'),
        }
        return render(request, 'admin/order.html', d)

def serial(nam):
    newserial = 1765 + nam
    return newserial

def delete(request):
    delete_ids = request.POST.getlist('delete_ids')
    if delete_ids:
        Message.objects.filter(id__in=delete_ids).delete()
    return redirect('store:index')

def makedelete(request):
    make_ids = request.POST.getlist('make_ids')
    if make_ids:
        Message.objects.filter(id__in=make_ids).update(status = '調理')
    return redirect('store:maker_list')

def maker_list(request):
    sol=0
    cur=0
    car=0
    cho=0
    h = Message.objects.filter(status='注文')
    for record in h.annotate(sum=models.Sum('solt_butter')):
        sol += record.sum
    for record in h.annotate(sum=models.Sum('curry')):
        cur += record.sum
    for record in h.annotate(sum=models.Sum('caramel')):
        car += record.sum
    for record in h.annotate(sum=models.Sum('chocolate')):
        cho += record.sum
    d = {
        'messages': h,
        'title': '調理リスト',
        'sol': sol,
        'cur': cur,
        'car': car,
        'cho': cho,
    }
    return render(request, 'admin/maker_list.html', d)

def maker1(request):
    h = Message.objects.filter(status='オーダー')
    s = h.first()
    if request.method == 'POST':
        if 'button_1' in request.POST:
            s.status = '調理'
            s.save()
            return redirect('store:maker')
    d = {
        'messages': h,
        'first': s,
        'activate': request.GET.get('activate'),
        'title': '調理',
    }
    return render(request, 'admin/maker1.html', d)

def makemore(request):
    if request.method == 'POST':
        if 'button_1' in request.POST:
            h = Message.objects.filter(status='オーダー')
            s = h.first()
            s.status = '調理'
            s.save()

def entrance_list(request):
    h = Message.objects.filter(status='注文')
    d = {
        'messages': h,
        'title': '受付リスト',
    }
    return render(request, 'admin/entrance_list.html', d)

def entrance1(request):
    getserial = request.GET.get('serial')
    s = Message.objects.get(serial=getserial)
    buy = s.solt_butter + s.curry + s.caramel + s.chocolate
    if request.method == 'POST':
        if 'button_1' in request.POST:
            s.status = '取引済'
            s.save()
            return redirect('store:entrance0')
    d = {
        'first': s,
        'buy': buy * 100,
        'buy2': buy,
        'title': '受付',
    }
    return render(request, 'admin/entrance1.html', d)

def entrance0(request):
    if request.POST.get('serial'):
        if search_user(request.POST.get('serial')) != False:
            num = search_user(request.POST.get('serial'))
            if num.status == '調理':
                d = {
                    'serial': request.POST.get('serial'),
                    'title': '受付',
                }
            elif num.status == '注文':
                d = {
                    'serial': request.POST.get('serial'),
                    'title': '受付',
                }
            else:
                d = {
                    'error': '存在しません',
                    'title': '受付',
                }
        else:
            d = {
                'error': '存在しません',
                'title': '受付',
            }
    else:
        d = {'title': '受付'}
    return render(request, 'admin/entrance0.html', d)

def search_user(a):
    try:
        h = Message.objects.get(serial=a)
    except:
        return False
    return h