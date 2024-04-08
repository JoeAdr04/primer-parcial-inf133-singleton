from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import random

class Partida:
    _instance = None

    def __new__(cls,id, player, number, status) :
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.id = id
            cls._instance.player = player
            cls._instance.number = number
            cls._instance.attempts = []
            cls._instance.status = status
        return cls._instance
    
    def to_dict(self):
        return {"player": self.id , "palyer": self.player, "number": self.number, "attempts": self.attepmts, "status": self.status}
    
    def realice_attepmt(self, number, attempts ):
        number = random(1,100)
        attempts = self.attempts
        for i in range


class PartidaHandler(BaseHTTPRequestHandler):
    def do_GET(self):















def run():
    global Partida
    Partida = 1
    try:
        server_address = ('', 8000)
        httpd = HTTPServer(server_address, PartidaHandler )
        print("Iniciando servidor en: http://localhost:8000")
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.socket.close()

if __name__ == "_main_":
    run()