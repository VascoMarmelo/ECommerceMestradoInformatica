<<<<<<< HEAD
# Generated by Django 4.2 on 2024-04-20 14:07
=======
# Generated by Django 4.2 on 2024-04-20 14:42
>>>>>>> 9a9e65d51987a2891c337a56e87294a0a61c9220

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='app.category'),
        ),
    ]
