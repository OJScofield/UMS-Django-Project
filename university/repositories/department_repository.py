from university.models import Department

class DepartmentRepository:

    @staticmethod
    def get_all_departments():
        return Department.objects.all()

    @staticmethod
    def get_department_by_id(department_id):
        return Department.objects.get(pk=department_id)

    @staticmethod
    def create_department(department_data):
        department = Department(**department_data)
        department.save()
        return department

    @staticmethod
    def update_department(department_id, **kwargs):
        department = Department.objects.get(pk=department_id)
        for key, value in kwargs.items():
            setattr(department, key, value)
        department.save()
        return department

    @staticmethod
    def delete_department(department):
        department.delete()
