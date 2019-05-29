import unittest
from app.models import User
from app import db

class UserModelTest(unittest.TestCase):
    '''
    Test class to test behaviours of the User class
    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_user = User(password = '5575')

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password


    def test_password_verify(self):
        self.assertTrue(self.new_user.verify_password('5575'))


if __name__ == '__main__':
    unittest.main()
