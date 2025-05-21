# Projeto Formativo PWBE 

Projeto é uma API desenvolvida para meu projeto Formativo Backend no SENAI "Roberto Mange";
Sua finalidade é realizar o gerenciamento de um sistema escolarç;
Foi desenvolvido em Django com todo carinho 🥰.

# Por onde eu começo?
Primeiramente é necessário ter algumas ferramentas em seu computador.
## 🔧 Ferramentas
- [VSCODE](https://code.visualstudio.com/download)
- [Python 3.9+](https://www.python.org/downloads/)
- [MySQL](https://dev.mysql.com/downloads/windows/installer/8.0.html)
- API CLIENT [Postman](https://www.postman.com/downloads/)

# Passo a passo 😎
Deu tudo certo né? Agora vamos em partes abrir esse projeto!
## ⌨️ 1- Clonando o repositório
- Vá no botão CODE 
- Copie este link: `https://github.com/GiovanaCris/Formativa-PWBE.git`

## 💻 2- Criando o ambiente virtual
- Abra uma pasta no VSCODE
- No terminal crie o ambiente virtual: python -m venv env
- Ative o ambiente virtual com o comando: .\venv\Scripts\activate

## 🔦 3- Instalando as dependências
- Faça o comando: pip install -r requeriments.txt

## 👀 4-  Verificando o banco de Dados
- Vá até a pasta: projeto
- Vá em settings.py
- Procure no código: DATABASES 

````python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cadastro',
        'USER': '#', # Seu usuario do Workbench 
        'PASSWORD': '#', # Suas senha do Workbench 
        'HOST': 'localhost',  # Mysql IP
        'PORT': '3306',  # Porta Mysql      
    }
}
````
- Faça o banco de dados funcionar: 
    CREATE DATABASE cadastro (nome da tabela)
- 🚨 Salve as alterações realizadas: 
      py manage.py makemigrations
      py manage.py migrate 

## 🧔 5- Criando o usuário
- Vá no terminal
- Faça o comando: python manage.py createsuperuser
- Preencha os campos requisitados

## 🎉 6- Rodando o projeto
- No terminal faça o comando: python manage.py runserver

# E você pensa que acabou?
-   Veja a documentação para aprender ainda mais!
- Link documentação: [Clique aqui!](https://documenter.getpostman.com/view/43171648/2sB2qZENTN)
- Agora sim chegamos ao final, parabéns por sua evolução! 🚀