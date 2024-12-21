import time, tracemalloc
import unittest
from lab6.task1.src.task1 import main


class TestTask1(unittest.TestCase):

    def test_should_find_element_in_set(self):
        # given
        data = [['A', '3'], ['?', '3'], ['D', '3'], ['?', '3']]
        exception_result = ['Y','N']
        limit_time = 2
        limit_memory = 256

        # when
        time_start = time.perf_counter()
        tracemalloc.start()

        result = main(data)

        memory_used = tracemalloc.get_traced_memory()
        memory_used_in_mb = memory_used[1] / 2 ** 20

        tracemalloc.stop()
        time_spent = time.perf_counter() - time_start

        # then
        self.assertEqual(result, exception_result)
        self.assertLessEqual(time_spent, limit_time)
        self.assertLessEqual(memory_used_in_mb, limit_memory)

        print(time_spent, memory_used_in_mb)
