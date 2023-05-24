from fastapi import FastAPI

app = FastAPI()

# Rota para a página inicialde
@app.get('/')
def home():
    return {'message': 'Bem-vindo à API básica!'}

# Rota para retornar um JSON com dados
@app.get('/api/dados')
def get_dados():
    dados = {
        'nome': 'João',
        'idade': 25,
        'cidade': 'São Paulo'
    }
    return dados

# Rota para receber dados via POST e retornar uma resposta
@app.post('/api/receber')
def receber_dados(dados: dict):
    nome = dados['nome']
    mensagem = f'Olá, {nome}! Dados recebidos com sucesso.'
    return {'mensagem': mensagem}