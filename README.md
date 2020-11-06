# DESAFIO ELOGROUP 2020/2 - SISTEMA BACKEND

Esse repositório contém o código de resposta para o Desafio proposto pela EloGroup descrito no arquivo pdf.

Para utilizá-lo é necessário:
    Python 3
    venv
    mysql

## Criando a venv
    No Windows:
        Abra o terminal cmd e entre na pasta do projeto:
            C:\> cd [SUA PASTA]\desafio_elogroup
        Cria a venv com o comando:
            C:\> pyhton3 -m venv venv
        Ative a venv com o comando:
            C:\> <venv>\Scripts\activate.bat

## Instalando os Pre-requisitos
    Uma vez a venv ativada, instale os requisitos necessários para o programa:
        C:\> pip install -r requirements.txt

## O Sistema

### Migrando e populando o banco
    Para a migração do banco dados deve ser feita através do comando
        C:\> python3 manage.py migrate db

    Os status das leads são fixos e é importante criá-los antes da criação de qualquer lead.

    Para isso

### Para rodar

    Para rodar é só estar na pasta raíz do projeto e digita o que se segue:
        C:\> python3 manage.py run

    Abra o seu navegador de preferencia e entre em 127.0.0.1/5000
    Lá, aparecerá todas as funcionalidades proporcionadas pela API

#### Usando as funções
    Na aba user, clique no método post e crie o seu usuário através do "Try out"
    No campo payload, substitua os valores "string" pelo seu "user" e "password" e clique em Execute.

    Clique na aba auth, e faça o login usando o mesmo comando Try out. Digite os valores usados para criar o seu usuario
anteriormente e clique em execute.  A mensagem de resposta trará um campo com nome Authorization. Copie o conteudo de authorization sem
as aspas. Clique no botão Authorize no canto superior esquerdo da janela e cole o valor no campo Value e clique em Authorize.
