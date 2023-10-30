import sqlite3
import json
from nss_handler import status
from repository import db_get_single, db_get_all, db_update

class SizesView():

    def get(self, handler, url):
        if url['pk'] != 0:
            sql = "SELECT s.id, s.carets, s.price FROM Sizes s WHERE s.id = ?"
            query_results = db_get_single(sql, url['pk'])
            serialized_size = json.dumps(dict(query_results))

            return handler.response(serialized_size, status.HTTP_200_SUCCESS.value)

        else:
            query_results = db_get_all("SELECT s.id, s.carets, s.price FROM Sizes s")
            sizes = [dict(row) for row in query_results]
            serialized_sizes = json.dumps(sizes)

            return handler.response(serialized_sizes, status.HTTP_200_SUCCESS.value)

    def update(self, handler, size_data, pk):
        sql = "UPDATE Sizes SET carets = ?, price = ? WHERE id = ?"
        row_updated = db_update(sql, (size_data['carets'], size_data['price'], pk))

        if row_updated > 0:
            return handler.response("The size has been updated :)", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
        else:
            return handler.response("Size not found :(", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

    def delete(self, handler):
        return handler.response("Unsupported Method!", status.HTTP_405_UNSUPPORTED_METHOD.value)
    