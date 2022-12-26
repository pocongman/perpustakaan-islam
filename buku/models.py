from django.db import models

# Create your models here.

class Kategori(models.Model):
    nama = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "Kategori"

class Buku(models.Model):
    judul = models.CharField(max_length=100, blank=True, null=True)
    pengarang = models.CharField(max_length=100)
    penerbit = models.CharField(max_length=100)
    halaman = models.IntegerField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{} - {}".format(self.judul, self.pengarang, self.penerbit, self.halaman)
    
    class Meta: 
        ordering =['-id']
        verbose_name_plural = "Buku"