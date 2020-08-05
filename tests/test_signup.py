import json

from tests.BaseCase import BaseCase

class TestUserSignup(BaseCase):

    def test_successful_signup(self):
        # Given
        payload = json.dumps({
            "email": "x@gmail.com",
            "password": "mycoolpassword"
        })

        # When
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)
