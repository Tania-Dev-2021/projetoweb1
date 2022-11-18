# Generated by Django 4.1.2 on 2022-11-10 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dclientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomec', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=50)),
                ('endereco', models.TextField()),
                ('tipo', models.CharField(choices=[('F', 'Pessoa Física'), ('J', 'Pessoa Jurídica')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Dprodutos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomep', models.CharField(max_length=20)),
                ('valor_produto', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Dpedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_pedido', models.IntegerField()),
                ('data_pedido', models.DateField()),
                ('valor_pedido', models.FloatField()),
                ('status', models.CharField(choices=[('PP', 'PEDIDO EM PROCESSO'), ('PR', 'PEDIDO REALIZADO'), ('PE', 'PEDIDO ENTREGUE')], max_length=2)),
                ('quantidade_pedido', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastrar.dclientes')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastrar.dprodutos')),
            ],
        ),
    ]
