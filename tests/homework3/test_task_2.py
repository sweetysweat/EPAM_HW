import time

import pytest

from homework3.task2 import multiprocessing_calculation

test_data = [i for i in range(10)]


@pytest.mark.parametrize("pools, input_data, time_to_execute", [[20, test_data, 10]])
def test_multiprocessing_calculation(pools, input_data, time_to_execute):
    time_start_execution = time.time()
    multiprocessing_calculation(input_data)
    assert (time.time() - time_start_execution) < 10
