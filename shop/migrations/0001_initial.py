# Generated by Django 4.0.3 on 2022-05-29 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of Category', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of the book', max_length=70)),
                ('description', models.TextField(help_text='The description text')),
                ('description2', models.TextField(help_text='The second description text')),
                ('publication_date', models.DateTimeField(auto_now_add=True, verbose_name='Date the book was published')),
                ('normal_price', models.IntegerField(help_text='Normal price for a book')),
                ('discount_price', models.IntegerField(blank=True, help_text='Discount price for a book', null=True)),
                ('cover', models.ImageField(null=True, upload_to='book_covers/')),
                ('program', models.FileField(null=True, upload_to='book_content/')),
                ('slug', models.SlugField(max_length=40)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
    ]
