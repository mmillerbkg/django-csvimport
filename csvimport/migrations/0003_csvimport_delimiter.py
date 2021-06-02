from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("csvimport", "0002_csvimport_model_name_default"),
    ]

    operations = [
        migrations.AddField(
            model_name="csvimport",
            name="delimiter",
            field=models.CharField(default=",", max_length=1),
        ),
    ]
