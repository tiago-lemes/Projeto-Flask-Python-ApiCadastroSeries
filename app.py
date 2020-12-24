from flask import Flask, request, jsonify
from data import alchemy
from model import show, episode

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = "chavesupersecreta"

@app.before_first_request
def create_tables():
    alchemy.create_all()


@app.route('/', methods=['GET'])
def home():
    return "API retorno - Hello World", 200


@app.route('/showall', methods=['GET'])
def get_all_shows():
    result = show.ShowModel.find_all()
    print("result")
    print([show.json() for show in result])
    if result:
        return jsonify([show.json() for show in result])
    else:
        return jsonify([])
    

@app.route('/show', methods=['POST'])
def create_show():
    request_data = request.get_json()
    new_show = show.ShowModel(request_data["name"])
    new_show.save_to_db()
    #print("NOVO ID: {0}".format(new_show.id))

    result = show.ShowModel.find_by_id(new_show.id)

    return jsonify(result.json())


@app.route('/show/<string:name>', methods=['GET'])
def get_show_by_id(name):
    result = show.ShowModel.find_by_name(name)

    if result:
        return result.json()
    else:
        return {"message":"Série não encontrada"}, 404


@app.route('/show/<int:id>', methods=['GET'])
def get_show_by_name(id):
    result = show.ShowModel.find_by_id(id)

    if result:
        return result.json()
    else:
        return {"message":"Série não encontrada"}, 404


@app.route('/show/<int:id>', methods=['DELETE'])
def delete_show(id):
    show_deleted = show.ShowModel.find_by_id(id)

    if show_deleted:
        show_deleted.delete_from_db()
        return {"message":"série excluída"}, 202
    else:
        return {"message":"Série não encontrada"}, 404        


@app.route('/show/<int:id>/episode', methods=['POST']) 
def create_episode_in_show(id):
    request_data = request.get_json()

    for item in request_data:

        parent = show.ShowModel.find_by_id(id)

        if parent:
            new_episode = episode.EpisodeModel(name = item["name"], season = item["season"], show_id = parent.id)
            new_episode.save_to_db()
           # return new_episode.json()
        else:
            return {"message":"Série não encontrada"}, 404

    return show.ShowModel.find_by_id(id).json()

if __name__ == "__main__":
    from data import alchemy
    alchemy.init_app(app)
    app.run(port=5555, debug=True)