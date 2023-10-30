import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status


# Add your imports below this line
from views import SizesView, MetalsView, StylesView


class JSONServer(HandleRequests):

    def do_GET(self):
        url = self.parse_url(self.path)
        view = self.determine_view(url)

        try:
            view.get(self, url)
        except AttributeError:
            return self.response("No view for that route", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

    def do_PUT(self):
        self.response("You can't do that! Method NOT ALLOWED!!", status.HTTP_405_UNSUPPORTED_METHOD.value)

    def do_DELETE(self):
        url = self.parse_url(self.path)
        view = self.determine_view(url)
        if "orders" not in self.path:
            return self.response("Method not allowed!", status.HTTP_405_UNSUPPORTED_METHOD.value)
        else:
            try:
                view.delete(self, url)
            except AttributeError:
                return self.response("No view for that route", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

    def do_POST(self):
        # Parse the URL
        url = self.parse_url(self.path)
        # Determine the correct view needed to handle the requests
        view = self.determine_view(url)
        if "orders" not in self.path:
            return self.response("Method not allowed!", status.HTTP_405_UNSUPPORTED_METHOD.value)
        else:
        # Get the request body
            content_len = int(self.headers.get('content-length', 0))
            request_body = self.rfile.read(content_len)
            post_data = json.loads(request_body)
            # Invoke the correct method on the view
            try:
                view.create(self, post_data)
            except AttributeError:
                return self.response("No view for that route", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)


    def determine_view(self, url):
        """Lookup the correct view class to handle the requested route

        Args:
            url (dict): The URL dictionary

        Returns:
            Any: An instance of the matching view class
        """
        try:
            routes = {
                "sizes": SizesView,
                "metals": MetalsView,
                "styles": StylesView
            }

            matching_class = routes[url["requested_resource"]]
            return matching_class()
        except KeyError:
            return status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value


#
# THE CODE BELOW THIS LINE IS NOT IMPORTANT FOR REACHING YOUR LEARNING OBJECTIVES
#
def main():
    host = ''
    port = 8000
    HTTPServer((host, port), JSONServer).serve_forever()

if __name__ == "__main__":
    main()
