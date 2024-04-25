from flask import Flask
from view.game_view import gameView
from view.playerGame_view import playerGameView

app = Flask(__name__)
# app.config['DATABASE'] = os.path.join(os.path.dirname(__file__), "model", "NLG.sqlite")

app.register_blueprint(gameView)
app.register_blueprint(playerGameView)


@app.route("/")
def index():
    return "<center><h1>HOME PAGE</h1></center>"


if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
