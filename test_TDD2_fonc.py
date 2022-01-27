import string
import unittest
import func

class test_func(unittest.TestCase):
    def test_func_mirroir(self):
        self.assertEqual(func.func_mirroir("",1),False) # string empty
        self.assertEqual(func.func_mirroir("trop",10),False) # number out of range
        self.assertEqual(func.func_mirroir("maison",-1),False) # invalid value
        self.assertEqual(func.func_mirroir("maison",0),"mm") # 0 value
        self.assertEqual(func.func_mirroir("azertyuiop",3),"azerreza") 


    #def test_func_deriv(self):


    #def test_func_deriv_sec(self):


    #def test_func_approx(self):


if __name__ == "__main__":
    unittest.main()