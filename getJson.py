#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      LianGee
#
# Created:     06/08/2016
# Copyright:   (c) LianGee 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import BaseHTTPServer
import io, shutil
import urllib
import os, sys, json
class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        mpath,margs = urllib.splitquery(self.path) # split with ?
        self.do_action(mapth, margs)

    def do_POST(self):
        mpath,margs=urllib.splitquery(self.path)
        datas = self.rfile.read(int(self.headers['content-length']))
        self.do_action(mpath, datas)
        dic = {"status":200, "group":8}
        str = json.dumps(dic)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type','application/json')
        self.end_headers()
        print str
        self.wfile.write(str)
        self.connection.shutdown(1)

    def do_action(self, path, args):
        print path

        print type(args), args

server_address = ('127.0.0.1', 8888)
server_class=BaseHTTPServer.HTTPServer
httpd = server_class(server_address, MyRequestHandler)
httpd.serve_forever()



