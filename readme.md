# Consumir recursos da AWS utilizando o SDK boto3

Este script tem como objetivo consumir os dados do EC2 (listar, stop e start)

## Deploy

Para fazer o deploy na sua máquina e utilizar como exemplo, siga o passo a passo a seguir.

- Clone o repositório.

```bash
git clone https://github.com/leandro-matos/python-script-boto3
```

- Acesse o diretório

```bash
cd python-script-boto3
```

- Crie uma virtual env

```bash
python3 -m venv .venv
```

- Ative a virtual env

```bash
source .venv/bin/activate
```

- Instale as bibliotecas

```bash
pip install -r requirements.txt
```

Incluir as configurações da AWS utilizando o comando: aws-configure

```bash
* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* AWS_DEFAULT_REGION
```
Mais informações na documentação: https://boto3.amazonaws.com/v1/documentation/api/1.9.42/guide/configuration.html