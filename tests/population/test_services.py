from unittest import mock

from instance import PopulationService
from tests.interfaces.test_basic import BasicTests


class ShopPopulationServiceTests(BasicTests):
    climate_population_service = mock.Mock()
    sport_population_service = mock.Mock()
    practice_center_population_service = mock.Mock()
    user_population_service = mock.Mock()
    recommendation_population_service = mock.Mock()
    shop_population_service = mock.Mock()
    equipment_population_service = mock.Mock()
    announce_population_service = mock.Mock()

    def setUp(self):
        self.population_service = PopulationService(
            self.climate_population_service,
            self.sport_population_service,
            self.practice_center_population_service,
            self.user_population_service,
            self.recommendation_population_service,
            self.shop_population_service,
            self.equipment_population_service,
            self.announce_population_service)

        self.population_service.db_populate()

    def test_db_populate_adds_climates(self):
        assert self.climate_population_service.db_populate.called

    def test_db_populate_adds_sports(self):
        assert self.sport_population_service.db_populate.called

    def test_db_populate_adds_practice_centers(self):
        assert self.practice_center_population_service.db_populate.called

    def test_db_populate_adds_users(self):
        assert self.user_population_service.db_populate.called

    def test_db_populate_adds_recommendations(self):
        assert self.recommendation_population_service.db_populate.called

    def test_db_populate_adds_shops(self):
        assert self.shop_population_service.db_populate.called

    def test_db_populate_adds_equipments(self):
        assert self.equipment_population_service.db_populate.called

    def test_db_populate_adds_announces(self):
        assert self.announce_population_service.db_populate.called
