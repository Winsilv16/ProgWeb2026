from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loja", "0003_rename_nome_categoria_categoria_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="produto",
            name="imagem",
            field=models.ImageField(blank=True, null=True, upload_to="produtos/"),
        ),
        migrations.AlterField(
            model_name="produto",
            name="msgPromocao",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
