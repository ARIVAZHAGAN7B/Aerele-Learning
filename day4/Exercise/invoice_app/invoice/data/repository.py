from invoice.config import DB_NAME


def save(invoice):
    print(f"Saving to {DB_NAME}")
    print(invoice.customer, invoice.amount)