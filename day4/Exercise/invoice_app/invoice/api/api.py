from invoice.models.invoice import Invoice
from invoice.service.invoice_service import process


def create_invoice(customer, amount):

    invoice = Invoice(customer, amount)

    process(invoice)


def main():
    create_invoice("Alice", 500)