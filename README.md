# API de Países - Python

Este é um script Python que utiliza a API de países para obter informações sobre países, incluindo contagem total de países, informações de moedas e população.

## Pré-requisitos

- Python 3.x
- Módulos: `json`, `sys`, `requests`

## Uso

1. Clone este repositório ou faça o download do arquivo `API_paises.py`.
2. Certifique-se de que você tenha os pré-requisitos instalados.
3. Execute o script Python usando a linha de comando:

```sh
python API_paises.py <ação> <nome do país>

## Ações Disponíveis

- `contagem`: Exibe o número total de países no mundo.
- `moeda`: Exibe as informações das moedas de um país.
- `populacao`: Exibe a população de um país.


## Exemplos de Uso

1. Contagem de países:
```sh
python API_paises.py contagem

2. Informações de moedas de um país:
```sh
python API_paises.py moeda brazil

3. População de um país:
```sh
python API_paises.py populacao germany

