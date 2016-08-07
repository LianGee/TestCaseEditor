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
import urllib, urllib2
import os, sys, json
class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        mpath,margs = urllib.splitquery(self.path) # split with ?
        self.do_action(mapth, margs)

    def do_POST(self):
        mpath,margs=urllib.splitquery(self.path)
        datas = self.rfile.read(int(self.headers['content-length']))
        str = self.do_action(mpath, datas)
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
        JNstr = json.loads(args)
        if JNstr['Priority'] == 8:
            dic = {"status":200, "group":8}
            return json.dumps(dic)
        else:
            dic = {
            	'JobID': 'John',
            	'Priority': 8,
            	'Description':'c://json.json',
            	'TestOutput': {
                  "order_url":'',
                  "response":'',
                  "response1":'',
                  "response2":'',
                  "response3":'',
                  "response4":[1,2,3,1123,123123],
                },
            	'ExpectOutput': 28,
            	'status':'waiting',
            }
            return json.dumps(dic)

    def send_data(self):
        url = "http://localhost:8000/TestCaseEditor/html/TestReport.html"
        data ={'user':'Smith','passwd':'123456'}
        jsonStr = json.dumps(data)
        req = urllib2.Request(url, jsonStr)
        responses = urllib2.urlopen(req)
        return responses.read()

server_address = ('127.0.0.1', 8888)
server_class=BaseHTTPServer.HTTPServer
httpd = server_class(server_address, MyRequestHandler)
httpd.serve_forever()



