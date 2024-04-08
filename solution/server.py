from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class guess:
    _instance = None
    _instance.id = 1
    def __new__(cls,id, player, status) :
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.id = id
            cls._instance.player = player
            cls._instance.number = 50
            cls._instance.attempts = []
            cls._instance.status = status
        return cls._instance
    
    def to_dict(self):
        return {"id": self.id , "player": self.player, "number": self.number, "attempts": self.attepmts, "status": self.status}
    
    def realice_attepmt(self, number, attempts ):
        number = self.number
        attempts = self.attempts
        for i in attempts:
            if (number < i):
                print("el numero a adivinar es mayor")
            elif(number > i):
                print("el numero a adivinar es menor")
            else:
                print("felicitaciones has adiinado el numero")
    
        

class GuessHandler(BaseHTTPRequestHandler):
    def handle_response(self, data):
        self.send_response(data)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        return self

    def do_GET(self):
        if self.path == "/guess":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            guess_data = json.dumps(guess.to_dict())
            self.wfile.write(guess_data.encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/guess/":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            number = json.loads(post_data.decode("utf-8"))["number"]
            attempts = json.loads(post_data.decode("utf-8"))["attempts"]
            guess.realice_attepmt(number, attempts)
            self.send_response(201)
            self.end_headers()
            player_data = json.dumps(guess.to_dict())
            self.wfile.write(player_data.encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

def run():
    global guess
    guess = 1
    try:
        server_address = ('', 8000)
        httpd = HTTPServer(server_address, GuessHandler )
        print("Iniciando servidor en: http://localhost:8000")
        httpd.serve_forever()
    except KeyboardInterrupt: 
        httpd.socket.close()

if __name__ == "_main_":
    run()