from data_transform.tests import calc_rate_test, lag_values_test
from data_transform.util.file_extension import *

assert remove_extension("hello.csv") == 'hello'
assert remove_extension("hello.ext") == 'hello'
assert remove_extension("hello") == 'hello'
assert lag_values_test.df.dropna().size == lag_values_test.df.size
