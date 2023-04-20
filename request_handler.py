from urllib.parse import urlparse#, parse_qs
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_metals, get_single_metal, update_metal
from views import get_all_sizes, get_single_size
from views import get_all_styles, get_single_style
from views import get_all_orders, get_single_order
from views import create_order, delete_order#, update_order

class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """
    def parse_url(self, path):
        ''' Just like splitting a string in JavaScript. If the '''
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        url_components = urlparse(path)
        path_params = url_components.path.strip("/").split("/")
        query_params = []

        if url_components.query != "":
            query_params = url_components.query.split("&")

        resource = path_params[0]
        id = None

        # Try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[1])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id, query_params)

    def do_GET(self):
        """Handles GET requests to the server """
        # self._set_headers(200)

        response = {} # Default response
        parsed = self.parse_url(self.path)

        if '?' not in self.path:
            (resource, id, query_params) = parsed

            if resource == "metals":
                if id is not None:
                    response = get_single_metal(id)
                else:
                    print('If resource = metals and no Id.')
                    response = get_all_metals(query_params)

            elif resource == "sizes":
                if id is not None:
                    response = get_single_size(id)
                else:
                    response = get_all_sizes(query_params)

            elif resource == "styles":
                if id is not None:
                    response = get_single_style(id)
                else:
                    response = get_all_styles(query_params)

            elif resource == "orders":
                if id is not None:
                    response = get_single_order(id)
                else:
                    response = get_all_orders()

        else:
            (resource, id, query_params) = parsed

            if resource == "metals":
                #if query_params.get("price"):
                response = get_all_metals(query_params)
            elif resource == "sizes":
                response = get_all_sizes(query_params)
            elif resource == "styles":
                response = get_all_styles(query_params)

        if response is None:
            self._set_headers(404)
        else:
            self._set_headers(200)

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Handles POST requests to the server """
        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id, query_params) = self.parse_url(self.path)

        new_order = None

        if resource == "orders":
            if "metal_id" in post_body and "size_id" in post_body and "style_id" in post_body:
                self._set_headers(201)
                new_order = create_order(post_body)
            else:
                self._set_headers(400)
                new_order = {"message":
                             f'{"Metal selection is required." if "metalId" is not post_body else ""} {"Size selection is required." if "sizeId" is not post_body else ""} {"Style selection is required." if "styleId" is not post_body else ""}'}

        self.wfile.write(json.dumps(new_order).encode())

    def do_PUT(self):
        """Handles PUT requests to the server """
        # self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id, query_params) = self.parse_url(self.path)

        success = False

        if resource == "orders":
            # update_order(id, post_body)
            self._set_headers(400)

        elif resource == 'metals':
            success = update_metal(id, post_body)

        if success:
            self._set_headers(204)
        else:
            self._set_headers(400)

        self.wfile.write("".encode())


    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_DELETE(self):
        '''Delete method.'''
        self._set_headers(204)
        (resource, id, query_params) = self.parse_url(self.path)
        if resource == "orders":
            delete_order(id)

        self.wfile.write("".encode())


# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()
