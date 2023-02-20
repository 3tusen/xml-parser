#imports
import xml.sax

#class
class PeopleHandler(xml.sax.ContentHandler):

    def startElement(self, name, attrs):
        self.current = name
