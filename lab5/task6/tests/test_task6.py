import time, tracemalloc
import unittest
from lab5.task6.src.task6 import main


class TestTask6(unittest.TestCase):

    def test_should_get_queue_minimals(self):
        # given
        commands = ['A 3', 'A 4', 'A 2', 'X', 'D 2 1', 'X', 'X', 'X']
        exception_result = ['2', '1', '3', '*']
        limit_time = 2
        limit_memory = 256

        # when
        time_start = time.perf_counter()
        tracemalloc.start()

        result = main(commands)

        memory_used = tracemalloc.get_traced_memory()
        memory_used_in_mb = memory_used[1] / 2 ** 20

        tracemalloc.stop()
        time_spent = time.perf_counter() - time_start

        # then
        self.assertEqual(result, exception_result)
        self.assertLessEqual(time_spent, limit_time)
        self.assertLessEqual(memory_used_in_mb, limit_memory)

        print(time_spent, memory_used_in_mb)
