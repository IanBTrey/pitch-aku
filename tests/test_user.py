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
