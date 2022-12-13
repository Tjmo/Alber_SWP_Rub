from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

score = {}


class SimpleNameScore(Resource):
    def get(self, name=""):
        if name in score:
            return {name: score[name]}
        if name == "":
            return {score}
        return {"Message": "Nicht vorhanden"}

    def put(self, name):
        existing = name in score
        score[name] = request.form['score']
        if existing:
            return {"Message": "Überschrieben"}
        return {"Message": "Neu hinzugefügt"}

    def delete(self, name):
        del score[name]
        return {"Message": "%s gelöscht" % name}

    def patch(self, name):
        score[name] = request.form['score']
        return {"Message": "%s gepatched" % name}


api.add_resource(SimpleNameScore, '/score/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)