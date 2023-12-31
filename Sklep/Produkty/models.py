from django.db import models

class Producent(models.Model):
    def __str__(self):
        return self.nazwa
    
    nazwa = models.CharField(max_length=60)
    opis = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Producent'
        verbose_name_plural = 'Producenci'

class Kategoria(models.Model):
    def __str__(self):
        return self.nazwa
    
    nazwa = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'
        
class Produkt(models.Model):
    def __str__(self):
        return self.nazwa
    
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE, null=True)
    kategoria = models.ForeignKey(Kategoria, null=True, blank=True, on_delete=models.CASCADE)
    
    # Odpowiednik pola Input Text w HTML
    nazwa = models.CharField(max_length=100)
    # Odpowiednik pola Text Area w HTML
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=12, decimal_places=2)
    zdjecie = models.ImageField(upload_to='media/produkty/', default=None, blank=True, null=True)

    class Meta:
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'