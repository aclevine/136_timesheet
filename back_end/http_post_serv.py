import os, sys
import BaseHTTPServer, cgi

servAddr = ('localhost',8000)

#Define the HTTP handler that overrides do_POST
class httpServHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):
        
        # Setup the form
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type']}
        )
        
        # The uploaded file
        upfile = form['upfile']
        
        # Allow us to write back to the user in the browser
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        sys.stdout = self.wfile
        
        #Handle the post
        self.wfile.write("<h2>Handling Post</h2><P>")
        self.wfile.write("<li>Form headers: {}<hr>".format(str(form.headers)))
        self.wfile.write("<li>Uploaded filename: <b>{}</b><hr>".format(upfile.filename))
        #self.wfile.write("<li>Location: <b>{}</b>".format(self.path))
        self.wfile.write("<li>Arguments: <b>{}</b><hr>".format(self.args))
        length = self.headers['content-length']
        self.wfile.write("<li>Content-length: <b>{}</b><hr>".format(length))
        
        #Write the uploaded file to server
        with open(upfile.filename, 'wb') as file:
            while True:
                chunk = upfile.file.read(8192)
                if len(chunk) == 0:
                    break
                else:
                    file.write(chunk)
        
        #Execute the script remotely
        execfile(self.path, self.args)

#Set the root directory
home = os.envrion['HOME']
if 'Sites' in os.listdir(home):
    os.chdir(os.path.join(home, 'Sites'))
else:
    os.chdir(home)

#Create server object
serv = BaseHTTPServer.HTTPServer(servAddr, httpServHandler)

#Start Server
serv.serve_forever()