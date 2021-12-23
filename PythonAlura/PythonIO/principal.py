import contato_utilis

try:
    # contatos = contato_utilis.csv_para_contatos('PythonAlura\PythonIO\dados\contatos.csv','latin_1')
    # contato_utilis.contato_para_pickle(contatos,'PythonAlura\PythonIO\dados\contatos.pickle' )
    
    # contatos = contato_utilis.pickle_para_contatos('PythonAlura\PythonIO\dados\contatos.pickle')
    # contato_utilis.contatos_para_json(contatos,'PythonAlura\PythonIO\dados\contatos.json' )

    contatos = contato_utilis.json_para_contato('PythonAlura\PythonIO\dados\contatos.json')
    
    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')


except FileNotFoundError:
    print('arquivo não encontrado')
