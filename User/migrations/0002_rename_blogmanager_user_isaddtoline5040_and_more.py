# Generated by Django 4.0 on 2023-10-07 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='BlogManager',
            new_name='isAddToLine5040',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='OrderingManager',
            new_name='isAddToLineHamkadeh',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='ProductManager',
            new_name='isMonitoring5040',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='HowSee',
        ),
        migrations.RemoveField(
            model_name='user',
            name='HowSeePerson',
        ),
        migrations.RemoveField(
            model_name='user',
            name='JobPosition',
        ),
        migrations.RemoveField(
            model_name='user',
            name='NameFather',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Presenter',
        ),
        migrations.RemoveField(
            model_name='user',
            name='codeMeli',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phoneNumber2',
        ),
        migrations.AddField(
            model_name='user',
            name='isMonitoringHamkadeh',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
