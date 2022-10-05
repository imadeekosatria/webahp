from turtle import onclick, update
from venv import create
from django.db import models
# from django.contrib import admin

# Create your models here.
class Kategori(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Ram(models.Model):
    ram = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.ram)

class UkuranLayar(models.Model):
    ukuran = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return str(self.ukuran)

class Brand(models.Model):
    brand = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return str(self.brand)

class Os(models.Model):
    os = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return str(self.os)

class Harga(models.Model):
    harga = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.harga)

class Penggunaan(models.Model):
    penggunaan = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return str(self.penggunaan)

class Baterai(models.Model):
    kapasistas_baterai = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # smartphone_id = models.IntegerField(default=None)

    def __str__(self):
        return str(self.kapasistas_baterai)

class Memory(models.Model):
    memory = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.memory)

class Kamera(models.Model):
    nama_fitur = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return str(self.nama_fitur)

class Smartphone(models.Model):
    name_smartphone = models.CharField(max_length=255)
    ram = models.ForeignKey(Ram, on_delete=models.CASCADE, null=True)
    baterai = models.ForeignKey(Baterai, on_delete=models.CASCADE, null=True)
    ukuran_layar = models.ForeignKey(UkuranLayar, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    os = models.ForeignKey(Os, on_delete=models.CASCADE, null=True)
    kamera = models.ForeignKey(Kamera, on_delete=models.CASCADE, null=True)
    harga = models.ForeignKey(Harga, on_delete=models.CASCADE, null=True)
    penggunaan = models.ManyToManyField(Penggunaan)
    # memory = models.ManyToManyField(Memory)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name_smartphone)    
    