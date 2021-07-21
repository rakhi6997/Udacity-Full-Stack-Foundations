from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
import cgitb
cgitb.enable()


class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Hello!</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text' ><input type='submit' value='Submit'> </form>'''
                output += "</body></html>"
                self.wfile.write(output.encode())
                print(output)
                return

            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>&#161 Hola !<a href 'hello'>Back to Hello!</a></h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text' ><input type='submit'value='Submit'> </form>'''
                output += "</body></html>"
                self.wfile.write(output.encode())
                print(output)
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            print("I am in Post Method1")
            self.send_response(301)
            print("I am in Post Method2")
            self.send_header('Content-type', 'text/html')
            print("I am in Post Method3")
            self.end_headers()
            print("I am in Post Method4")
            ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))
            print("I am in Post Method5")
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')
            print("I am in Post Method6")
            output = ""
            print("I am in Post Method7")
            output += "<html><body>"
            print("I am in Post Method8")
            output += " <h2> Okay, how about this: </h2>"
            print("I am in Post Method9")
            output += "<h1> %s </h1>" % messagecontent[0]
            print("I am in Post Method10")
            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text' ><input type='submit' value='Submit'> </form>'''
            print("I am in Post Method11")
            output += "</body></html>"
            self.wfile.write(output.encode())
            print("I am in Post Method")
        except:
            pass
 

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print("Web Server running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print(" ^C entered, stopping web server....")
        server.socket.close()

if __name__ == '__main__':
    main()