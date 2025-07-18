
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taluka', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Village',
            fields=[
                ('village_id', models.AutoField(primary_key=True, serialize=False)),
                ('village_name', models.CharField(max_length=255)),
                ('taluka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taluka.taluka')),
            ],
            options={
                'db_table': 'tbl_village',
            },
        ),
    ]
