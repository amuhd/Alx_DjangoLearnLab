from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission


class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

class BookshelfConfig(AppConfig):
    name = 'bookshelf'

    def ready(self):
        # Get or create the group
        editors_group, created = Group.objects.get_or_create(name='Editors')

        # Assign permissions
        can_create_permission = Permission.objects.get(codename='can_create')
        can_delete_permission = Permission.objects.get(codename='can_delete')

        editors_group.permissions.add(can_create_permission, can_delete_permission)