# Generated by Django 4.2.6 on 2023-10-21 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=60)),
                ('opis', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Producent',
                'verbose_name_plural': 'Producenci',
            },
        ),
        migrations.AlterModelOptions(
            name='produkty',
            options={'verbose_name': 'Produkt', 'verbose_name_plural': 'Produkty'},
        ),
    ]
