from data_transform.tests import calc_rate_test, lag_values_test
from data_transform.tests.stats_test import *
from data_transform.tests.file_extension_test import *

run_stats_test()
run_file_ext_tests()
assert lag_values_test.df.dropna().size == lag_values_test.df.size
