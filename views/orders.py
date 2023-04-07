ORDERS = [
    { 
    "metalId": 1,
    "sizeId": 3,
    "styleId": 2,
    "timestamp": 161459931693,
    "id": 1
    }
]

def get_all_orders():
    ''' Shows all ORDERS. '''
    return ORDERS

def get_single_order(id):
    '''Shows a single order from ORDERS.'''
    requested_order = None
    for order in ORDERS:
        if order["id"] == id:
            requested_order = order

    return requested_order

def create_order(order):
    '''Get the id value of the last order in the list.'''
    max_id = ORDERS[-1]["id"]
    new_id = max_id + 1
    order["id"] = new_id
    ORDERS.append(order)
    return order
