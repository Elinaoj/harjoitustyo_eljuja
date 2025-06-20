# Generated by Django 5.2.1 on 2025-06-04 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aika', models.CharField(max_length=5, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Ruoka-ajat',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Artikkeli',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artikkeli', models.CharField(max_length=75)),
                ('hinta', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('lisatietoja', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Artikkelit',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Asunto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nimi', models.CharField(blank=True, max_length=5)),
            ],
            options={
                'verbose_name_plural': 'Asunnot',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Taloyhtio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nimi', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Taloyhtiot',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Myynti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kpl', models.IntegerField(blank=True)),
                ('aika', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artikkelit.aika')),
                ('artikkeli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artikkelit.artikkeli')),
                ('asunto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artikkelit.asunto')),
                ('taloyhtio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artikkelit.taloyhtio')),
            ],
            options={
                'verbose_name_plural': 'Myynnit',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='asunto',
            name='taloyhtio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artikkelit.taloyhtio'),
        ),
    ]
