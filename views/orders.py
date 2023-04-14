import sqlite3
from models import Metal, Size, Style, Order
from .metals import get_single_metal
from .sizes import get_single_size
from .styles import get_single_style

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
        "styleId": 2,
        "timestamp": 161459931693,
        "id": 2}
]


def get_all_orders():
    ''' Shows all ORDERS. '''
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            o.timestamp,
            m.metal,
            m.price metal_price,
            s.size,
            s.price size_price,
            t.style,
            t.price style_price
        FROM Orders o
        JOIN Metals m
            ON m.id = o.metal_id
        JOIN Sizes s
            ON s.id = o.size_id
        JOIN Styles t
            On t.id = o.style_id
        """)

        orders = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            order = Order(row['id'], row['metal_id'],
                          row['size_id'], row['style_id'],
                          row['timestamp'])
            metal = Metal(row['metal_id'], row['metal'],
                          row['metal_price'])
            size = Size(row['size_id'], row['size'], row['size_price'])
            style = Style(row['style_id'], row['style'], row['style_price'])

            order.metal = metal.__dict__
            order.size = size.__dict__
            order.style = style.__dict__

            orders.append(order.__dict__)

    return orders


def get_single_order(id):
    '''Shows a single order from ORDERS.'''
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            o.timestamp,
            m.metal,
            m.price metal_price,
            s.size,
            s.price size_price,
            t.style,
            t.price style_price
        FROM Orders o
        JOIN Metals m
            ON m.id = o.metal_id
        JOIN Sizes s
            ON s.id = o.size_id
        JOIN Styles t
            On t.id = o.style_id
        WHERE o.id = ?
        """, (id,))

        data = db_cursor.fetchone()

        order = Order(data['id'], data['metal_id'],
                      data['size_id'], data['style_id'],
                      data['timestamp'])
        metal = Metal(data['metal_id'], data['metal'],
                      data['metal_price'])
        size = Size(data['size_id'], data['size'], data['size_price'])
        style = Style(data['style_id'], data['style'], data['style_price'])

        order.metal = metal.__dict__
        order.size = size.__dict__
        order.style = style.__dict__

        return order.__dict__

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
