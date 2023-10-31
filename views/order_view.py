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

    def update(self, handler, order_data, pk):
        sql = "UPDATE Orders SET metal_id = ?, size_id = ?, style_id = ? WHERE id = ?"
        row_updated = db_update(sql, (order_data['metal_id'], order_data['size_id'], order_data['style_id'], pk))

        if row_updated > 0:
            return handler.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
        else:
            return handler.response("", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
