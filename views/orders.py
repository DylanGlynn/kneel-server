ORDERS = [
    {
    "metalId": 1,
    "sizeId": 3,
    "styleId": 2,
    "timestamp": 161459931693,
    "id": 1
    },
    {
    "metalId": 2,
    "sizeId": 2,
    "styleId": 4,
    "timestamp": 161459931693,
    "id": 2}
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

def delete_order(id):
    '''The delete an order'''
    order_index = -1
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            order_index = index

    if order_index >= 0:
        ORDERS.pop(order_index)

def update_order(id, new_order):
    '''Handles the PUT request for order updates.'''
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break
