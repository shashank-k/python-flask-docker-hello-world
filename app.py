import socket
from flask import Flask

app = Flask(__name__)

@app.route("/")
def return_hostname():
    return "Hello World from {} and my IP address is {}".format(socket.gethostname(), socket.gethostbyname(socket.gethostname()) )

if __name__ == "__main__":
    app.run(host='0.0.0.0')