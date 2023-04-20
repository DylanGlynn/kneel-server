import sqlite3
from models import Style

STYLES = [
    {
        "id": 1,
        "style": "Classic",
        "price": 500
    },
    {
        "id": 2,
        "style": "Modern",
        "price": 710
    },
    {
        "id": 3,
        "style": "Vintage",
        "price": 965
    }]

def get_all_styles(query_params):
    '''Shows all STYLES.'''
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        sort_by = ""

        if len(query_params) != 0:
            param = query_params[0]
            [qs_key, qs_value] = param.split("=")

            if qs_key == "_sortBy":
                sort_by = f"ORDER BY t.{qs_value} ASC"

        sql_to_execute = f"""
        SELECT
            t.id,
            t.style,
            t.price
        FROM Styles t
        {sort_by}
        """

        db_cursor.execute(sql_to_execute)

        styles = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            style = Style(row['id'],
                          row['style'],
                          row['price'],)

            styles.append(style.__dict__)

    return styles

def get_single_style(id):
    '''Shows a single style of STYLES.'''
    requested_style = None
    for style in STYLES:
        if style["id"] == id:
            requested_style = style

    return requested_style
