from flask import Flask, render_template, request, make_response
import utils
import settings
from string import ascii_uppercase
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def game():
    remaining_tries = settings.DEFAULT_AVAILABLE_GUESSES
    wrong_letters = []
    game_solved = False
    # while remaining_tries and not game_solved:
    guessed_char = request.args.get('guess')
    game_word = request.cookies.get('game_word') or utils.get_random_word().upper()
    print(game_word)

    if not guessed_char:
        boolean_list = [False for char in game_word]
    else:
        if guessed_char in game_word:
            index = game_word.index(guessed_char)
            boolean_list = [False for char in game_word]
            boolean_list[index] = True

    displayed_word = utils.get_displayed_word(game_word, boolean_list)

    data = {'displayed_word': displayed_word, 'word_length': len(game_word)}
    response = make_response(render_template('hangman_base.html', data=data))
    # clue = utils.get_word_meaning(game_word)

    if not game_word:
        response.set_cookie('game_word', game_word)
    return response


if __name__ == '__main__':
    app.run()
