import time, tracemalloc
import unittest
from lab7.task1.src.task1 import money_exchange


class TestTask1(unittest.TestCase):

    def test_should_money_exchange(self):
        # given
        money_ = 34
        coins_ = [1, 3, 4]
        exception_result = 9
        limit_time = 1

        # when
        time_start = time.perf_counter()
        tracemalloc.start()

        result = money_exchange(money_, coins_)

        memory_used = tracemalloc.get_traced_memory()
        memory_used_in_mb = memory_used[1] / 2 ** 20

        tracemalloc.stop()
        time_spent = time.perf_counter() - time_start

        # then
        self.assertEqual(result, exception_result)
        self.assertLessEqual(time_spent, limit_time)

        print(time_spent, memory_used_in_mb)
