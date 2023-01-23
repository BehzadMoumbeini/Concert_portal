# Generated by Django 3.2 on 2023-01-09 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsales', '0002_concertmodel_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profilemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Family', models.CharField(max_length=100)),
                ('Gender', models.IntegerField(choices=[('Man', 'Man'), ('Woman', 'Woman')])),
                ('Profile_image', models.ImageField(upload_to='profile_images/')),
            ],
        ),
        migrations.AddField(
            model_name='concertmodel',
            name='Poster',
            field=models.ImageField(null=True, upload_to='concert_image/'),
        ),
        migrations.CreateModel(
            name='Ticketmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
                ('Ticket_image', models.ImageField(upload_to='ticket_images/')),
                ('Profilemodel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketsales.profilemodel')),
                ('Timemodel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketsales.timemodel')),
            ],
        ),
    ]
