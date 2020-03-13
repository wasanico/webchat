import cherrypy
import socket

print(socket.gethostbyname(socket.gethostname()))
class WebApp():
    @cherrypy.expose
    def index(self):
        return '<b>YYOOOOOOOOOOOOOOOOOOOOOO<b>!'
cherrypy.server.socket_host = "0.0.0.0"
cherrypy.quickstart(WebApp())

""" Pour se connecter depuis un autre pc : ipadress:8080"""