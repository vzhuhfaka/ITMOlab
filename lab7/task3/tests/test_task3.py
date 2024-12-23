import time, tracemalloc
import unittest
from lab7.task3.src.task3 import distance


class TestTask3(unittest.TestCase):

    def test_should_return_correct_result(self):
        # given
        word_1 = 'short'
        word_2 = 'ports'
        exception_result = 3
        limit_time = 2
        limit_memory = 256

        # when
        time_start = time.perf_counter()
        tracemalloc.start()

        result = distance(word_1, word_2)

        memory_used = tracemalloc.get_traced_memory()
        memory_used_in_mb = memory_used[1] / 2 ** 20

        tracemalloc.stop()
        time_spent = time.perf_counter() - time_start

        # then
        self.assertEqual(result, exception_result)
        self.assertLessEqual(time_spent, limit_time)
        self.assertLessEqual(memory_used_in_mb, limit_memory)

        print(time_spent, memory_used_in_mb)
