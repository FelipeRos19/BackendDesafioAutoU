Backend Desafio AutoU

Bem-vindo ao repositório do desafio backend da AutoU!

📦 Tecnologias Utilizadas

Python: Linguagem principal do projeto.

FastAPI: Framework para criação de APIs RESTful.

Docker: Containerização da aplicação.

Outras dependências: Definidas no arquivo requirements.txt.

⚙️ Pré-requisitos

Antes de rodar o projeto, assegure-se de ter as seguintes ferramentas instaladas:

Python 3.8+

Docker

🛠️ Instalação e Execução
1. Clonar o repositório
git clone https://github.com/FelipeRos19/BackendDesafioAutoU.git
cd BackendDesafioAutoU

2. Criar e ativar um ambiente virtual (opcional, mas recomendado)
```
python -m venv venv
```
# No Windows:
```
venv\Scripts\activate
```
# No macOS/Linux:
```
source venv/bin/activate
```

3. Instalar as dependências
```
pip install -r requirements.txt
```

4. Rodar a aplicação
```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Por padrão, a API estará disponível em http://127.0.0.1:5000.

5. Usando Docker (alternativa)

Se preferir, é possível rodar a aplicação utilizando Docker:
```
docker build -t backend-desafio-autou .
docker run -p 5000:5000 backend-desafio-autou
```


A API estará disponível em http://localhost:5000.


📁 Estrutura do Projeto
```
├── main.py               # Ponto de entrada da aplicação
├── requirements.txt      # Dependências do projeto
├── Dockerfile            # Arquivo para construção da imagem Docker
├── routes/               # Definição das rotas da API
├── middlewares/          # Middlewares personalizados
└── preprocessing/        # Funções de pré-processamento
```