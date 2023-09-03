Eventif
Sistema do evento do IF que está sendo desenvolvido na disciplina de Desenvolvimento de Sistemas 2.

Como desenvolver

Clone o repositório

Crie um virtualenv com python 3.10 ou superior

Ative o virtualenv

Instale as dependências

Configure a instância com o arquivo .env



Execute os testes

git clone git@github.com:XeanG/eventif

cd eventif

python -m venv .eventif

source .eventif/bin/activate

pip install -r requirements.txt

cp contrib/env-sample .env

python manage.py test
