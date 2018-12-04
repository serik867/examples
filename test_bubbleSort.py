import unittest
import bubblesort

class TestBubbleSort(unittest.TestCase):

    def test_bubbleSort(self):
        _list = [87,565,5,2,6,7,8,9]
        bubblesort.bubbleSort(_list)
        self.assertEqual(_list,[2,5,6,7,8,9,87,565],'Sorts correctly!!')







if __name__ == '__main__':
    unittest.main()



