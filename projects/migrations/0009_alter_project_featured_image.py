# Generated by Django 3.2.8 on 2021-11-01 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_alter_project_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='Z:\\djangoo\\Udemy1\\devsearch\\static\\images\\m.jpg', null=True, upload_to=''),
        ),
    ]
