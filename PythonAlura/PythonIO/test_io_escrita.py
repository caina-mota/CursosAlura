arquivo = open('PythonAlura\PythonIO\dados\contatos-escrita.csv',encoding='latin_1',mode='a+')

print(type(arquivo))

conteudo = arquivo.buffer.read()
# print(conteudo)
# texto_em_bytes = b'texto em bytes'
texto_em_bytes = bytes('É um texto em bytes', 'latin_1')
# print(texto_em_bytes)
# print(type(texto_em_bytes))

contato = bytes('12,Anali,anali@anali.com\n', encoding='latin_1')
arquivo.buffer.write(contato)

arquivo.close()