arquivo_contatos = open('PythonAlura\PythonIO\dados\contatos-escrita.csv',encoding='latin_1', mode  ='a')

contato = '11,Camila,camila@camila.com\n'

arquivo_contatos.write(contato)