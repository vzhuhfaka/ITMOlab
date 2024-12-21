import time, tracemalloc
import unittest
from lab6.task5.src.task5 import main


class TestTask5(unittest.TestCase):

    def test_should_return_correct_result(self):
        # given
        data = [['McCain', '10'], ['McCain', '5'], ['Obama', '9'], ['Obama', '8'], ['McCain', '1']]
        exception_result = [['McCain', 16], ['Obama', 17]]
        limit_time = 2
        limit_memory = 64

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
