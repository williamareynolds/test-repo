def is_odd(num):
  return num % 2 == 1

def test_is_odd_returns_true_for_odd():
  assert is_odd(3) "3 should be odd, but was considered even"
  
def test_is_odd_returns_false_for_even():
  assert not is_odd(2) "2 should be even, but was considered odd"
 
test_is_odd_returns_true_for_odd()
test_is_odd_returns_false_for_even()
