# Generated by Django 4.2.1 on 2023-05-16 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_cour_salle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salle_Cour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_cour', models.DateField()),
                ('cour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.cour')),
                ('salle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.salle')),
            ],
        ),
        migrations.CreateModel(
            name='Presence_Cour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_presence', models.DateField()),
                ('cour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.cour')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.etudiant')),
            ],
        ),
    ]
