import unittest
from datetime import datetime
from Order_Class import Order 

class TestOrder(unittest.TestCase):

    def test_add_item_updates_total_cost(self):
        """Test that add_item correctly updates the total cost."""
        order = Order(date=datetime.now())
        order.add_item('Widget', 3, 'Supplier A', 10.0)
        
        # Assert that the total cost is correctly calculated
        self.assertEqual(order.total_cost, 30.0)  # 3 * 10.0 = 30.0

    def test_get_order_details_returns_correct_items(self):
        """Test that get_order_details returns the correct items."""
        order = Order(date=datetime.now())
        order.add_item('Widget', 2, 'Supplier A', 5.0)
        order.add_item('Gadget', 1, 'Supplier B', 15.0)

        expected_items = [
            ['Widget', 2, 'Supplier A'],
            ['Gadget', 1, 'Supplier B']
        ]

        # Assert that the returned list of items matches the expected list
        self.assertEqual(order.get_order_details(), expected_items)

if __name__ == '__main__':
    unittest.main()