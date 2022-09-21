nome = input('Digite seu nome completo ')
print('O nome digitado foi: {}'.format(nome))
print('Nome com todas letras maiusculas: {} '.format(nome.upper()))
print('Nome com todas letras minusculas: {}'.format(nome.lower()))
dividido = nome.split()
print('O primeiro nome é: {}'.format(dividido[0]))
espaço = nome.replace(' ', '')
print('O nome: {} possui {} letras'.format(nome, len(espaço)))



