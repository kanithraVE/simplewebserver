from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>laptop details</title>
    </head>
    <body align="center">
            <h1>laptop details</h1>
            <h2>KanithraVE</h2>
            <h2>26008403</h2>
        <table align="center" border="2">
        <tr>
            <td>device name</td>
            <td>kanithra</td>
        </tr>
        <tr>
            <td>processor</td>
            <td>Intel(R) Core(TM) 5 210H (2.20 GHz)</td>
        </tr>
        <tr> 
             <td>installed RAM</td>
             <td>16.0 GB (15.7 GB usable)</td>
        </tr>
        <tr>
            <td>Graphics card</td>
            <td>Intel(R) Graphics (128 MB)</td>
        </tr>
        <tr>
            <td>Storage</td>
            <td>114 GB of 477 GB used</td>
        </tr>
        <tr>
            <td>device ID </td>
            <td>C299E9CB-66C2-4366-8EAC-B9002EED96EB</td>
        </tr>
        <tr>
            <td>product id</td>
            <td>00342-42954-08641-AAOEM</td>
        </tr>
        <tr>
            <td>system type</td>
            <td>64-bit operating system, x64-based processor</td>
        </tr>
        <tr>
            <td>pen and touch</td>
            <td>No pen or touch input is available for this display</td>
        </tr>
        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()