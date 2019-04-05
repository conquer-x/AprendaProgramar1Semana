#!/usr/bin/python
# -*- coding: latin-1 -*-
#
# ConquerX: Introducao a programacao - Python
# Exemplo de servidor rest API. Um servidor que salvará notas de um usuário
# Usa o https://www.flaskapi.org/
from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

# cria uma instancia do servidor
app = FlaskAPI(__name__)

# configura o modo de segurança
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)


# para não usar banco de dados, usaremos esta estrutura de arquivos
notes = {
    0: 'do the shopping',
    1: 'build the codez',
    2: 'paint the door',
}

def note_repr(key):
    return {
        'url': request.host_url.rstrip('/') + url_for('notes_detail', key=key),
        'text': notes[key]
    }


@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), status.HTTP_400_BAD_REQUEST

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), status.HTTP_400_BAD_REQUEST
    if not password:
        return jsonify({"msg": "Missing password parameter"}), status.HTTP_400_BAD_REQUEST

    if username != 'test' or password != 'test':
        return jsonify({"msg": "Bad username or password"}), status.HTTP_401_UNAUTHORIZED

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), status.HTTP_200_OK


@app.route('/auth')
def authRouteHandler():
    """
    Controle de senha. Ira simplesmente fazer o retorno do usuário e senha
    """
    # ret = request.headers.get('authorization')
    password = request.authorization['password']
    usario = request.authorization['username']

    return jsonify(user=usario, password=password)

@app.route("/", methods=['GET'])
def notes_list():
    """
    lista ou cria as notas
    """
    # verifica se é o método post
    if request.method == 'POST':
        # busca o texto de um campo text
        note = str(request.data.get('text', ''))
        idx = max(notes.keys()) + 1
        notes[idx] = note
        return note_repr(idx), status.HTTP_201_CREATED

    # request.method == 'GET'. Busca a informação somente
    return [note_repr(idx) for idx in sorted(notes.keys())]

@app.route("/notes/", methods=['POST'])
@jwt_required
def notes_create():
    """
    lista ou cria as notas
    """
    # busca o texto de um campo text
    note = str(request.data.get('text', ''))
    idx = max(notes.keys()) + 1
    notes[idx] = note
    return note_repr(idx), status.HTTP_201_CREATED


@app.route("/notes/<int:key>/", methods=['GET'])
def notes_detail(key):
    """
    Faz um update, deleta ou busca uma nota em específico
    """

    # método para salvar/atualizar
    if request.method == 'PUT':
        note = str(request.data.get('text', ''))
        notes[key] = note
        return note_repr(key)

    elif request.method == 'DELETE':
        # apaga as notas
        notes.pop(key, None)
        return '', status.HTTP_204_NO_CONTENT

    # busca as notas
    if key not in notes:
        raise exceptions.NotFound()
    return note_repr(key)

@app.route("/notes/<int:key>/", methods=['PUT', 'DELETE'])
@jwt_required
def notes_detail_change(key):
    """
    Faz um update, deleta ou busca uma nota em específico
    """

    # método para salvar/atualizar
    if request.method == 'PUT':
        note = str(request.data.get('text', ''))
        notes[key] = note
        return note_repr(key)

    elif request.method == 'DELETE':
        # apaga as notas
        notes.pop(key, None)
        return '', status.HTTP_204_NO_CONTENT

    # busca as notas
    if key not in notes:
        raise exceptions.NotFound()
    return note_repr(key)


# Protect a view with jwt_required, which requires a valid access token
# in the request to access.
@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


if __name__ == "__main__":
    """
    Roda a aplicação em modo debug
    """
    app.run(debug=True)
