from university.models import Role

class RoleRepository:

    @staticmethod
    def get_all_roles():
        return Role.objects.all()

    @staticmethod
    def get_role_by_id(role_id):
        return Role.objects.get(pk=role_id)

    @staticmethod
    def create_role(role_data):
        role = Role(**role_data)
        role.save()
        return role

    @staticmethod
    def update_role(role_id, **kwargs):
        role = Role.objects.get(pk=role_id)
        for key, value in kwargs.items():
            setattr(role, key, value)
        role.save()
        return role

    @staticmethod
    def delete_role(role):
        role.delete()
