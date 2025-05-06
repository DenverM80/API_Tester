import json
import logging
import requests
from utils.logger import log

JSON_PLACEHOLDER_URL = "https://jsonplaceholder.typicode.com"


class UserActions:
    """
    This class wraps common user related actions for the {JSON}Placeholder API
    """

    @staticmethod
    def get_users(client: requests.Session) -> requests.Response:
        """
        Send a GET request to list all users.

        Args:
           client (requests.Session): Fixture to provide a persistent session.

        Returns:
            requests.Response: Response to the request.
        """
        log.info("Getting all users...")
        response = client.get(url=f"{JSON_PLACEHOLDER_URL}/users")
        log.debug(f"Received in get_users: {json.dumps(response.json(), indent=2)}")
        log.debug(f"{len(response.json())}")

        if not 200 <= response.status_code < 300:
            log.warning(f"Non success response[{response.status_code}]")

        return response

    @staticmethod
    def get_user_by_id(client: requests.Session, user_id: int) -> requests.Response:
        """
        Send a GET request to get a user's details.

        Args:
           client (requests.Session): Fixture to provide a persistent session.
           user_id (int): ID of user to get details for

        Returns:
            requests.Response: Response to the request.
        """
        log.info(f"Getting user {user_id}...")
        response = client.get(url=f"{JSON_PLACEHOLDER_URL}/users/{user_id}")
        log.debug(f"Received in get_user_by_id: {json.dumps(response.json(), indent=2)}")

        if not 200 <= response.status_code < 300:
            log.warning(f"Non success response[{response.status_code}]")

        return response

    @staticmethod
    def create_user(client: requests.Session, user: dict, verbose: bool=True) -> requests.Response:
        """
        Send a POST request to create a user.

        Args:
           client (requests.Session): Fixture to provide a persistent session.
           user (dict): dict generated from /models/User dataclass
           verbose (bool): optionally suppress noisy debug prints in the log

        Returns:
            requests.Response: Response to the request.
        """
        log.info(f"Creating user: {user['name']}...")
        if not verbose:
            log.setLevel(logging.DEBUG)
        log.debug(f"{json.dumps(user, indent=2)}...")
        response = client.post(url=f"{JSON_PLACEHOLDER_URL}/users", json=user)
        log.debug(f"Received in create_user: {json.dumps(response.json(), indent=2)}")
        if not verbose:
            log.setLevel(logging.INFO)

        if not 200 <= response.status_code < 300:
            log.warning(f"Non success response[{response.status_code}]")

        return response

    @staticmethod
    def update_user(client: requests.Session, user: dict) -> requests.Response:
        """
        Send a PATCH request to update some or all of a user's details.

        Args:
           client (requests.Session): Fixture to provide a persistent session.
           user (dict): dict of /models/User dataclass with properties to update.

        Returns:
            requests.Response: Response to the request.
        """
        log.info(f"Updating user: {user['name']}...")
        log.debug(f"{json.dumps(user, indent=2)}...")
        response = client.patch(url=f"{JSON_PLACEHOLDER_URL}/users/{user['id']}", json=user)
        log.debug(f"Received in update_user: {json.dumps(response.json(), indent=2)}")

        if not 200 <= response.status_code < 300:
            log.warning(f"Non success response[{response.status_code}]")

        return response

    @staticmethod
    def delete_user(client: requests.Session, user_id: int) -> requests.Response:
        """
        Send a DELETE request to delete a user.

        Args:
           client (requests.Session): Fixture to provide a persistent session.
           user_id (int): dict generated from /models/User dataclass

        Returns:
            requests.Response: Response to the request.
        """
        log.info(f"Deleting user: {user_id}...")
        response = client.delete(url=f"{JSON_PLACEHOLDER_URL}/users/{user_id}")
        log.debug(f"Received status {response.status_code} in delete_user: {json.dumps(response.json(), indent=2)}")

        if not 200 <= response.status_code < 300:
            log.warning(f"Non success response[{response.status_code}]")

        return response
