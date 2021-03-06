# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from .common import CommonCarrierCase


class TestDeliveryCarrier(CommonCarrierCase):
    def setUp(self):
        super(CommonCarrierCase, self).setUp()
        self.carrier_service = self.service.component("delivery_carrier")

    def test_search_all(self):
        res = self.carrier_service.search()
        expected = {
            "count": 2,
            "rows": [
                {
                    "price": 0.0,
                    "description": self.free_carrier.name or None,
                    "id": self.free_carrier.id,
                    "name": self.free_carrier.name,
                    "type": None,
                },
                {
                    "price": 0.0,
                    "description": self.poste_carrier.name or None,
                    "id": self.poste_carrier.id,
                    "name": self.poste_carrier.name,
                    "type": None,
                },
            ],
        }
        self.assertDictEqual(res, expected)

    def test_search_current_cart(self):
        res = self.carrier_service.search(target="current_cart")
        expected = {
            "count": 2,
            "rows": [
                {
                    "price": 0.0,
                    "description": self.free_carrier.name or None,
                    "id": self.free_carrier.id,
                    "name": self.free_carrier.name,
                    "type": None,
                },
                {
                    "price": 20.0,
                    "description": self.poste_carrier.name or None,
                    "id": self.poste_carrier.id,
                    "name": self.poste_carrier.name,
                    "type": None,
                },
            ],
        }
        self.assertDictEqual(res, expected)
