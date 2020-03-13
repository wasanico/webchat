import random
import string
import json
import os

import cherrypy

filename = "user.json"
data = []


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head>
            <title> Whotsapp </title>
            
              <style>
                    table {
                    width: 100%;
                    border-color: black;
                    }
                </style>
          </head>
          <body>
            <header>
                <h1>Whotsapp </h1>
            </header>
            <form method="get" action="generate" >
              <p> Username 
                <input type="text" value="" name="username" />
                
              </p>
                            
              <button type="submit">Log in</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def generate(self, username="",password=""):
      if username != "" and username in data :
        return """<html>
          <body>
          <form method="get" action="loging" >
              <p> Welcome back !!! Please enter your password
                <p>
                <input type="text" value="" name="password" />
                </p>
                
              </p>


        </form>
        </body>
        </html>"""

      elif username !="" and username not in data:
            self.savename(username,password)
      

    def loging(self,username,password):
      return 'hello {}. Your password is {}'.format(username,password)
    def savename(self, username,password):
        global data
        data.append({'user':username, 'password':password})
        with open(filename, "w") as file:
            json.dump(data, file)



cherrypy.server.socket_host = "0.0.0.0"
if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())