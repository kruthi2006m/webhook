import unittest

#application code 
def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
  
#automated test cases
class TestCalculator(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(20,20),40)
  def test_subtract(self):
    self.assertEqual(subtract(40,10),30)
  def test_multiply(self):
    self.assertEqual(multiply(6,4),24)

#main application
if __name__ == "__main__":
  print("student calculator application")
  print("addition:",add(20,20))
  print("subtraction:",subtract(40,10))
  print("multiplication:",multiply(6,4))
  print("\n Exectuting automated tests..\n")
  unittest.main(argv=['first-arg-is-ignored'],exit=False)
