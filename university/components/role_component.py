from university.exceptions import ResourceException, DatabaseException
from university.models import Role
from university.repositories import RoleRepository

class RoleComponent:

    def get_all_roles(self):
        return RoleRepository.get_all_roles()

    def get_role_by_id(self, role_id):
        try:
            return RoleRepository.get_role_by_id(role_id)
        except Role.DoesNotExist:
            raise ResourceException(f"Role with id {role_id} not found.")
        except Exception as e:
            raise DatabaseException(f"Error retrieving role with id {role_id}: {str(e)}")

    def create_role(self, role_data):
        try:
            return RoleRepository.create_role(role_data)
        except Exception as e:
            raise DatabaseException(f"Error creating role: {str(e)}")

    def update_role_by_id(self, role_id, data):
        try:
            role = RoleRepository.get_role_by_id(role_id)
            RoleRepository.update_role(role_id, **data)
        except Role.DoesNotExist:
            raise ResourceException(f"Role with id {role_id} not found.")
        except Exception as e:
            raise DatabaseException(f"Error updating role with id {role_id}: {str(e)}")

    def delete_role_by_id(self, role_id):
        try:
            role = RoleRepository.get_role_by_id(role_id)
            RoleRepository.delete_role(role)
        except Role.DoesNotExist:
            raise ResourceException(f"Role with id {role_id} not found.")
        except Exception as e:
            raise DatabaseException(f"Error deleting role with id {role_id}: {str(e)}")
        return True
