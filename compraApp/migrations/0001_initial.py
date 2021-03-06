# Generated by Django 3.2.7 on 2021-11-14 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Credit_card',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('card_name', models.CharField(max_length=20, verbose_name='Card Name')),
                ('card_number', models.IntegerField(default=0)),
                ('card_franchise', models.CharField(max_length=20, verbose_name='Card Franchise')),
                ('bank_name', models.CharField(max_length=40, verbose_name='Bank name')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credit_card', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_date', models.DateTimeField()),
                ('transaction_status', models.CharField(choices=[('A', 'Aprobada'), ('D', 'Denegada'), ('R', 'Reversado'), ('E', 'En proceso')], max_length=20, verbose_name='Status')),
                ('transaction_value', models.FloatField(default=0)),
                ('store_name', models.CharField(max_length=40, verbose_name='Store name')),
                ('id_credit_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction', to='compraApp.credit_card')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('balance', models.IntegerField(default=0)),
                ('lastChangeDate', models.DateTimeField()),
                ('isActive', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
