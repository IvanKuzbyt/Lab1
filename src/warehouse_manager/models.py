from dataclasses import dataclass


@dataclass
class WarehouseItem:
    code: str
    name: str
    quantity: int
    price: float

    @property
    def total_value(self) -> float:
        """Обчислює загальну вартість даної позиції на складі."""
        return self.quantity * self.price