from django.shortcuts import render, redirect
from .models import *
from .prosess_ahp import *
# Create your views here.
def index(request):
    ponsel = Smartphone.objects.all()

    content = {'ponsel': ponsel}

    return render(request, 'index.html', content)

# Kategori

def kategori_ram(request):
    kategori = Kategori.objects.all()[1:]
    current_kategori = Kategori.objects.get(name='ram')
    if request.method == 'POST':
        data = {
                'ram' : 1,            
                'kamera' : round(convert_to_float(request.POST.get('kamera')),2),
                'harga' : round(convert_to_float(request.POST.get('harga')),2),
                'layar' : round(convert_to_float(request.POST.get('layar')),2),
                'baterai' : round(convert_to_float(request.POST.get('baterai')),2),
            
        }
        save_kategori(data, 'ram')
        return redirect('kategori_kamera')
    content = {'title': 'Kategori', 'kategori': kategori, 'current_kategori': current_kategori}

    return render(request, 'kategori.html', content)


def kategori_kamera(request):
    kategori = Kategori.objects.all()[2:]
    current_kategori = Kategori.objects.get(name='kamera')
    data_sebelum = convert_to_float(datadict['ram']['kamera'])

    if data_sebelum >= 1:
        ram = round(1 / data_sebelum, 1)
    else:
        ram = round(1 / data_sebelum)
    


    if request.method == 'POST':
        data = {

                'ram' : ram,
                'kamera' : 1,
                'harga' : round(convert_to_float(request.POST.get('harga')), 2),
                'layar' : round(convert_to_float(request.POST.get('layar')), 2),
                'baterai' : round(convert_to_float(request.POST.get('baterai')), 2),
            
        }
        save_kategori(data, 'kamera')
        return redirect('kategori_harga')

    content = {'title': 'Kategori', 'kategori': kategori, 'current_kategori': current_kategori}

    return render(request, 'kategori.html', content)

def kategori_layar(request):
    kategori = Kategori.objects.all()[4:]
    current_kategori = Kategori.objects.get(name='layar')

    data_ram = convert_to_float(datadict['ram']['layar'])
    if data_ram >= 1:
        ram = round(1/data_ram, 1)
    else:
        ram = round(1/data_ram)

    data_kamera = convert_to_float(datadict['kamera']['layar'])
    if data_kamera >= 1:
        kamera = round(1/data_kamera, 1)    
    else:
        kamera = round(1/data_kamera)
    
    data_harga = convert_to_float(datadict['harga']['layar'])
    if data_kamera >= 1:
        harga = round(1/data_harga, 1)    
    else:
        harga = round(1/data_harga)

    if request.method == 'POST':
        data = {
            'ram' : ram,
            'kamera' : kamera,
            'harga' : harga,
            'layar' : 1,
            'baterai' : round(convert_to_float(request.POST.get('baterai')), 2),
        }

        save_kategori(data, 'layar')
        kategori_baterai()
        return redirect('index')
    content = {'title': 'Kategori', 'kategori': kategori, 'current_kategori': current_kategori}

    return render(request, 'kategori.html', content)


def kategori_harga(request):
    kategori = Kategori.objects.all()[3:]
    current_kategori = Kategori.objects.get(name='harga')

    data_ram = convert_to_float(datadict['ram']['harga'])
    if data_ram >= 1:
        ram = round(1/data_ram, 1)
    else: 
        ram = round(1/data_ram)

    data_kamera = convert_to_float(datadict['kamera']['harga'])
    if data_kamera >= 1:
        kamera = round(1/data_kamera, 1)
    else:
        kamera = round(1/data_kamera)

    if request.method == 'POST':
        data = {
            'ram' : ram,
            'kamera' : kamera,
            'harga' : 1,
            'layar' : round(convert_to_float(request.POST.get('layar')), 2),
            'baterai' : round(convert_to_float(request.POST.get('baterai')), 2),
        }

        save_kategori(data, 'harga')
        return redirect('kategori_layar')


    content = {'title': 'Kategori', 'kategori': kategori, 'current_kategori': current_kategori}

    return render(request, 'kategori.html', content)

def kategori_baterai():
    data = {}
    for da in datadict:
        value = datadict[da]['baterai']
        if value >= 1:
            data[da] = round(1/value, 1)
        else:
            data[da] = round(1/value)
    data['baterai'] = 1
    save_kategori(data, 'baterai')


# Ram 

