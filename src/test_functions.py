import unittest
from functions import *

class TestFunctions(unittest.TestCase):

    def test_insert_task(self):
        task_list1 = TaskList()
        task_list1.insert_task('Test')
        self.assertEqual(task_list1.task_list[0].description, 'Test')

if __name__ == '__main__':
    unittest.main()


