arquivo = open('PythonAlura\PythonIO\dados\contatos.csv',encoding='latin_1')

print(type(arquivo))

conteudo = arquivo.buffer.read()
# print(conteudo)
# texto_em_bytes = b'texto em bytes'
texto_em_bytes = bytes('É um texto em bytes', 'latin_1')
print(texto_em_bytes)
print(type(texto_em_bytes))

arquivo.close()