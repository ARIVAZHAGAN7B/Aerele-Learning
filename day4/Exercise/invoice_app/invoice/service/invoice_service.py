from invoice.data.repository import save

def validate_invoice(invoice):
    if invoice.amount <= 0:
        print("Invalid amount")
        return False
    return True

def process(invoice):

    if not validate_invoice(invoice):
        print("Invoice validation failed")
        return
    save(invoice)