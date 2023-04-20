import sqlite3
import json
from models import Size

SIZES = [
    {
        "id": 1,
        "carets": 0.5,
        "price": 405
    },
    {
        "id": 2,
        "carets": 0.75,
        "price": 782
    },
    {
        "id": 3,
        "carets": 1,
        "price": 1470
    },
    {
        "id": 4,
        "carets": 1.5,
        "price": 1997
    },
    {
        "id": 5,
        "carets": 2,
        "price": 3638
    }
]

def get_all_sizes(query_params):
    '''Shows all SIZES.'''
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        sort_by = ""

        if len(query_params) != 0:
            param = query_params[0]
            [qs_key, qs_value] = param.split("=")

            if qs_key == "_sortBy":
                sort_by = f"ORDER BY s.{qs_value} ASC"

        sql_to_execute = f"""
        SELECT
            s.id,
            s.size,
            s.price
        FROM Sizes s
        {sort_by}
        """
        db_cursor.execute(sql_to_execute)

        sizes = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            size = Size(row['id'],
                        row['size'],
                        row['price'])

            sizes.append(size.__dict__)

    return sizes

def get_single_size(id):
    '''Shows a single size of SIZES.'''
    requested_size = None
    for size in SIZES:
        if size["id"] == id:
            requested_size = size

    return requested_size
