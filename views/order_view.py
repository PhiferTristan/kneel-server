import sqlite3
import json
from nss_handler import status
from repository import db_get_single, db_get_all, db_delete, db_create

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

    def delete(self, handler, url):
        row_deleted = db_delete("DELETE FROM Orders WHERE id =?", url['pk'])

        if row_deleted > 0:
            return handler.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
        else:
            return handler.response("", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

    def create(self, handler, order_data):
        sql = "INSERT INTO Orders (metal_id, size_id, style_id) VALUES (?, ?, ?)"

        row_created = db_create(sql, (order_data['metal_id'], order_data['size_id'], order_data['style_id']))

        if row_created > 0:
            return handler.response("", status.HTTP_201_SUCCESS_CREATED.value)
        else:
            return handler.response("", status.HTTP_400_CLIENT_ERROR_BAD_REQUEST_DATA.value)
