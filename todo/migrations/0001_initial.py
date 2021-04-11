# Generated by Django 3.0.5 on 2021-04-08 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('created_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Intermediate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secondary_id', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('totalTime', models.FloatField()),
                ('timeSpent', models.FloatField()),
                ('goalId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Goal')),
            ],
        ),
    ]