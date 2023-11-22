# Generated by Django 4.1 on 2023-11-15 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0005_questionbypreference_questionbypreferenceoption'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='question_by_preference',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='voting', to='voting.questionbypreference'),
        ),
        migrations.AlterField(
            model_name='voting',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='voting', to='voting.question'),
        ),
    ]
