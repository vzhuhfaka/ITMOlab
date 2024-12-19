import time, tracemalloc
import unittest
from lab5.task4.src.task4 import min_heap


class TestTask4(unittest.TestCase):

    def test_should_min_heap(self):
        # given
        n = 9
        array = [8, 3, 4, 1, 2, 5, 6, 7, 9]
        exception_result = [(0, 3), (1, 4), (2, 4), (3, 4), (4, 5), (5, 6), (6, 7)]
        limit_time = 2
        limit_memory = 256

        # when
        time_start = time.perf_counter()
        tracemalloc.start()

        result = min_heap(array, n)[0]

        memory_used = tracemalloc.get_traced_memory()
        memory_used_in_mb = memory_used[1] / 2 ** 20

        tracemalloc.stop()
        time_spent = time.perf_counter() - time_start

        # then
        self.assertEqual(result, exception_result)
        self.assertLessEqual(time_spent, limit_time)
        self.assertLessEqual(memory_used_in_mb, limit_memory)

        print(time_spent, memory_used_in_mb)