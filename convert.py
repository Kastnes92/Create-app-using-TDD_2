import sys
import unittest

class LengthConverter:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
        
    def to_mm(self):
        if self.unit == 'inches':
            return self.value * 25.4
        elif self.unit == 'cm':
            return self.value * 10
        elif self.unit == 'm':
            return self.value * 1000
        else:
            raise ValueError("Invalid input unit")
        
    def to_cm(self):
        if self.unit == 'inches':
            return self.value * 2.54
        elif self.unit == 'mm':
            return self.value / 10
        elif self.unit == 'm':
            return self.value * 100
        else:
            raise ValueError("Invalid input unit")
        
    def to_m(self):
        if self.unit == 'inches':
            return self.value / 39.37
        elif self.unit == 'mm':
            return self.value / 1000
        elif self.unit == 'cm':
            return self.value / 100
        else:
            raise ValueError("Invalid input unit")

class TestLengthConverter(unittest.TestCase):
    def test_to_mm(self):
        self.assertAlmostEqual(LengthConverter(1, 'inches').to_mm(), 25.4)
        
    def test_to_cm(self):
        self.assertAlmostEqual(LengthConverter(1, 'inches').to_cm(), 2.54)
        
    def test_to_m(self):
        self.assertAlmostEqual(LengthConverter(1, 'inches').to_m(), 0.0254)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python converter.py <value> <unit>")
    else:
        value = float(sys.argv[1])
        unit = sys.argv[2]
        converter = LengthConverter(value, 'inches')
        if unit == 'mm':
            print(converter.to_mm())
        elif unit == 'cm':
            print(converter.to_cm())
        elif unit == 'm':
            print(converter.to_m())
        else:
            print("Invalid output unit")