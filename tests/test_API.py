import unittest

from yandex_api import Yan_disk


class MyTestAPI(unittest.TestCase):

    def setUp(self):
        token = 'AQAAAAAtrpb1AADLW9d3Mv1vH0IphQHB3SiW7_o'
        self.api = Yan_disk(token)

    def test_list_files_on_disk(self):
        self.assertIn(self.api.folder, self.api.list_files_on_disk())

    def test_creating_folder(self):
        self.assertIn(self.api.creating_folder(), [201, 409])

    @unittest.expectedFailure
    def test_2_creating_folder(self):
        self.assertIn(self.api.creating_folder(), [400, 404, 406, 429])


if __name__ == '__main__':
    unittest.main()
