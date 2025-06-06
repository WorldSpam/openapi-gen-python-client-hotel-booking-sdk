# coding: utf-8

"""
    Hotel Booking API

    This API represents relation between Hotel and Room entities

    The version of the OpenAPI document: 1.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hotel_booking_sdk.models.room_create import RoomCreate

class TestRoomCreate(unittest.TestCase):
    """RoomCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoomCreate:
        """Test RoomCreate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoomCreate`
        """
        model = RoomCreate()
        if include_optional:
            return RoomCreate(
                number = '',
                type = '',
                price = 1.337
            )
        else:
            return RoomCreate(
                number = '',
                type = '',
                price = 1.337,
        )
        """

    def testRoomCreate(self):
        """Test RoomCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
