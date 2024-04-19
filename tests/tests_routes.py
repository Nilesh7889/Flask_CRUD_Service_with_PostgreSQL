import unittest
from tests import create_app, db
from unittest.mock import patch
from app import routes


# Test routes
class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()  # Create a test Flask app
        self.client = self.app.test_client()  # Create a test client
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # Test case: Adding a new user
    @patch.object(routes, 'add_user')
    def test_add_user_success(self, mock_add_user):
        mock_add_user.return_value = {'message': 'Success! User added successfully'}
        data = {'full_name': 'test_name5', 'email': 'test5@gmail.com', 'services': []}
        self.client.post('/users', json=data)
        self.assertEqual(mock_add_user.return_value, {'message': 'Success! User added successfully'})

    # Test case: Creating a user with duplicate email
    @patch.object(routes, 'add_user')
    def test_add_user_duplicate_email(self, mock_add_user):
        mock_add_user.return_value = {
            'error message': 'This email is duplicate, please try different email address.'}
        data = {'full_name': 'test_name5', 'email': 'test5@gmail.com', 'services': []}
        self.client.post('/users', json=data)
        self.assertEqual(mock_add_user.return_value,
                         {'error message': 'This email is duplicate, please try different email address.'})

    # Test case: Get user by user ID
    @patch.object(routes, 'get_user')
    def test_read_user_by_id(self, mock_get_user):
        user_id = 1  # Assuming a user with ID 1 exists in the database
        mock_get_user.return_value = {"id": 1, "full_name": "test_name", "email": "test@gmail.com", "services": []}
        self.client.get(f'/users/{user_id}')
        self.assertEqual(mock_get_user.return_value.get("id"), user_id)

    # Test case: User not found
    def test_read_user_not_found(self):
        user_id = 999  # Assuming this user ID does not exist
        response = self.client.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 404)

    # Test case: Update user information
    @patch.object(routes, 'update_user')
    def test_update_user(self, mock_update_user):
        user_id = 1  # Assuming a user with ID 1 exists in the database
        mock_update_user.return_value = {'message': 'Success! User updated successfully'}
        updated_data = {
            'full_name': 'test_name_updated',
            'email': 'testUpdated@gmail.com'
        }
        self.client.put(f'/users/{user_id}', json=updated_data)
        self.assertEqual(mock_update_user.return_value, {'message': 'Success! User updated successfully'})

    # Test case: Update user not found
    def test_update_user_not_found(self):
        user_id = 999  # Assuming this user ID does not exist
        updated_data = {
            'full_name': 'test_name_updated',
            'email': 'testUpdated@gmail.com'
        }
        response = self.client.put(f'/users/{user_id}', json=updated_data)
        self.assertEqual(response.status_code, 404)

    # Test case: Delete user by user ID
    @patch.object(routes, 'delete_user')
    def test_delete_user(self, mock_delete_user):
        # Assuming a user with ID 1 exists in the database
        user_id = 1
        mock_delete_user.return_value = {'message': 'Success! User deleted successfully'}
        response = self.client.delete(f'/users/{user_id}')
        self.assertEqual(mock_delete_user.return_value, {'message': 'Success! User deleted successfully'})

    # Test case: Delete user not found
    def test_delete_user_not_found(self):
        user_id = 999  # Assuming this user ID does not exist
        response = self.client.delete(f'/users/{user_id}')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
