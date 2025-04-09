from urllib.parse import urlparse
from synology_api import photos
from synology_config import SYNOLOGY_URL, USERNAME, PASSWORD
from typeguard import typechecked

@typechecked
def create_photos_api() -> photos.Photos:
    """
    Creates and returns an instance of Synology Photos API.
    """
    parsed_url = urlparse(SYNOLOGY_URL)
    host = parsed_url.hostname  # Retrieves only the hostname or IP

    photos_api = photos.Photos(
        ip_address=host,
        port=5000,  # Specify the port (5000 for HTTP, 5001 for HTTPS)
        username=USERNAME,
        password=PASSWORD,
        secure=False,
        cert_verify=False,
        dsm_version=7,
        debug=True  # Enable debug mode
    )
    return photos_api