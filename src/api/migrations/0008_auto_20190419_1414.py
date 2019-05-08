# Generated by Django 2.1 on 2019-04-19 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resource_inventory', '0009_auto_20190315_1757'),
        ('api', '0007_auto_20190417_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='BridgeConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interfaces', models.ManyToManyField(to='resource_inventory.Interface')),
                ('opnfv_config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resource_inventory.OPNFVConfig')),
            ],
        ),
        migrations.AddField(
            model_name='opnfvapiconfig',
            name='bridge_config',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.BridgeConfig'),
        ),
    ]
