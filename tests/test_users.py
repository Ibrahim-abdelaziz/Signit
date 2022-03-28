"""
users
"""

from profiles.api.v1.schemas import UserSchema


class TestUser:
    """
    Test for users
    """

    def test_get_users(self, db, create_users, users_url, request_client):
        """
        Fetch users
        """
        response = request_client.get(users_url())
        expected_users = UserSchema(many=True).dump(create_users)
        assert response.status_code == 200
        assert response.get_json()["data"] == expected_users
