import unittest
import task_manager as tm

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        # use a fake list instead of the real JSON file
        self.fake_tasks = []
        tm.load_tasks = lambda: self.fake_tasks
        tm.upload_task = lambda new_task: self.fake_tasks.append(vars(new_task))

    def test_new_id(self):
        self.fake_tasks.extend([{"id": 1}, {"id": 2}])
        self.assertEqual(tm.new_id(), 3)

    def test_create_task_invalid_priority(self):
        result = tm.create_task("Test task", "banana", 3)
        self.assertFalse(result)

    def test_create_task_valid(self):
        tm.create_task("Buy milk", "LOW", 3)
        self.assertEqual(len(self.fake_tasks), 1)
        self.assertEqual(self.fake_tasks[0]["title"], "Buy milk")

if __name__ == "__main__":
    unittest.main()