import sqlite3
import json
from nss_handler import status
from repository import db_get_single, db_get_all, db_delete, db_create

class OrdersView():

    def get(self, handler, url):

        if url['pk'] != 0:
            order_id = url['pk']
            query_params = url.get('query_params', [])
            expand_params = query_params.get('_expand', [])

            # Define order SQL query to select an order
            order_sql = "SELECT o.id, o.metal_id, o.size_id, o.style_id FROM Orders o WHERE o.id = ?"

            order = db_get_single(order_sql, order_id)
            dict_order = dict(order)

            # Check if there are any expands
            if 'metal' in expand_params:
                # Separate SQL query for expanding the 'metal' table
                metal_sql = "SELECT m.metal AS metal_name, m.price AS metal_price FROM Orders o LEFT JOIN Metals m ON o.metal_id = m.id WHERE o.id = ?"
                metal_data = db_get_single(metal_sql, order_id)
                if metal_data:
                    metal_data = dict(metal_data)
                # expanded_data.append(('metal', metal_data))
                dict_order['metal'] = metal_data

            if 'size' in expand_params:
                size_sql = "SELECT s.carets AS size_carets, s.price AS size_price FROM Orders o LEFT JOIN Sizes s ON o.size_id = s.id WHERE o.id = ?"
                size_data = db_get_single(size_sql, order_id)
                if size_data:
                    size_data = dict(size_data)
                dict_order['size'] = size_data

            if 'style' in expand_params:
                style_sql = "SELECT st.style AS style_name, st.price AS style_price FROM Orders o LEFT JOIN Styles st ON o.style_id = st.id WHERE o.id = ?"
                style_data = db_get_single(style_sql, order_id)
                if style_data:
                    style_data = dict(style_data)
                dict_order['style'] = style_data


            serialized_order = json.dumps(dict_order)

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

        # expanded_data = []

        # order_data = {
        #     "id": order_id,
        #     "metal_id": order_id,
        #     "size_id": order_id,
        #     "style_id": order_id,
        # }

        # for table, data in expanded_data:
        #     if data:
        #         order_data[table] = data

        # if expanded_sql:
        #     final_sql = f"{order_sql} {expanded_fields[0]}    "
        # else:
        #     final_sql = order_sql

        # query_results = db_get_single(final_sql, order_id)

        # if query_results:

        #     order = dict(query_results)

        #     if 'metal' in expand_params:
        #         metal_data = {
        #             "name": order.pop("metal_name"),
        #             "price": order.pop("metal_price")
        #         }
        #         order["metal"] = metal_data

        #     if 'size' in expand_params:
        #         size_data = {
        #             "carets": order.pop("size_carets"),
        #             "price": order.pop("size_price")
        #         }
        #         order["size"] = size_data

        #     if 'style' in expand_params:
        #         style_data = {
        #             "name": order.pop("style_name"),
        #             "price": order.pop("style_price")
        #         }
        #         order["style"] = style_data

        #     serialized_order = json.dumps(order)
        # else:
        #     return handler.response("", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

        # return handler.response(serialized_order, status.HTTP_200_SUCCESS.value)

        #     expanded_orders = []

        #     for row in query_results:
        #         order = dict(row)

        #         if 'metal' in expand_params:
        #             metal_data = {
        #                 "name": order.pop("metal_name"),
        #                 "price": order.pop("metal_price")
        #             }
        #             order["metal"] = metal_data

        #         if 'size' in expand_params:
        #             size_data = {
        #                 "carets": order.pop("size_carets"),
        #                 "price": order.pop("size_price")
        #             }
        #             order["size"] = size_data

        #         if 'style' in expand_params:
        #             style_data = {
        #                 "name": order.pop("style_name"),
        #                 "price": order.pop("style_price")
        #             }
        #             order["style"] = style_data

        #         expanded_orders.append(order)

        #     serialized_orders = json.dumps(expanded_orders)
        # else:
        #     orders = [dict(row) for row in query_results]
        #     serialized_orders = json.dumps(orders)

        # return handler.response(serialized_orders, status.HTTP_200_SUCCESS.value)

    # def get(self, handler, url):
    #     if url['pk'] != 0:
    #         sql = "SELECT o.id, o.metal_id, o.size_id, o.style_id FROM Orders o WHERE o.id = ?"
    #         query_results = db_get_single(sql, url['pk'])
    #         serialized_order = json.dumps(dict(query_results))

    #         return handler.response(serialized_order, status.HTTP_200_SUCCESS.value)

    #     else:
    #         query_results = db_get_all("SELECT o.id, o.metal_id, o.size_id, o.style_id FROM Orders o")
    #         orders = [dict(row) for row in query_results]
    #         serialized_orders = json.dumps(orders)

    #         return handler.response(serialized_orders, status.HTTP_200_SUCCESS.value)
