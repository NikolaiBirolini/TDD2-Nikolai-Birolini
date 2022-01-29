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


    def test_func_deriv(self):
        self.assertEqual(func.func_deriv([]),False) # empty list
        self.assertEqual(func.func_deriv([1]),False) # derivation of a point
        self.assertEqual(func.func_deriv([2,2,2]),[0,0]) # const derivation
        self.assertEqual(func.func_deriv([2,2,2,3,4,5]),[0,0,1,1,1]) # func par morceau

        self.assertEqual(func.func_deriv([-4,-5,-6]),[-1,-1]) # neg derivation
        self.assertEqual(func.func_deriv([1,2,3,4,5]),[1,1,1,1]) # pos derivation
        self.assertEqual(func.func_deriv([0.5,1,1.5]),[0.5,0.5]) # h le pas, float
        self.assertEqual(func.func_deriv([2,4,8]),[2,4]) # x²


    #def test_func_deriv_sec(self):


    #def test_func_approx(self):


if __name__ == "__main__":
    unittest.main()