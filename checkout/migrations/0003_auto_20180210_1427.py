# Generated by Django 2.0.1 on 2018-02-10 17:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0002_auto_20180208_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Aguardando Pagamento'), (1, 'Concluida'), (2, 'Cancelada')], default=0, verbose_name='Situação')),
                ('payment_option', models.CharField(choices=[('pagseguro', 'PagSeguro'), ('paypal', 'Paypal')], default='deposit', max_length=20, verbose_name='Opção de Pagamento')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modicado em')),
                ('user', models.ForeignKey(on_delete='Usuário', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantidade')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('order', models.ForeignKey(on_delete='items', to='checkout.Order', verbose_name='Pedido')),
                ('product', models.ForeignKey(on_delete='Produto', to='catalog.Product')),
            ],
            options={
                'verbose_name': 'Item do pedido',
                'verbose_name_plural': 'Itens dos pedidos',
            },
        ),
        migrations.AlterModelManagers(
            name='cartitem',
            managers=[
            ],
        ),
    ]
