from warehouse_manager.models import WarehouseItem


def add_stock(item: WarehouseItem, amount: int) -> None:
    """Збільшує кількість товару на складі (надходження)."""
    if amount > 0:
        item.quantity += amount


def decrease_stock(item: WarehouseItem, amount: int) -> bool:
    """Зменшує кількість товару на складі (списання). Повертає True, якщо успішно."""
    if 0 < amount <= item.quantity:
        item.quantity -= amount
        return True
    return False


def find_item_by_code(items: list[WarehouseItem], code: str) -> WarehouseItem | None:
    """Шукає позицію за унікальним кодом."""
    for item in items:
        if item.code.lower() == code.lower():
            return item
    return None


def calculate_total_warehouse_value(items: list[WarehouseItem]) -> float:
    """Обчислює загальну вартість усіх запасів на складі."""
    return sum(item.total_value for item in items)


def find_low_stock_items(items: list[WarehouseItem], threshold: int = 5) -> list[WarehouseItem]:
    """Визначає товари із низьким запасом (нижче або дорівнює пороговому значенню)."""
    return [item for item in items if item.quantity <= threshold]