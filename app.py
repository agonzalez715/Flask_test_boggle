from flask import Flask, request, render_template, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sammy'
app.debug = True
toolbar = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def home_page():
    """Show the game board."""
    board = boggle_game.make_board()
    session['board'] = board  # Storing the board in session
    return render_template('board.html', board=board)

if __name__ == '__main__':
    app.run(debug=True)
