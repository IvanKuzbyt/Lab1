from warehouse_manager.models import WarehouseItem
from warehouse_manager.services import (
    add_stock,
    calculate_total_warehouse_value,
    decrease_stock,
    find_item_by_code,
    find_low_stock_items,
)


def test_warehouse_item_total_value():
    item = WarehouseItem(code="A1", name="Test Item", quantity=10, price=150.0)
    assert item.total_value == 1500.0


def test_add_stock():
    item = WarehouseItem(code="A1", name="Test Item", quantity=5, price=100.0)
    add_stock(item, 5)
    assert item.quantity == 10


def test_decrease_stock_success():
    item = WarehouseItem(code="A1", name="Test Item", quantity=10, price=100.0)
    success = decrease_stock(item, 4)
    assert success is True
    assert item.quantity == 6


def test_decrease_stock_insufficient():
    item = WarehouseItem(code="A1", name="Test Item", quantity=5, price=100.0)
    success = decrease_stock(item, 10)
    assert success is False
    assert item.quantity == 5


def test_find_item_by_code():
    items = [
        WarehouseItem(code="A001", name="Mouse", quantity=10, price=500.0),
        WarehouseItem(code="A002", name="Keyboard", quantity=5, price=1500.0),
    ]
    found = find_item_by_code(items, "a002")
    assert found is not None
    assert found.name == "Keyboard"

    not_found = find_item_by_code(items, "Z999")
    assert not_found is None


def test_calculate_total_warehouse_value():
    items = [
        WarehouseItem(code="1", name="Item 1", quantity=2, price=100.0),
        WarehouseItem(code="2", name="Item 2", quantity=3, price=200.0),
    ]
    total = calculate_total_warehouse_value(items)
    assert total == 800.0


def test_find_low_stock_items():
    items = [
        WarehouseItem(code="1", name="Low", quantity=2, price=100.0),
        WarehouseItem(code="2", name="Normal", quantity=10, price=200.0),
        WarehouseItem(code="3", name="Borderline", quantity=5, price=50.0),
    ]
    low_items = find_low_stock_items(items, threshold=5)
    assert len(low_items) == 2
    codes = [item.code for item in low_items]
    assert "1" in codes
    assert "3" in codes