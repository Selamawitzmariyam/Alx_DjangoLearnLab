from django.db import migrations

def create_groups_and_permissions(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    # Define groups
    editors_group, _ = Group.objects.get_or_create(name='Editors')
    viewers_group, _ = Group.objects.get_or_create(name='Viewers')
    admins_group, _ = Group.objects.get_or_create(name='Admins')

    # Define permissions
    can_view = Permission.objects.get(codename='can_view')
    can_create = Permission.objects.get(codename='can_create')
    can_edit = Permission.objects.get(codename='can_edit')
    can_delete = Permission.objects.get(codename='can_delete')

    # Assign permissions to groups
    editors_group.permissions.add(can_view, can_create, can_edit)
    viewers_group.permissions.add(can_view)
    admins_group.permissions.add(can_view, can_create, can_edit, can_delete)

def remove_groups_and_permissions(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name__in=['Editors', 'Viewers', 'Admins']).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('app_name', 'previous_migration_file'),  # Replace with your previous migration file
    ]

    operations = [
        migrations.RunPython(create_groups_and_permissions, remove_groups_and_permissions),
    ]