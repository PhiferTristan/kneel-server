import sqlite3
import json
from nss_handler import status
from repository import db_get_single, db_get_all, db_update

class OrdersView():

    def get(self, handler, url):
        if url['pk'] != 0:
            sql = "SELECT o.id, o.metal_id, o.size_id, o.style_id FROM Orders o WHERE o.id = ?"
            query_results = db_get_single(sql, url['pk'])
            serialized_order = json.dumps(dict(query_results))

            return handler.response(serialized_order, status.HTTP_200_SUCCESS.value)

        else:
            query_results = db_get_all("SELECT o.id, o.metal_id, o.size_id, o.style_id FROM Orders o")
            orders = [dict(row) for row in query_results]
            serialized_orders = json.dumps(orders)

            return handler.response(serialized_orders, status.HTTP_200_SUCCESS.value)
