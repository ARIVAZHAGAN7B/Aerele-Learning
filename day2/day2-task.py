import frappe


def handle_order(data):
    if data:
        if data.get("customer"):
            if data.get("items"):
                total = 0
                for item in data["items"]:
                    if item.get("qty") and item.get("rate"):
                        line_total = item["qty"] * item["rate"]
                        if item.get("discount"):
                            line_total = line_total - (line_total * item["discount"] / 100)
                        total = total + line_total
                if total > 0:
                    doc = frappe.new_doc("Sales Order")
                    doc.customer = data["customer"]
                    doc.grand_total = total
                    for item in data["items"]:
                        doc.append("items", {
                            "item_code": item.get("item_code"),
                            "qty": item.get("qty"),
                            "rate": item.get("rate")
                        })
                    doc.insert()
                    if total > 50000:
                        frappe.sendmail(recipients=["manager@example.com"], subject="Large order placed")
                    return doc.name
                else:
                    return None
            else:
                return None
        else:
            return None
    else:
        return None