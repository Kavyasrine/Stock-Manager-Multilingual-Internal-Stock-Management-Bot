from .classifier import rule_intent
from .nlp_model import extract_entities
from .db.products import get_product_by_name, update_quantity, create_product, set_threshold, list_products
from .db.transactions import log_transaction
from .predictor import check_threshold_and_recommend

def handle_message(text: str):
    intent = rule_intent(text)
    entities = extract_entities(text)
    product_name = entities.get('product')
    qty = entities.get('quantity')

    if intent == 'check_stock':
        if not product_name:
            return "Which product do you want to check?"
        p = get_product_by_name(product_name)
        if not p:
            return f"Product '{product_name}' not found."
        rec = check_threshold_and_recommend(p)
        return f"{p['name']} — {p['quantity']} units. Threshold {p['threshold']}. Suggest restock: {rec['suggest_restock']} units."

    if intent == 'add_stock':
        if not product_name or qty is None:
            return "Please specify product name and quantity to add."
        p = get_product_by_name(product_name)
        if not p:
            create_product(product_name, quantity=qty)
            log_transaction(product_name, qty, reason='add')
            return f"Created product {product_name} with {qty} units."
        updated = update_quantity(product_name, qty)
        log_transaction(product_name, qty, reason='add')
        return f"Updated {updated['name']} — {updated['quantity']} units now."

    if intent == 'remove_stock':
        if not product_name or qty is None:
            return "Please specify product name and quantity to remove."
        p = get_product_by_name(product_name)
        if not p:
            return f"Product '{product_name}' not found."
        updated = update_quantity(product_name, -qty)
        log_transaction(product_name, -qty, reason='remove')
        return f"Updated {updated['name']} — {updated['quantity']} units now."

    if intent == 'list_products':
        products = list_products()
        return "\n".join([f"{p['name']} — {p['quantity']} units" for p in products])

    if intent == 'set_threshold':
        if not product_name or qty is None:
            return "Please specify product name and threshold value."
        updated = set_threshold(product_name, qty)
        return f"Threshold for {updated['name']} set to {updated['threshold']} units."

    return "Sorry, I didn't understand that."
