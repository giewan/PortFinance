# test_portfinance.py
"""
Tests for PortFinance module.
"""

import unittest
from portfinance import PortFinance

class TestPortFinance(unittest.TestCase):
    """Test cases for PortFinance class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PortFinance()
        self.assertIsInstance(instance, PortFinance)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PortFinance()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
