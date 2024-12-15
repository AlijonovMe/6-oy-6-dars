from django.db import models


class Brands(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nomi")
    country = models.CharField(max_length=50, verbose_name="Mamlakati")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Brend "
        verbose_name_plural = "Brendlar"


class Cars(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nomi")
    description = models.TextField(default="Ma'lumot qo'shilmadi.", verbose_name="Tavsifi")
    year = models.IntegerField(verbose_name="Yili")
    price = models.IntegerField(verbose_name="Narxi")
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, verbose_name="Brandi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Avtomobil "
        verbose_name_plural = "Avtomobillar"
        ordering = ['-id']
