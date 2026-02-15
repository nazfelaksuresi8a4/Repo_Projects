from dataclasses import dataclass, field, asdict
from typing import List
from uuid import uuid4
from datetime import datetime


@dataclass(order=True, slots=True)
class Product:
    price: float
    name: str
    stock: int = field(default=0, compare=False)

    def __post_init__(self):
        if self.price <= 0:
            raise ValueError("Fiyat 0'dan büyük olmalı")
        if self.stock < 0:
            raise ValueError("Stok negatif olamaz")


@dataclass(slots=True)
class Customer:
    name: str
    email: str
    created_at: datetime = field(default_factory=datetime.utcnow)

    def __post_init__(self):
        if "@" not in self.email:
            raise ValueError("Geçersiz email adresi")


@dataclass(slots=True)
class Order:
    customer: Customer
    products: List[Product]
    order_id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=datetime.utcnow)
    _total: float = field(init=False, repr=False)

    def __post_init__(self):
        if not self.products:
            raise ValueError("Sipariş boş olamaz")

        self._total = sum(p.price for p in self.products)

    @property
    def total(self):
        return self._total

    def to_dict(self):
        return asdict(self)
