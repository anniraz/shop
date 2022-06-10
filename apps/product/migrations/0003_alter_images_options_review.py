# Generated by Django 4.0.4 on 2022-06-06 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('text', models.TextField()),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=5)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_product', to='product.product')),
            ],
        ),
    ]
