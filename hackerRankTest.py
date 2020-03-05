import unittest
from grid import grid

class Test(unittest.TestCase):

    def test_grid(self):
        expected_id = [0,2];
        generated_id = grid(3, 0, 0,"RR")
        self.assertEqual(expected_id, generated_id)
        

if __name__ == '__main__':
    unittest.main()

        

        
   





        

        
   






