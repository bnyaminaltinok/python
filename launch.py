from flask import Flask
from flask import jsonify
helloworld = Flask(__name__)

veri = {
  okkkkk
}

healtcheck = {

okk

}


@helloworld.route("/veri")
def run():
    return jsonify(veri)
if __name__ == "__main__":
    helloworld.run(host="0.0.0.0", port=int("5002"), debug=True)

@helloworld.route("/healtcheck")
def run():
    return jsonify(healtcheck)
if __name__ == "__main__":
    helloworld.run(host="0.0.0.0", port=int("5001"), debug=True)
