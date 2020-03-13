import random
import string
import json
import os
import cherrypy



filename = "user.json"
data=[]


class WebApp(object):
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
              <form method="get" action="signin" >
                <p> Username 
                  <input type="text" value="" name="username" />
                  
                </p>
                <p> Password 
                  <input type="text" value="" name="password" />
                  
                </p>
                              
                <button type="submit">Log in</button>
              </form>
            </body>
          </html>"""

    @cherrypy.expose
    def signin(self, username="",password=""):
      with open(filename, "r") as file:
        data = file.read()
      if username != "" and password !="" and username in data and password in data:
        
        return 'welcome back {}!.'.format(username)

      elif username !="" and password !="" and username not in data:
          self.savename(username,password)
          return 'welcome {}. Your account has been created with this password {}'.format(username,password)
      else:
          self.index()  
         
          

    
    def savename(self, username,password):
        #global data
        data.append({'user':username, 'password':password})
        with open(filename, "w") as file:
            json.dump(data, file)



cherrypy.server.socket_host = "0.0.0.0"
if __name__ == '__main__':
    cherrypy.quickstart(WebApp())