def ram_4gb(request):
    list_ram = Ram.objects.all()[1:]
    current_ram = Ram.objects.all().get(ram= '4 Gb')
    
    if request.method == 'POST':
        
        data = {
            '4gb': 1,
            '6gb': round(convert_to_float(request.POST.get('6 Gb')), 2),
            '8gb': round(convert_to_float(request.POST.get('8 Gb')), 2),
            '12gb': round(convert_to_float(request.POST.get('12 Gb')), 2)
        }
        save_ram(data, '4gb')
        return redirect('ram_6gb')
    content = {'title': 'pilih ram', 'ram': list_ram, 'current_ram': current_ram}
    return render(request, 'ram.html', content)

def ram_6gb(request):
    list_ram = Ram.objects.all()[2:]
    current_ram = Ram.objects.all().get(ram='6 Gb')

    data_sebelum = convert_to_float(ramdict['4gb']['6gb'])
    if data_sebelum >= 1:
        fourgig = round(1 / data_sebelum, 1)
    else:
        fourgig = round(1 / data_sebelum)


    if request.method == 'POST':
        data = {
            '4gb' : fourgig,
            '6gb' : 1,
            '8gb' : round(convert_to_float(request.POST.get('8 Gb')), 2),
            '12gb' : round(convert_to_float(request.POST.get('12 Gb')), 2)
        }
        save_ram(data, '6gb')
        return redirect('ram_8gb')

    content = {'title': 'pilih ram', 'ram': list_ram, 'current_ram': current_ram}
    return render(request, 'ram.html', content)

def ram_8gb(request):
    list_ram = Ram.objects.all()[3:]
    current_ram = Ram.objects.all().get(ram='8 Gb')

    data_4gb = convert_to_float(ramdict['4gb']['8gb'])
    if data_4gb >= 1:
        fourgig = round(1 / data_4gb, 1)
    else:
        fourgig = round(1 / data_4gb)

    data_6gb = convert_to_float(ramdict['6gb']['8gb'])
    if data_6gb >= 1:
        sixgig = round(1 / data_6gb, 1)
    else:
        sixgig = round(1 / data_6gb)

    if request.method == 'POST':
        data = {
            '4gb' : fourgig,
            '6gb' : sixgig,
            '8gb' : 1,
            '12gb' : round(convert_to_float(request.POST.get('12 Gb')), 2)
        }
        save_ram(data, '8gb')
        ram_12gb()
        return redirect('index')

    content = {'title': 'pilih ram', 'ram': list_ram, 'current_ram': current_ram}
    return render(request, 'ram.html', content)

def ram_12gb():
    data = {}
    for da in ramdict:
        value = ramdict[da]['12gb']
        if value >= 1:
            data[da] = round(1/value, 1)
        else:
            data[da] = round(1/value)
    data['12gb'] = 1
    save_ram(data, '12gb')

# Baterai
def tigaribu(request):
    list_baterai = Baterai.objects.all()[1:]
    current_baterai = Baterai.objects.all().get(kapasistas_baterai = 'kurang dari 3000 mAh')

    if request.method == 'POST':
        data = {
            'tiga': 1,
            'empat': round(convert_to_float(request.POST.get('kurang dari 4000 mAh')), 2),
            'lima': round(convert_to_float(request.POST.get('4000 - 5000 mAh')), 2)
        }

        save_baterai(data, 'tiga')
        return redirect('empatribu')
    content = {'title': 'Baterai', 'baterai': list_baterai, 'current_baterai': current_baterai}
    return render(request, 'baterai.html', content)

def empatribu(request):
    list_baterai = Baterai.objects.all()[2:]
    current_baterai = Baterai.objects.all().get(kapasistas_baterai = 'kurang dari 4000 mAh')

    data_tiga = convert_to_float(ramdict['tiga']['empat'])
    if data_tiga >= 1:
        tiga = round(1 / data_tiga, 1)
    else:
        tiga = round(1 / data_tiga)

    if request.method == 'POST':
        data = {
            'tiga': tiga,
            'empat': 1,
            'lima': round(convert_to_float(request.POST.get('4000 - 5000 mAh')), 2),
        }

        save_baterai(data, 'empat')
        limaribu()
        return redirect('index')
    content = {'title': 'Baterai', 'baterai': list_baterai, 'current_baterai': current_baterai}
    return render(request, 'baterai.html', content)

