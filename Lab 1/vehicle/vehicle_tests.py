import unittest
import vehicle

class VehicleTests(unittest.TestCase):
   def test_vehicle(self, wheels = 4, fuel = .90, doors = 2, roof = True):
      a= vehicle.vehicle(wheels,fuel,doors,roof)
      self.assertEqual(a.wheels, 4)
      self.assertEqual(a.fuel, .90)
      self.assertEqual(a.doors, 2)
      self.assertTrue(a.roof, True)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

