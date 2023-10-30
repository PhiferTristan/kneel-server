import sqlite3
import json
from nss_handler import status
from repository import db_get_single, db_get_all

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
   