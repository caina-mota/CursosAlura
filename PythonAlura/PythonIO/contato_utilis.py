import csv, pickle, json
from contato import Contato

def csv_para_contatos(caminho, encode='latin_1'):
    contatos= []
    with open(caminho, encoding=encode) as arquivo:
        leitor = csv.reader(arquivo) #le o arquivo CSV e monta uma lista

        for linha in leitor:
            id=linha[0]
            nome = linha[1]
            email = linha[2]
            #id, nome, email = linha

            contato = Contato(id,nome,email)
            contatos.append(contato)
    
    return contatos

def contato_para_pickle(contatos, caminho):
    with open(caminho, mode='wb') as arquivo:
        pickle.dump(contatos, arquivo)

def pickle_para_contatos(caminho):
    with open(caminho, mode='rb') as arquivo:
        contatos = pickle.load(arquivo)
    return contatos

def contatos_para_json(contatos, caminho):
    with open(caminho, mode='w') as arquivo:
        json.dump(contatos, arquivo, default=_contato_para_json) 

def _contato_para_json(contato):
    return contato.__dict__

def json_para_contato(caminho):
    contatos= []
    with open(caminho, mode='rb') as arquivo:
        contatos_json = json.load(arquivo)

        for contato in contatos_json:
            #c = Contato(contato['id'], contato['nome'],contato['email'])
            c = Contato(**contato) #ja que o inicializador e as chaves do dicionario tem oi mesmo nome, pode-se passar desta forma
            contatos.append(c)

    return contatos
