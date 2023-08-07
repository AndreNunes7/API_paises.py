import json
import sys

import requests


url_all = "https://restcountries.com/v3.1/all"
URL_Name = "https://restcountries.com/v3.1/name/"


def requisicao(url):
    try:
        resposta = requests.get(url)

        if resposta.status_code == 200:
            return resposta.text
    except:
        print("Erro ao fazer requisição em:", url)
    return None



def parsing(texto):
    try:
        return json.loads(texto) # PARSING DE JSON PARA PYTHON
    except:
        print("Erro ao fazer o pasing")


def contagem_de_paises():
    resposta = requisicao(url_all)
    
    if resposta:
        lista_paises = parsing(resposta)
        if lista_paises:
            return len(lista_paises)




def listar_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais['name']['common'])



def mostrar_populacao(nome_do_pais):
    resposta = requisicao(f"{URL_Name}/{nome_do_pais}")
    
    if resposta:
        lista_de_paises = parsing(resposta)

        if lista_de_paises:
            for pais in lista_de_paises:
                print(f"{pais['name']['common']}: {pais['population']} habitantes ")
    else:
        print("Pais não encontrado")
    


def mostrar_moedas(nome_pais):
    resposta = requisicao(f"{URL_Name}/{nome_pais}")
    
    if resposta:
        lista_de_paises = parsing(resposta)

        if lista_de_paises:
            for pais in lista_de_paises:
                moedas = pais.get('currencies')
                if moedas:
                    for codigo, info_moeda in moedas.items():
                        name = info_moeda.get('name')
                        symbol = info_moeda.get('symbol')
                        print(f"Moeda: {name} - Símbolo: {symbol}")
                else:
                    print("Moedas não encontradas para o país.")
    else:
        print("País não encontrado")
    

def ler_nome_do_pais():
    try:
        nome_do_pais = argumento2 = sys.argv[2]
        return nome_do_pais
    except:
        print("É Preciso passar o nome do país")


if __name__ == "__main__":

    
    # texto = requisicao(url_all)
    # if texto:
    #     texto_parsing = parsing(texto)
    #     if texto_parsing:
    #         print(contagem_de_paises(texto_parsing))
    #         print(listar_paises(texto_parsing))

    
   #mostrar_populacao('brazil')
   #mostrar_moedas('bra')   

    if len(sys.argv) == 1:
        print("## Bem vindo ao sistema de páises ##")
        print("Uso: python API_paises.py <açao> <nome do páis>")
        print("Ações: \n contagem, moeda, populacao")
    else:
        argumento1 = sys.argv[1]

        if argumento1 == "contagem":
            numero_de_paises = contagem_de_paises()
            print(f"Existem {numero_de_paises} países no mundo todo")
            exit(0)

        elif argumento1 == "moeda":
            try:
                pais = ler_nome_do_pais()
                if pais:
                    mostrar_moedas(pais)

            except:
                print("É preciso passar o nome do país")


        elif argumento1 == "populacao":
            pais = ler_nome_do_pais()
            if pais:
                mostrar_populacao(pais)
  
        else:
            print("Argumento inválido")
            exit(0)


        
