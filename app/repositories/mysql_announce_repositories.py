import datetime

from injector import inject

from app.announces.models import Announce
from app.announces.repositories import AnnouncesRepository
from app.database import Database
from app.repositories.mysql_announce_queries import MySQLAnnouncesQuery as Query
from app.repositories.mysql_tables import MySQLAnnouncesTable as Announces


class MySQLAnnouncesRepository(AnnouncesRepository):
    @inject
    def __init__(self, database: Database):
        self.database = database

    def get_all_for_shop(self, shop_id):
        query = Query().get_all_for_shop(shop_id)
        return self.get_all(query)

    def get_all_for_equipment(self, equipment_id):
        query = Query().get_all_for_equipment(equipment_id)
        return self.get_all(query)

    def get_all(self, query):
        announces = []

        try:
            with self.database.connect().cursor() as cur:
                cur.execute(query)

                for announce_cur in cur.fetchall():
                    announces.append(self.build_announce(announce_cur))
        finally:
            cur.close()

        return announces

    @staticmethod
    def build_announce(cur):
        return Announce(cur[Announces.id_col],
                        cur[Announces.shop_id_col],
                        cur[Query.fake_shop_name_col],
                        cur[Announces.equipment_id_col],
                        cur[Query.fake_equipment_name_col],
                        cur[Announces.state_col],
                        cur[Announces.price_col],
                        cur[Announces.date_col])

    def add(self, announce):
        announce.date = datetime.datetime.now()
        query = Query().add()

        try:
            with self.database.connect().cursor() as cur:
                cur.execute(query, (announce.shop_id, announce.equipment_id, announce.state,
                                    announce.price, announce.date))

                self.database.connect().commit()

                announce.id = cur.lastrowid
        finally:
            cur.close()

        return cur.lastrowid
