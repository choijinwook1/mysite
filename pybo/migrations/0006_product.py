# Generated by Django 4.0.3 on 2023-10-11 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pybo', '0005_answer_voter_question_voter_alter_answer_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('pcode', models.CharField(max_length=10)),
                ('pname', models.TextField()),
                ('unitprice', models.IntegerField(default=0)),
                ('discountrate', models.DecimalField(decimal_places=2, default=0, max_digits=11)),
                ('mainfunc', models.CharField(default='', max_length=100)),
                ('imgfile', models.ImageField(blank=True, null=True, upload_to='')),
                ('detailfunc', models.CharField(default='', max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]