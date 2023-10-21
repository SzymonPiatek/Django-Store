# Generated by Django 4.2.6 on 2023-10-21 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0003_produkty_producent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Kategorie',
            },
        ),
        migrations.AddField(
            model_name='produkty',
            name='kategoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Produkty.kategoria'),
        ),
    ]