def limaribu():
    data = {}
    for da in bateraidict:
        value = bateraidict[da]['lima']
        if value >= 1:
            data[da] = round(1/value, 1)
        else:
            data[da] = round(1/value)
    data['lima'] = 1
    save_baterai(data, 'lima')

# Kamera

def biasa(request):
    list_kamera = Kamera.objects.all()[1:]
    current_kamera = Kamera.objects.all().get(nama_fitur= 'biasa')

    if request.method == 'POST':
        data = {
            'biasa': 1,
            'cukup lengkap': round(convert_to_float(request.POST.get('cukup lengkap')), 2),
            'sangat lengkap': round(convert_to_float(request.POST.get('sangat lengkap')), 2)
        }

        save_kamera(data, 'biasa')        
        return redirect('cukup_lengkap')
    content = {'title': 'Fitur Kamera', 'kamera': list_kamera, 'current_kamera': current_kamera}
    return render(request, 'kamera.html', content)

def cukup_lengkap(request):
    list_kamera = Kamera.objects.all()[2:]
    current_kamera = Kamera.objects.all().get(nama_fitur='cukup lengkap')

    data_sebelum = convert_to_float(kameradict['biasa']['cukup lengkap'])
    if data_sebelum >= 1:
        mp = round(1 / data_sebelum, 1)
    else: 
        mp = round(1 / data_sebelum)
    
    if request.method == 'POST':
        data = {
            'biasa': mp,
            'cukup lengkap': 1,
            'sangat lengkap': round(convert_to_float(request.POST.get('sangat lengkap')), 2)
        }

        save_kamera(data, 'cukup lengkap')        
        sangat_lengkap()
        return redirect('index')

    content = {'title': 'Fitur Kamera', 'kamera': list_kamera, 'current_kamera': current_kamera}
    return render(request, 'kamera.html', content)

def sangat_lengkap():
    data = {}
    for da in kameradict:
        value = kameradict[da]['sangat lengkap']
        if value >= 1:
            data[da] = round(1/value, 1)
        else:
            data[da] = round(1/value)
    data['sangat lengkap'] = 1
    save_kamera(data, 'sangat lengkap')

# Harga

def duajuta(request):
    list_harga = Harga.objects.all()[1:]
    current_harga = Harga.objects.all().get(harga= '< Rp 2.000.000')

    if request.method == 'POST':
        data = {
            '2 juta': 1,
            '3 juta': round(convert_to_float(request.POST.get('< Rp 3.000.000')), 2),
            '4 juta': round(convert_to_float(request.POST.get('< Rp 4.000.000')), 2),
            '5 juta': round(convert_to_float(request.POST.get('< Rp 5.000.000')), 2),
            '6 juta': round(convert_to_float(request.POST.get('>= Rp 5.000.000')), 2)
        }

        save_harga(data, '2 juta')        
        return redirect('tigajuta')
    content = {'title': 'Harga', 'harga': list_harga, 'current_harga': current_harga}
    return render(request, 'harga.html', content)

def tigajuta(request):
    list_harga = Harga.objects.all()[2:]
    current_harga = Harga.objects.all().get(harga= '< Rp 3.000.000')

    data_duajuta = convert_to_float(hargadict['2 juta']['3 juta'])
    if data_duajuta >= 1:
        duajuta = round(1 / data_duajuta, 1)
    else: 
        duajuta = round(1 / data_duajuta)

    if request.method == 'POST':
        data = {
            '2 juta': duajuta,
            '3 juta': 1,
            '4 juta': round(convert_to_float(request.POST.get('< Rp 4.000.000')), 2),
            '5 juta': round(convert_to_float(request.POST.get('< Rp 5.000.000')), 2),
            '6 juta': round(convert_to_float(request.POST.get('>= Rp 5.000.000')), 2)
        }

        save_harga(data, '3 juta')        
        return redirect('empatjuta')
    content = {'title': 'Harga', 'harga': list_harga, 'current_harga': current_harga}
    return render(request, 'harga.html', content)

