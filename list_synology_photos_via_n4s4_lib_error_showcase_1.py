from list_synology_photos_via_N4S4_lib import create_photos_api
from printing_common_functions import print_api_call_result, print_api_call_result_yaml


def list_photos_and_fail_showcase_example():
    """ FIXME: This method returns synology_api.exceptions.PhotosError:

            synology_api/auth.py", line 452, in request_data
            raise PhotosError(error_code=error_code)
            synology_api.exceptions.PhotosError"""
    
    photos_api = create_photos_api()
    print_api_call_result("Testing list_item_in_folders with basic parameters")
    items = photos_api.list_item_in_folders(offset=0, limit=10)
    print_api_call_result_yaml("Response from list_item_in_folders:", items)


if __name__ == "__main__":
    list_photos_and_fail_showcase_example()
