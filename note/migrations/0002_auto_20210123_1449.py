# Generated by Django 3.1.4 on 2021-01-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='delivery_location',
            field=models.CharField(choices=[('HD', 'Hall D'), ('ELT', 'Edozian lecture THeatre'), ('Coleng', 'College of Engineering'), ('Colenv', 'College of Environmental Science'), ('Colmas', 'College of Mangement Science'), ('Colnas', 'College of Natural Science'), ('Bronze male hostel', 'Bronze male hostel'), ('Bronze female hostel', 'Bronze female hostel'), ('Silver female hostel', 'Silver female hostel'), ('Silver 1 male hostel', 'Silver 1 male hostel'), ('Silver 2 male hostel', 'Silver 2 male hostel'), ('Silver 3 male hostel', 'Silver 3 male hostel'), ('marque', 'Marque'), ('hall b', 'Hall B')], max_length=100),
        ),
    ]
