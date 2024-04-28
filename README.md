# Pokedex
# Sobre o projeto
O projeto Pokedex é uma aplicação web construída ao longo de um desafio proposto em sala, durante a disciplina de estrutura de dados.

A aplicação consiste em uma ferramenta para pesquisa de pokemóns, utilizando os devidos meios para criar uma interface intuitiva e diferentes modelos de pokemóns a ser visualizados.

## Layout web
![Web 1] (https://github.com/rafaelfr66/Pokedex/blob/main/projetopokedex/templates/index.html)
![Web 2] (https://github.com/rafaelfr66/Pokedex/blob/main/projetopokedex/templates/nopokemon.html)
![Web 3] (https://github.com/rafaelfr66/Pokedex/blob/main/projetopokedex/templates/pokemon.html)

# Tecnologias utilizadas
## Back end
- Python
- Flask

## Front end
- HTML
- CSS

# Como executar o projeto

Pré-requisitos: 

Python 3.10 ou superior;
Pip 23.2 ou superior;
Flask 3.0 ou superior.

## Linux
```bash
# clonar repositório
git clone https://github.com/devsuperior/sds1-wmazoni

# entrar na pasta do projeto
cd pokedex/projetopokedex

# Criar ambiente virtual
python3 -m venv venv

# Instalar o flask 
pip install flask

# ativar o ambiente virtual
source venv/bin/activate

# definindo aplicação principal do flask
export FLASK_APP=main.py

# executar o projeto Flask localmente
xdg-open http://127.0.0.1:5000
flask run
```

## Windows
```batch

# Criar ambiente virtual:
python -m venv venv

# Instalar o Flask:
pip install flask

# Ativar o ambiente virtual:
venv\Scripts\activate

# Definir a aplicação principal do Flask:
set FLASK_APP=main.py

# Executar o projeto Flask localmente:
start http://127.0.0.1:5000
flask run
```

# Autor

Rafael Franklin Gomes Cruz

https://www.linkedin.com/in/rafaelfranklingomes/
