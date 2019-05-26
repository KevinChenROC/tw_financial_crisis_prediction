from data_transform.tests import calc_rate_test, lag_values_test
from data_transform.tests.stats_test import *
from data_transform.tests.file_extension_test import *
from data_transform.tests import crisis_features_test

calc_rate_test.run_tests()
lag_values_test.run_tests()
run_file_ext_tests()
run_stats_test()
