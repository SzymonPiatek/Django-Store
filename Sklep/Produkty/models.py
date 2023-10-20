from django.db import models

class Produkty(models.Model):
    # Odpowiednik pola Input Text w HTML
    nazwa = models.CharField(max_length=100)
    # Odpowiednik pola Text Area w HTML
    opis = models.TextField(blank=True)
    
    cena = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nazwa
    