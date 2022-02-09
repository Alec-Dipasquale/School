import unittest 
import short

class Test(unittest.TestCase):

    def test_x1(self): #it checks the main method
        self.assertRaises(ValueError, short.process_input("",1,1,3))
    
    def test_y1(self): #it checks the main method
        self.assertRaises(ValueError, short.process_input(1,"skdk",2,3))
        
        
    def test_x2(self): #it checks the main method
        self.assertRaises(ValueError, short.process_input(1,1,"alkdj",5))
        
    def test_y2(self): #it checks the main method
        self.assertRaises(ValueError, short.process_input(1,1,5,""))
    
    def test4(self): #it checks the main method
        self.assertEqual(0, short.shortest_distance(7,1,1,1))
    
    def test5(self): #it checks the main method
        self.assertEqual(None, short.process_input("","a",1,1))



if __name__ == '__main__':
    unittest.main()