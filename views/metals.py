import sqlite3
from models import Metal

METALS = [
    {
        "id": 1,
        "metal": "Sterling Silver",
        "price": 12.42
    },
    {
        "id": 2,
        "metal": "14K Gold",
        "price": 736.4
    },
    {
        "id": 3,
        "metal": "24K Gold",
        "price": 1258.9
    },
    {
        "id": 4,
        "metal": "Platinum",
        "price": 795.45
    },
    {
        "id": 5,
        "metal": "Palladium",
        "price": 1241.0
    }]

def get_all_metals(query_params):
    '''Shows all METALS.'''
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        sort_by = ""

        if len(query_params) != 0:
            param = query_params[0]
            [qs_key, qs_value] = param.split("=")

            if qs_key == "_sortBy":
                sort_by = f"ORDER BY m.{qs_value} ASC"

        sql_to_execute = f"""
        SELECT
            m.id,
            m.metal,
            m.price
        FROM Metals m
        {sort_by}
        """

        db_cursor.execute(sql_to_execute)

        metals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            metal = Metal(row['id'], row['metal'], row['price'])
            metals.append(metal.__dict__)

    return metals


def get_single_metal(id):
    '''Shows a single metal from METALS.'''
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            m.id,
            m.metal,
            m.price
        FROM Metals m
        WHERE m.id = ?    
        """, (id, ))
        data = db_cursor.fetchone()
        metal = Metal(data['id'], data['metal'], data['price'])
        return metal.__dict__


def update_metal(id, new_metal):
    ''' Handles updating information of existing animals. '''
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        UPDATE Metals
            SET
                metal = ?,
                price = ?
        WHERE id = ?
        """ , (new_metal['metal'], new_metal['price'], id, ))

        rows_affected = db_cursor.rowcount

        if rows_affected == 0:
            return False
        return True
