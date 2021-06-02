from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("csvimport", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="csvimport",
            name="model_name",
            field=models.CharField(
                default="app_label.model_name",
                help_text="Please specify the app_label.model_name",
                max_length=255,
            ),
        ),
    ]