def empatjuta(request):
    list_harga = Harga.objects.all()[3:]
    current_harga = Harga.objects.all().get(harga= '< Rp 4.000.000')

    data_duajuta = convert_to_float(hargadict['2 juta']['4 juta'])
    if data_duajuta >= 1:
        duajuta = round(1 / data_duajuta, 1)
    else: 
        duajuta = round(1 / data_duajuta)

    data_tigajuta = convert_to_float(hargadict['3 juta']['4 juta'])
    if data_tigajuta >= 1:
        tigajuta = round(1 / data_tigajuta, 1)
    else: 
        tigajuta = round(1 / data_tigajuta)

    if request.method == 'POST':
        data = {
            '2 juta': duajuta,
            '3 juta': tigajuta,
            '4 juta': 1,
            '5 juta': round(convert_to_float(request.POST.get('< Rp 5.000.000')), 2),
            '6 juta': round(convert_to_float(request.POST.get('>= Rp 5.000.000')), 2)
        }

        save_harga(data, '4 juta')        
        return redirect('limajuta')
    content = {'title': 'Harga', 'harga': list_harga, 'current_harga': current_harga}
    return render(request, 'harga.html', content)

def limajuta(request):
    list_harga = Harga.objects.all()[4:]
    current_harga = Harga.objects.all().get(harga= '< Rp 5.000.000')

    data_duajuta = convert_to_float(hargadict['2 juta']['5 juta'])
    if data_duajuta >= 1:
        duajuta = round(1 / data_duajuta, 1)
    else: 
        duajuta = round(1 / data_duajuta)

    data_tigajuta = convert_to_float(hargadict['3 juta']['5 juta'])
    if data_tigajuta >= 1:
        tigajuta = round(1 / data_tigajuta, 1)
    else: 
        tigajuta = round(1 / data_tigajuta)
    
    data_empatjuta = convert_to_float(hargadict['4 juta']['5 juta'])
    if data_empatjuta >= 1:
        empatjuta = round(1 / data_empatjuta, 1)
    else: 
        empatjuta = round(1 / data_empatjuta)

    if request.method == 'POST':
        data = {
            '2 juta': duajuta,
            '3 juta': tigajuta,
            '4 juta': empatjuta,
            '5 juta': 1,
            '6 juta': round(convert_to_float(request.POST.get('>= Rp 5.000.000')), 2)
        }

        save_harga(data, '5 juta')   
        enamjuta()     
        return redirect('index')
    content = {'title': 'Harga', 'harga': list_harga, 'current_harga': current_harga}
    return render(request, 'harga.html', content)

def enamjuta():
    data = {}
    for da in hargadict:
        value = hargadict[da]['6 juta']
        if value >= 1:
            data[da] = round(1/value, 1)
        else:
            data[da] = round(1/value)
    data['6 juta'] = 1
    save_harga(data, '6 juta')

# Ukuran Layar

def kecil(request):
    list_layar = UkuranLayar.objects.all()[1:]
    current_layar = UkuranLayar.objects.all().get(ukuran='Kecil')

    if request.method == 'POST':
        data = {
            'kecil': 1,
            'sedang': round(convert_to_float(request.POST.get('Sedang')), 2),
            'besar': round(convert_to_float(request.POST.get('Besar')), 2)
        }

        save_layar(data, 'kecil')        
        return redirect('sedang')
    content = {'title': 'Ukuran Layar', 'layar': list_layar, 'current_layar': current_layar}
    return render(request, 'ukuranlayar.html', content)


def sedang(request):
    list_layar = UkuranLayar.objects.all()[2:]
    current_layar = UkuranLayar.objects.all().get(ukuran='Sedang')

    data_rendah = convert_to_float(layardict['kecil']['sedang'])
    if data_rendah >= 1:
        rendah = round(1 / data_rendah, 1)
    else: 
        rendah = round(1 / data_rendah)
    

    if request.method == 'POST':
        data = {
            'kecil': rendah,
            'sedang': 1,
            'besar': round(convert_to_float(request.POST.get('Besar')), 2)
        }

        save_layar(data, 'sedang')   
        besar()     
        return redirect('index')
    content = {'title': 'Ukuran Layar', 'layar': list_layar, 'current_layar': current_layar}
    return render(request, 'ukuranlayar.html', content)

def besar():
    data = {}
    for da in layardict:
        value = layardict[da]['besar']
        if value >= 1:
            data[da] = round(1/value, 1)
        else:
            data[da] = round(1/value)
    data['besar'] = 1
    save_layar(data, 'besar')

def result(request):
    kategori = sum_kategori()
    eigen = eigen_kategori()
    sum_average =sum_avarage_eigen_kategori(eigen)
    content = {'title': 'Hasil', 'kategori': kategori, 'eigen': eigen, 'sum_average': sum_average}
    return render(request, 'result.html', content)