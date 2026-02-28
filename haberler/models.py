from django.db import models

# Create your models here.
class Haber(models.Model):
    yazar = models.CharField(max_length=100)
    baslik = models.CharField(max_length=200)
    aciklama = models.CharField(max_length=200)
    icerik = models.TextField()
    sehir = models.CharField(max_length=100)
    aktif = models.BooleanField(default=True)
    yayin_tarihi = models.DateTimeField(auto_now_add=True,verbose_name= 'Yayınlanma Tarihi')
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.baslik
    

