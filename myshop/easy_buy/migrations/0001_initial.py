# Generated by Django 4.0.4 on 2022-05-19 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=70)),
                ('subject', models.CharField(default='', max_length=70)),
                ('message', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=60)),
                ('category', models.CharField(default='', max_length=200)),
                ('subcategory', models.CharField(default='', max_length=200)),
                ('mrp', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(default='', upload_to='easy_buy/images')),
                ('banner_image', models.ImageField(default='NULL', upload_to='easy_buy/banners')),
                ('is_home', models.IntegerField(default=0)),
                ('is_trandy', models.IntegerField(default=0)),
                ('is_arrived', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('catstatus', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=1000)),
                ('brand', models.CharField(default='', max_length=100)),
                ('discounted', models.CharField(default='', max_length=10)),
                ('model', models.CharField(default='', max_length=100)),
                ('pub_date', models.DateField(verbose_name='2022-05-16')),
            ],
        ),
    ]