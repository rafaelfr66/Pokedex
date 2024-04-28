#!/usr/bin/env python


#Framework flask para rotas e formulários.
from flask import Flask, request, render_template
app = Flask(__name__)


#Rota que retorna para a página home, utilizada nos botões de retorno.
@app.route('/home_page', methods=['POST'])
def home():
    return render_template('index.html')


#Rota inicial do software
@app.route('/')
def index():
    return render_template('index.html')


#Lista de pokemóns, uma espécie de database
pokemons = [
    {
        "nome": "pikachu",
        "tipo": "Elétrico",
        "hp": 35,
        "ataque": 55,
        "defesa": 40,
        "velocidade": 90,
        "imagem": "static/pikachu.jpg"  # Caminho da imagem para Pikachu em formato jpg
    },
    {
        "nome": "charmander",
        "tipo": "Fogo",
        "hp": 39,
        "ataque": 52,
        "defesa": 43,
        "velocidade": 65,
        "imagem": "static/charmander.jpg"  # Caminho da imagem para Charmander em formato jpg
    },
    {
        "nome": "bulbasaur",
        "tipo": "Planta",
        "hp": 45,
        "ataque": 49,
        "defesa": 49,
        "velocidade": 45,
        "imagem": "static/bulbasaur.jpg"  # Caminho da imagem para Bulbasaur em formato jpg
    },
    {
        "nome": "squirtle",
        "tipo": "Água",
        "hp": 44,
        "ataque": 48,
        "defesa": 65,
        "velocidade": 43,
        "imagem": "static/squirtle.jpg"  # Caminho da imagem para Squirtle em formato jpg
    },
    {
        "nome": "jigglypuff",
        "tipo": "Normal",
        "hp": 115,
        "ataque": 45,
        "defesa": 20,
        "velocidade": 20,
        "imagem": "static/jigglypuff.jpg"  # Caminho da imagem para Jigglypuff em formato jpg
    },
    {
        "nome": "mewtwo",
        "tipo": "Psíquico",
        "hp": 106,
        "ataque": 110,
        "defesa": 90,
        "velocidade": 130,
        "imagem": "static/mewtwo.jpg"  # Caminho da imagem para Mewtwo em formato jpg
    },
    {
        "nome": "dragonite",
        "tipo": "Dragão",
        "hp": 91,
        "ataque": 134,
        "defesa": 95,
        "velocidade": 80,
        "imagem": "static/dragonite.jpg"  # Caminho da imagem para Dragonite em formato jpg
    },
    {
        "nome": "gyarados",
        "tipo": "Água",
        "hp": 95,
        "ataque": 125,
        "defesa": 79,
        "velocidade": 81,
        "imagem": "static/gyarados.jpg"  # Caminho da imagem para Gyarados em formato jpg
    },
    {
        "nome": "snorlax",
        "tipo": "Normal",
        "hp": 160,
        "ataque": 110,
        "defesa": 65,
        "velocidade": 30,
        "imagem": "static/snorlax.jpg"  # Caminho da imagem para Snorlax em formato jpg
    },
    {
        "nome": "machamp",
        "tipo": "Lutador",
        "hp": 90,
        "ataque": 130,
        "defesa": 80,
        "velocidade": 55,
        "imagem": "static/machamp.jpg"  # Caminho da imagem para Machamp em formato jpg
    },
    {
        "nome": "alakazam",
        "tipo": "Psíquico",
        "hp": 55,
        "ataque": 50,
        "defesa": 45,
        "velocidade": 120,
        "imagem": "static/alakazam.jpg"  # Caminho da imagem para Alakazam em formato jpg
    },
    {
        "nome": "arcanine",
        "tipo": "Fogo",
        "hp": 90,
        "ataque": 110,
        "defesa": 80,
        "velocidade": 95,
        "imagem": "static/arcanine.jpg"  # Caminho da imagem para Arcanine em formato jpg
    },
    {
        "nome": "gengar",
        "tipo": "Fantasma",
        "hp": 60,
        "ataque": 65,
        "defesa": 60,
    }
]


#Função para procurar pokemóns na lista acima
def encontrar_pokemon(pokemon):
    for poke in pokemons:
        if poke["nome"] == pokemon:
            return poke  # Retorna o pokémon encontrado
    return None  # Retorna None se o Pokémon não for encontrado

  
@app.route('/get_pokemon', methods=['POST', 'GET'])
def teste():
    nome_pokemon = request.form['pokemon']
    pokemon = encontrar_pokemon(nome_pokemon) 
    if pokemon:
       return render_template('pokemon.html', pokemon=pokemon)
    else:
        return render_template('nopokemon.html')
          

if __name__ == '__main__':
    app.run(debug=True)