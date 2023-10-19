# Generated by Django 4.2.6 on 2023-10-19 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('question_text', models.CharField(max_length=1000)),
                ('answer_text', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]