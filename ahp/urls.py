from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('ram/', views.ram_4gb, name='ram_4gb'),
    path('ram_6gb/', views.ram_6gb, name='ram_6gb'),
    path('ram_8gb/', views.ram_8gb, name='ram_8gb'),
    
    
    path('kategori/', views.kategori_ram, name='kategori_ram'),
    path('kategori_kamera/', views.kategori_kamera, name='kategori_kamera'),
    path('kategori_layar/', views.kategori_layar, name='kategori_layar'),
    path('kategori_harga/', views.kategori_harga, name='kategori_harga'),

    path('baterai/', views.tigaribu, name='tigaribu'),
    path('empatribu/', views.empatribu, name='empatibu'),
    path('limaribu/', views.limaribu, name='limaribu'),

    path('kamera/', views.biasa, name='biasa'),
    path('cukup_lengkap/', views.cukup_lengkap, name='cukup_lengkap'),
    path('sangat_lengkap/', views.sangat_lengkap, name='sangat lengkap'),


    path('harga/', views.duajuta, name='duajuta'),
    path('tigajuta/', views.tigajuta, name='tigajuta'),
    path('empatjuta/', views.empatjuta, name='empatjuta'),
    path('limajuta/', views.limajuta, name='limajuta'),

    path('layar/', views.kecil, name='kecil'),
    path('sedang/', views.sedang, name='sedang'),
    path('besar/', views.besar, name='besar'),

    path('result/', views.result, name='result'),
    

]
