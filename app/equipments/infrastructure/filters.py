from app.interfaces.infrastructure.filters import MySQLFilter
from app.equipments.infrastructure.tables import MySQLEquipmentTable as Equipments


class MySQLEquipmentFilter(MySQLFilter):
    def get_col_names(self):
        return [f'E.{Equipments.category_col}',
                f'E.{Equipments.name_col}',
                f'E.{Equipments.description_col}']

    def get_values(self, form=None):
        return [] if form is None else [form.category.data, form.name.data, form.description.data]
