# coding: utf-8

"""
    Hotel Booking API

    This API represents relation between Hotel and Room entities

    The version of the OpenAPI document: 1.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hotel_booking_sdk.api.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()

    def tearDown(self) -> None:
        pass

    def test_hotels_get(self) -> None:
        """Test case for hotels_get

        Get a list of hotels.
        """
        pass

    def test_hotels_hotel_id_delete(self) -> None:
        """Test case for hotels_hotel_id_delete

        Delete hotel
        """
        pass

    def test_hotels_hotel_id_get(self) -> None:
        """Test case for hotels_hotel_id_get

        Get hotel info
        """
        pass

    def test_hotels_hotel_id_put(self) -> None:
        """Test case for hotels_hotel_id_put

        Update hotel info
        """
        pass

    def test_hotels_hotel_id_rooms_get(self) -> None:
        """Test case for hotels_hotel_id_rooms_get

        List of hotel rooms
        """
        pass

    def test_hotels_hotel_id_rooms_post(self) -> None:
        """Test case for hotels_hotel_id_rooms_post

        Add room to hotel
        """
        pass

    def test_hotels_hotel_id_rooms_room_id_delete(self) -> None:
        """Test case for hotels_hotel_id_rooms_room_id_delete

        Delete room
        """
        pass

    def test_hotels_hotel_id_rooms_room_id_get(self) -> None:
        """Test case for hotels_hotel_id_rooms_room_id_get

        Get room info
        """
        pass

    def test_hotels_hotel_id_rooms_room_id_put(self) -> None:
        """Test case for hotels_hotel_id_rooms_room_id_put

        Update room info
        """
        pass

    def test_hotels_post(self) -> None:
        """Test case for hotels_post

        Add new hotel
        """
        pass


if __name__ == '__main__':
    unittest.main()
