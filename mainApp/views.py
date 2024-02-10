from django.shortcuts import render, redirect

from .models import *
from .forms import *


# ------------------------------------------------------------------------------------------------------------------------------------------------
def lavozim(request):
    if request.method == "POST":
        data = LavozimForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect("/lavozim/")
    context = {
        "lavozimlar": Lavozim.objects.all(),
        "form": LavozimForm()
    }
    return render(request, 'lavozim.html', context)


def lavozim_ochir(request, pk):
    Lavozim.objects.get(id=pk).delete()
    return redirect("/lavozim/")


def lavozim_tahrirlash(request, pk):
    if request.method == "POST":
        lavozim = Lavozim.objects.get(id=pk)
        lavozim.maosh = request.POST['maosh']
        lavozim.save()
        return redirect('/lavozim/')
    context = {
        'lavozim': Lavozim.objects.get(id=pk),

    }
    return render(request, 'lavozim_tahrirlash.html', context)

# ------------------------------------------------------------------------------------------------------------------------------------------------
def xodim(request):
    if request.method == "POST":
        data = XodimForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect("/xodim/")
    context = {
        "xodimlar": Xodim.objects.all(),
        "form": XodimForm()
    }
    return render(request, 'xodim.html', context)


def xodim_ochir(request, pk):
    Xodim.objects.get(id=pk).delete()
    return redirect("/xodim/")


def xodim_tahrirlash(request, pk):
    if request.method == "POST":
        xodim = Xodim.objects.get(id=pk)
        xodim.ism = request.POST['ismi']
        xodim.yosh = request.POST['yosh']
        xodim.lavozim = Lavozim.objects.get(id=request.POST.get('l'))
        xodim.ish_vaqti = request.POST['i_vaqt']
        xodim.tel_raqam = request.POST['t_raqam']
        xodim.manzil = request.POST['mazil']
        xodim.save()
        return redirect('/xodim/')
    context = {
        'xodim': Xodim.objects.get(id=pk),
        'lavozimlar': Lavozim.objects.all()
    }
    return render(request, 'xodim_tahrirlash.html', context)


# ------------------------------------------------------------------------------------------------------------------------------------------------
def xona(request):
    if request.method == "POST":
        data = XonaForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect("/xona/")
    context = {
        "xonalar": Xona.objects.all(),
        "form": XonaForm()
    }
    return render(request, 'xona.html', context)


def xona_ochir(request, pk):
    Xona.objects.get(id=pk).delete()
    return redirect("/xona/")

def xona_tahrirlash(request, pk):
    if request.method == "POST":
        xona = Xona.objects.get(id=pk)
        xona.necha_orinli = request.POST['n_orinli']
        xona.bosh = request.POST.get('n_orinli')=='on'
        xona.narx = request.POST['narx']
        xona.save()
        return redirect('/xona/')
    context = {
        'xona': Xona.objects.get(id=pk),

    }
    return render(request, 'xona_tahrirlash.html', context)
# ------------------------------------------------------------------------------------------------------------------------------------------------
def buyurtma(request):
    if request.method == "POST":
        data = BuyurtmaForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect("/records/")
    context = {
        "buyurtmalar": Buyurtma.objects.all(),
        "form": BuyurtmaForm()
    }
    return render(request, 'byurtma.html', context)


def buyurtma_ochir(request, pk):
    Buyurtma.objects.get(id=pk).delete()
    return redirect("/buyurtma/")


def buyurtma_tahrirlash(request, pk):
    if request.method == "POST":
        buyurtma = Buyurtma.objects.get(id=pk)
        buyurtma.xodim = Xodim.objects.get(id=request.POST.get('xodim'))

        buyurtma.mijoz = request.POST['mijoz']
        buyurtma.xona = Xona.objects.get(id=request.POST.get('xona'))
        buyurtma.save()
        return redirect('/buyurtma/')
    context = {
        'buyurtma': Buyurtma.objects.get(id=pk),
        'xodimlar': Xodim.objects.all(),
        'xonalar': Xona.objects.all(),

    }
    return render(request, 'buyurtma_tahrirlash.html', context)
# ------------------------------------------------------------------------------------------------------------------------------------------------
def index(request):
    return render(request, 'index.html')
