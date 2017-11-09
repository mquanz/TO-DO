import unittest
from functions import *

class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.task_list1 = TaskList()
        self.task_list1.insert_task('Das')
        self.task_list1.insert_task('ist')
        self.task_list1.insert_task('ein')
        self.task_list1.insert_task('Test')

    def tearDown(self):
        pass

    def test_insert_task(self):
        self.assertEqual(self.task_list1.task_list[0].description, 'Das')
        self.assertEqual(self.task_list1.task_list[1].description, 'ist')

    def test_mark_done(self):
        self.task_list1.mark_done(1)
        self.assertTrue(self.task_list1.task_list[0].done)

    def test_delete_task(self):
        self.task_list1.delete_task(1)
        self.task_list1.delete_task(1)
        self.task_list1.delete_task(1)
        self.assertEqual(self.task_list1.task_list[0].description, 'Test')
 
    def test_print_list(self):
        self.assertEqual(self.task_list1.print_list(), ['1 [ ] Das', '2 [ ] ist', '3 [ ] ein', '4 [ ] Test'])

    def test_serialize_deserialize(self):
        self.assertEqual(self.task_list1, self.task_list1.deserialize(self.task_list1.serialize()))


if __name__ == '__main__':
    unittest.main()


