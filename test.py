import unittest
from unittest import TestCase
from main import MainClass


class my_test(TestCase):
    def setUp(self):
        test_obj = MainClass(10, 'test_case')
        self.result = test_obj.get_all()

    def test_summ(self):
        for i in range(len(self.result)):
            #self.assertEqual(0,0)
            if i<3:
                self.assertEqual(0,len(self.result[i]))
            else:
                for ii in self.result[i]:
                    self.assertEqual(i,sum(ii))
    def test_un(self):
        for i in range(3,len(self.result)):
            c_ = 0
            s_ = set()
            for ii in self.result[i]:
                c_ += 1
                #r_=tuple(sorted(ii))
                s_.add(tuple(sorted(ii)))
            #print(s_,c_,len(s_))
            self.assertEqual(c_, len(s_))


if __name__=="__main__":
    unittest.main()
