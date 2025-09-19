from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>
            Ref.no=25012265
        </title>
    </head>
        <body>
            Name   : Shreeshanth R<br>
            Ref_no : 25012265
            <table border="3" cellspacing="0" cellpadding="3">
                <tr>
                    <th>S.NO.</th>
                    <th>Device Specification</th>
                    <th>Details</th>
                </tr>
                <tr>
                    <td>1</td>
                    <td>Storage</td>
                    <td>447GB</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>RAM</td>
                    <td>16GB</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>GRAPHICS CARD</td>
                    <td>RTX 3050</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>GRAPHICS CARD MEMORY</td>
                    <td>6GB</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>WINDOWS</td>
                    <td>11</td>
                </tr>
            </table>
        </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()