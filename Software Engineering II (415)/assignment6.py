import unittest


def calcTotal(subtotal):
    total = round(subtotal + ((subtotal/100)*15), 2)
    return total


def calcSplit(subtotal, guests):
    total = calcTotal(subtotal)
    splitCost = round(total/guests,2)
    return splitCost

def main():
    subtotal = float(input("enter dinner total: "))
    numGuests = int(input("enter number of guests: "))
    
    print("subtotal:\t" + str(subtotal))
    print("total:\t\t" + str(calcTotal(subtotal)))
    print("guests:\t\t" + str(numGuests))
    print("guest total:\t" + str(calcSplit(subtotal, numGuests)))

class test_split(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(calcSplit(120, 4), 34.5)
    def test_equal2(self):
        self.assertEqual(calcSplit(120, 4), 50)
    def test_calcTotal(self):
        self.assertRaises(ValueError, calcTotal('.001'))
    def test_calcSplitSubtotal(self):
        self.assertRaises(ValueError, calcSplit("asd", 1))
    def test_calcSplitGuests(self):
        self.assertRaises(ValueError, calcSplit(120, "asd"))

if __name__ == '__main__':
    unittest.main()
    main()

