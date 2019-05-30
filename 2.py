import cherrypy
class HelloWorld():
        @cherrypy.expose
        def index(self):
            return "Hello CherryPi!"
        @cherrypy.expose
        def sayHello(self,myFriend='my friend'):
            return "Hello "+ myFriend
class StaticPage():
        @cherrypy.expose
        def index(self):
            return open('E://106/12/Heart/Heart/index.html')
#cherrypy.config.update({'server.socket_port':8985})
cherrypy.quickstart(StaticPage())