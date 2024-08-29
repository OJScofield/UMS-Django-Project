from university.exceptions import ResourceException, DatabaseException
from university.models import Department
from university.repositories import DepartmentRepository

class DepartmentComponent:

    def get_all_departments(self):
        return DepartmentRepository.get_all_departments()

    def get_department_by_id(self, department_id):
        try:
            return DepartmentRepository.get_department_by_id(department_id)
        except Department.DoesNotExist:
            raise ResourceException(f"Department with id {department_id} not found.")
        except Exception as e:
            raise DatabaseException(f"Error retrieving department with id {department_id}: {str(e)}")

    def create_department(self, department_data):
        try:
            return DepartmentRepository.create_department(department_data)
        except Exception as e:
            raise DatabaseException(f"Error creating department: {str(e)}")

    def update_department_by_id(self, department_id, data):
        try:
            department = DepartmentRepository.get_department_by_id(department_id)
            DepartmentRepository.update_department(department_id, **data)
        except Department.DoesNotExist:
            raise ResourceException(f"Department with id {department_id} not found.")
        except Exception as e:
            raise DatabaseException(f"Error updating department with id {department_id}: {str(e)}")

    def delete_department_by_id(self, department_id):
        try:
            department = DepartmentRepository.get_department_by_id(department_id)
            DepartmentRepository.delete_department(department)
        except Department.DoesNotExist:
            raise ResourceException(f"Department with id {department_id} not found.")
        except Exception as e:
            raise DatabaseException(f"Error deleting department with id {department_id}: {str(e)}")
        return True
