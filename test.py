import unittest
from unittest import TestCase
from main import MainClass


class my_test(TestCase):

    def test_summ(self):
        test_obj = MainClass(10,'test_case')
        result = test_obj.get_all()
        for i in range(len(result)):
            #self.assertEqual(0,0)
            if i<3:
                self.assertEqual(0,len(result[i]))
            else:
                for ii in result[i]:
                    self.assertEqual(i,sum(ii))

if __name__=="__main__":
    unittest.main()
