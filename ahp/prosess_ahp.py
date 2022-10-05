import json

def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.split('/')
        try:
            leading, num = num.split(' ')
            whole = float(leading)
        except ValueError:
            whole = 0
        frac = float(num) / float(denom)
        return whole - frac if whole < 0 else whole + frac

datadict = {}
def save_kategori(param, title):
    datadict[title] = param
    with open('data_dict.json', 'w') as json_file:
        json.dump(datadict, json_file)


total_column = {}
def sum_kategori():
    f = open('data_dict.json')
    datadict = json.load(f)
    f.close()
    for x in datadict:
        total = 0
        for y in datadict:
            total += datadict[y][x]
            print(datadict[y][x])
        total_column[x] = round(total,2)
    # print(total_column)
    with open('total_kategori.json', 'w') as json_file:
        json.dump(total_column, json_file)
    return total_column

eigen = {}
def eigen_kategori():
    
    f = open('data_dict.json')
    data = json.load(f)
    f.close()

    f = open('total_kategori.json')
    data_total = json.load(f)
    f.close()
    for x in data:
        eigen[x] = {}
        for y in data:
            total = data_total[y]
            new = data[x][y] / total
            eigen[x][y] = new 
    with open('eigen_kategori.json', 'w') as json_file:
        json.dump(eigen, json_file)
    sum_avarage_eigen_kategori(eigen)
    return eigen

def sum_avarage_eigen_kategori(eigen):
    sum_average = {}
    for x in eigen:
        sum_average[x] = {}
        total = 0 
        for y in eigen:
            total += eigen[x][y]
            sum_average[x]['total'] = total
        print(total)
        average = total/5
        print(average)
        sum_average[x]['average'] = average
    return sum_average

ramdict = {}
def save_ram(param, title):
    ramdict[title] = param
    with open('ram_dict.json', 'w') as json_file:
        json.dump(ramdict, json_file)

bateraidict = {}
def save_baterai(param, title):
    bateraidict[title] = param
    with open('bateraidict.json', 'w') as json_file:
        json.dump(bateraidict, json_file)


kameradict ={}
def save_kamera(param, title):
    kameradict[title] = param
    with open('kameradict.json', 'w') as json_file:
        json.dump(kameradict, json_file) 

hargadict = {}
def save_harga(param, title):
    hargadict[title] = param
    with open('hargadict.json', 'w') as json_file:
        json.dump(hargadict, json_file)

layardict = {}
def save_layar(param, title):
    layardict[title] = param
    with open('layardict.json', 'w') as json_file:
        json.dump(layardict, json_file)


# Kalkulasi CI
def calculate_ci(panjang):

    if panjang <= 2:
        ci = 0
    elif panjang == 4:
        ci = 0.90
    elif panjang == 5:
        ci = 1.12
    elif panjang == 7:
        ci = 1.32
    else:
        print('tidak masuk CI')


