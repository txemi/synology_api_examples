from typing import Any
from typeguard import typechecked

from synology_api import photos
from printing_common_functions import print_api_call_result, print_api_call_result_yaml, print_separator
from synology_photos_api_utils import create_photos_api


@typechecked
def _print_user_information(photos_api: photos.Photos) -> None:
    """Fetches and prints user information and guest settings."""
    print_separator("Executing: _print_user_information")

    user_info = photos_api.get_userinfo()
    print_api_call_result_yaml("get_userinfo", user_info)

    guest_settings = photos_api.get_guest_settings()
    print_api_call_result_yaml("get_guest_settings", guest_settings)

@typechecked
def _print_folder_information_by_id(photos_api: photos.Photos, folder_id: int | None) -> None:
    if folder_id is None:
        return

    folder_info = photos_api.get_folder(folder_id)
    print_api_call_result_yaml(f"get_folder: Folder information with ID {folder_id}", folder_info)

    items = photos_api.list_item_in_folders(folder_id=folder_id)
    # FIXME: This should return photo objects, DEBUG
    print_api_call_result_yaml(f"list_item_in_folders", items)
    folder_attrs = folder_info.get("data").get("folder")
    if False:
        name = folder_attrs.get("name")
        lf = photos_api.lookup_folder(name)
        # FIXME: The previous line fails
        print_api_call_result_yaml("lookup_folder", lf)

    parent_id = folder_attrs.get("parent")
    if parent_id == folder_id:
        return
    _print_folder_information_by_id(photos_api, parent_id)

@typechecked
def _print_folders_information(photos_api: photos.Photos) -> None:
    """Prints information about folders and items in Synology Photos."""
    print_separator("Executing: _print_folders_information")

    folder_count = photos_api.count_folders()
    print_api_call_result(f"\n--- count_folders: {folder_count}")

    folders = photos_api.list_folders()
    print_api_call_result_yaml("\n--- list_folders ---", folders)

    for folder in folders.get("data", {}).get("list", []):
        folder_id = folder.get("id")
        _print_folder_information_by_id(photos_api, folder_id)

@typechecked
def _print_team_folders_information(photos_api: photos.Photos) -> None:
    """Prints information about team folders and their items."""
    print_separator("Executing: _print_team_folders_information")

    team_folder_count = photos_api.count_team_folders()
    print_api_call_result(f"count_team_folders: {team_folder_count}")

    team_folders = photos_api.list_teams_folders()
    print_api_call_result_yaml("list_teams_folders: Team folders in Synology Photos", team_folders)

    for folder in team_folders.get("data", {}).get("list", []):
        folder_id = folder.get("id")
        if folder_id:
            folder_info = photos_api.lookup_team_folder(str(folder_id))
            print_api_call_result_yaml(
                f"lookup_team_folder: Team folder information with ID {folder_id} ---", folder_info)

@typechecked
def _print_albums_information(photos_api: photos.Photos) -> None:
    """Prints information about available albums."""
    print_separator("Executing: _print_albums_information")
    albums = photos_api.list_albums()
    print_api_call_result_yaml("list_albums: Available albums", albums)

    album_list = albums.get("data").get("list")
    for album in album_list:
        photos_api.get_album(album_id=album)
        # FIXME: Test get_album

@typechecked
def _print_other_data(photos_api: photos.Photos) -> None:
    """Prints information about search filters."""
    print_separator("Executing: _print_other_data")
    search_filters = photos_api.list_search_filters()
    print_api_call_result_yaml("list_search_filters: Available search filters", search_filters)


@typechecked
def print_synology_photos_information() -> None:
    """Executes all tests for the Synology Photos API.
    
            FIXME: Now it returns folders but no photos."""

    photos_api = create_photos_api()

    _print_user_information(photos_api)
    _print_folders_information(photos_api)
    _print_team_folders_information(photos_api)
    _print_albums_information(photos_api)
    _print_other_data(photos_api)

    print("\n--- OK: No errors occurred during execution ---")

if __name__ == "__main__":
    print_synology_photos_information()
