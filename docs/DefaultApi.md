# hotel_booking_sdk.DefaultApi

All URIs are relative to *https://api.example.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hotels_get**](DefaultApi.md#hotels_get) | **GET** /hotels | Get a list of hotels.
[**hotels_hotel_id_delete**](DefaultApi.md#hotels_hotel_id_delete) | **DELETE** /hotels/{hotelId} | Delete hotel
[**hotels_hotel_id_get**](DefaultApi.md#hotels_hotel_id_get) | **GET** /hotels/{hotelId} | Get hotel info
[**hotels_hotel_id_put**](DefaultApi.md#hotels_hotel_id_put) | **PUT** /hotels/{hotelId} | Update hotel info
[**hotels_hotel_id_rooms_get**](DefaultApi.md#hotels_hotel_id_rooms_get) | **GET** /hotels/{hotelId}/rooms | List of hotel rooms
[**hotels_hotel_id_rooms_post**](DefaultApi.md#hotels_hotel_id_rooms_post) | **POST** /hotels/{hotelId}/rooms | Add room to hotel
[**hotels_hotel_id_rooms_room_id_delete**](DefaultApi.md#hotels_hotel_id_rooms_room_id_delete) | **DELETE** /hotels/{hotelId}/rooms/{roomId} | Delete room
[**hotels_hotel_id_rooms_room_id_get**](DefaultApi.md#hotels_hotel_id_rooms_room_id_get) | **GET** /hotels/{hotelId}/rooms/{roomId} | Get room info
[**hotels_hotel_id_rooms_room_id_put**](DefaultApi.md#hotels_hotel_id_rooms_room_id_put) | **PUT** /hotels/{hotelId}/rooms/{roomId} | Update room info
[**hotels_post**](DefaultApi.md#hotels_post) | **POST** /hotels | Add new hotel


# **hotels_get**
> List[Hotel] hotels_get(page=page, size=size)

Get a list of hotels.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import hotel_booking_sdk
from hotel_booking_sdk.models.hotel import Hotel
from hotel_booking_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = hotel_booking_sdk.Configuration(
    host = "https://api.example.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with hotel_booking_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hotel_booking_sdk.DefaultApi(api_client)
    page = 1 # int | Page number (optional) (default to 1)
    size = 10 # int | Page size (optional) (default to 10)

    try:
        # Get a list of hotels.
        api_response = api_instance.hotels_get(page=page, size=size)
        print("The response of DefaultApi->hotels_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->hotels_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **size** | **int**| Page size | [optional] [default to 10]

### Return type

[**List[Hotel]**](Hotel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of hotels |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hotels_hotel_id_delete**
> hotels_hotel_id_delete(hotel_id)

Delete hotel

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import hotel_booking_sdk
from hotel_booking_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = hotel_booking_sdk.Configuration(
    host = "https://api.example.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with hotel_booking_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hotel_booking_sdk.DefaultApi(api_client)
    hotel_id = 'hotel_id_example' # str | Unique hotel id

    try:
        # Delete hotel
        api_instance.hotels_hotel_id_delete(hotel_id)
    except Exception as e:
        print("Exception when calling DefaultApi->hotels_hotel_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hotel_id** | **str**| Unique hotel id | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Hotel deleted |  -  |
**404** | Hotel not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hotels_hotel_id_get**
> Hotel hotels_hotel_id_get(hotel_id)

Get hotel info

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import hotel_booking_sdk
from hotel_booking_sdk.models.hotel import Hotel
from hotel_booking_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = hotel_booking_sdk.Configuration(
    host = "https://api.example.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with hotel_booking_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hotel_booking_sdk.DefaultApi(api_client)
    hotel_id = 'hotel_id_example' # str | Unique hotel id

    try:
        # Get hotel info
        api_response = api_instance.hotels_hotel_id_get(hotel_id)
        print("The response of DefaultApi->hotels_hotel_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->hotels_hotel_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hotel_id** | **str**| Unique hotel id | 

### Return type

[**Hotel**](Hotel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hotel info |  -  |
**404** | Hotel not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hotels_hotel_id_put**
> Hotel hotels_hotel_id_put(hotel_id, hotel_update)

Update hotel info

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import hotel_booking_sdk
from hotel_booking_sdk.models.hotel import Hotel
from hotel_booking_sdk.models.hotel_update import HotelUpdate
from hotel_booking_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = hotel_booking_sdk.Configuration(
    host = "https://api.example.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with hotel_booking_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hotel_booking_sdk.DefaultApi(api_client)
    hotel_id = 'hotel_id_example' # str | Unique hotel id
    hotel_update = hotel_booking_sdk.HotelUpdate() # HotelUpdate | 

    try:
        # Update hotel info
        api_response = api_instance.hotels_hotel_id_put(hotel_id, hotel_update)
        print("The response of DefaultApi->hotels_hotel_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->hotels_hotel_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hotel_id** | **str**| Unique hotel id | 
 **hotel_update** | [**HotelUpdate**](HotelUpdate.md)|  | 

### Return type

[**Hotel**](Hotel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hotel info updated |  -  |
**404** | Hotel not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hotels_hotel_id_rooms_get**
> List[Room] hotels_hotel_id_rooms_get(hotel_id, type=type)

List of hotel rooms

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import hotel_booking_sdk
from hotel_booking_sdk.models.room import Room
from hotel_booking_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = hotel_booking_sdk.Configuration(
    host = "https://api.example.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with hotel_booking_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hotel_booking_sdk.DefaultApi(api_client)
    hotel_id = 'hotel_id_example' # str | Unique hotel id
    type = 'type_example' # str | Filter by room type (optional)

    try:
        # List of hotel rooms
        api_response = api_instance.hotels_hotel_id_rooms_get(hotel_id, type=type)
        print("The response of DefaultApi->hotels_hotel_id_rooms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->hotels_hotel_id_rooms_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hotel_id** | **str**| Unique hotel id | 
 **type** | **str**| Filter by room type | [optional] 

### Return type

[**List[Room]**](Room.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of rooms |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hotels_hotel_id_rooms_post**
> Room hotels_hotel_id_rooms_post(hotel_id, room_create)

Add room to hotel

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import hotel_booking_sdk
from hotel_booking_sdk.models.room import Room
from hotel_booking_sdk.models.room_create import RoomCreate
from hotel_booking_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = hotel_booking_sdk.Configuration(
    host = "https://api.example.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with hotel_booking_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hotel_booking_sdk.DefaultApi(api_client)
    hotel_id = 'hotel_id_example' # str | Unique hotel id
    room_create = hotel_booking_sdk.RoomCreate() # RoomCreate | 

    try:
        # Add room to hotel
        api_response = api_instance.hotels_hotel_id_rooms_post(hotel_id, room_create)
        print("The response of DefaultApi->hotels_hotel_id_rooms_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->hotels_hotel_id_rooms_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hotel_id** | **str**| Unique hotel id | 
 **room_create** | [**RoomCreate**](RoomCreate.md)|  | 

### Return type

[**Room**](Room.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Added room |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hotels_hotel_id_rooms_room_id_delete**
> hotels_hotel_id_rooms_room_id_delete(hotel_id, room_id)

Delete room

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import hotel_booking_sdk
from hotel_booking_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = hotel_booking_sdk.Configuration(
    host = "https://api.example.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with hotel_booking_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hotel_booking_sdk.DefaultApi(api_client)
    hotel_id = 'hotel_id_example' # str | Unique hotel id
    room_id = 'room_id_example' # str | Unique room id inside of a hotel

    try:
        # Delete room
        api_instance.hotels_hotel_id_rooms_room_id_delete(hotel_id, room_id)
    except Exception as e:
        print("Exception when calling DefaultApi->hotels_hotel_id_rooms_room_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hotel_id** | **str**| Unique hotel id | 
 **room_id** | **str**| Unique room id inside of a hotel | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Room deleted |  -  |
**404** | Room not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hotels_hotel_id_rooms_room_id_get**
> Room hotels_hotel_id_rooms_room_id_get(hotel_id, room_id)

Get room info

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import hotel_booking_sdk
from hotel_booking_sdk.models.room import Room
from hotel_booking_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = hotel_booking_sdk.Configuration(
    host = "https://api.example.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with hotel_booking_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hotel_booking_sdk.DefaultApi(api_client)
    hotel_id = 'hotel_id_example' # str | Unique hotel id
    room_id = 'room_id_example' # str | Unique room id inside of a hotel

    try:
        # Get room info
        api_response = api_instance.hotels_hotel_id_rooms_room_id_get(hotel_id, room_id)
        print("The response of DefaultApi->hotels_hotel_id_rooms_room_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->hotels_hotel_id_rooms_room_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hotel_id** | **str**| Unique hotel id | 
 **room_id** | **str**| Unique room id inside of a hotel | 

### Return type

[**Room**](Room.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room info |  -  |
**404** | Room not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hotels_hotel_id_rooms_room_id_put**
> Room hotels_hotel_id_rooms_room_id_put(hotel_id, room_id, room_update)

Update room info

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import hotel_booking_sdk
from hotel_booking_sdk.models.room import Room
from hotel_booking_sdk.models.room_update import RoomUpdate
from hotel_booking_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = hotel_booking_sdk.Configuration(
    host = "https://api.example.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with hotel_booking_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hotel_booking_sdk.DefaultApi(api_client)
    hotel_id = 'hotel_id_example' # str | Unique hotel id
    room_id = 'room_id_example' # str | Unique room id inside of a hotel
    room_update = hotel_booking_sdk.RoomUpdate() # RoomUpdate | 

    try:
        # Update room info
        api_response = api_instance.hotels_hotel_id_rooms_room_id_put(hotel_id, room_id, room_update)
        print("The response of DefaultApi->hotels_hotel_id_rooms_room_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->hotels_hotel_id_rooms_room_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hotel_id** | **str**| Unique hotel id | 
 **room_id** | **str**| Unique room id inside of a hotel | 
 **room_update** | [**RoomUpdate**](RoomUpdate.md)|  | 

### Return type

[**Room**](Room.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Room updated |  -  |
**404** | Room not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hotels_post**
> Hotel hotels_post(hotel_create)

Add new hotel

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import hotel_booking_sdk
from hotel_booking_sdk.models.hotel import Hotel
from hotel_booking_sdk.models.hotel_create import HotelCreate
from hotel_booking_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.example.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = hotel_booking_sdk.Configuration(
    host = "https://api.example.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with hotel_booking_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hotel_booking_sdk.DefaultApi(api_client)
    hotel_create = hotel_booking_sdk.HotelCreate() # HotelCreate | 

    try:
        # Add new hotel
        api_response = api_instance.hotels_post(hotel_create)
        print("The response of DefaultApi->hotels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->hotels_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hotel_create** | [**HotelCreate**](HotelCreate.md)|  | 

### Return type

[**Hotel**](Hotel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Added hotel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

