import sqlite3
import json
from nss_handler import status
from repository import db_get_single, db_get_all

class StylesView():

    def get(self, handler, url):
        if url['pk'] != 0:
            sql = "SELECT s.id, s.style, s.price FROM Styles s WHERE s.id = ?"
            query_results = db_get_single(sql, url['pk'])
            serialized_style = json.dumps(dict(query_results))

            return handler.response(serialized_style, status.HTTP_200_SUCCESS.value)

        else:
            query_results = db_get_all("SELECT s.id, s.style, s.price FROM Styles s")
            styles = [dict(row) for row in query_results]
            serialized_styles = json.dumps(styles)

            return handler.response(serialized_styles, status.HTTP_200_SUCCESS.value)
