from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional


@dataclass
class InvoiceItem:
    item_code: str
    qty: float
    rate: float

    @property
    def amount(self) -> float:
        return self.qty * self.rate


@dataclass
class InvoiceData:
    """Pure data shape of an Invoice — mirrors a DocType's field schema / DB row."""
    customer: str
    posting_date: date
    items: List[InvoiceItem] = field(default_factory=list)
    name: Optional[str] = None       # docname, None until saved
    status: str = "Draft"
    grand_total: float = 0.0
    docstatus: int = 0               # 0 Draft, 1 Submitted, 2 Cancelled





class InvoiceController:
    """Behavior layer — equivalent of the .py controller Frappe loads for a DocType."""

    def __init__(self, data: InvoiceData):
        self.data = data

    def validate(self):
        """Frappe calls this automatically before every save."""
        self._validate_items()
        self._calculate_totals()
        self._validate_customer_credit()

    def _validate_items(self):
        if not self.data.items:
            raise ValueError("Invoice must have at least one item")
        for item in self.data.items:
            if item.qty <= 0:
                raise ValueError(f"Qty for {item.item_code} must be positive")

    def _calculate_totals(self):
        self.data.grand_total = sum(i.amount for i in self.data.items)

    def _validate_customer_credit(self):
        # stand-in for a real check against the Customer doctype's credit_limit field
        if self.data.grand_total > 500000 and self.data.customer == "Unverified Customer":
            raise ValueError("Credit limit exceeded")

    def submit(self):
        self.validate()
        self.data.docstatus = 1
        self.data.status = "Submitted"