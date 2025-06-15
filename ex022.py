    # Crie um programa que leia o nome completo de uma pessoa e mostre:
    # O nome com todas as Letras maiúsculas e minúsculas;

    # Quantas letras ao todo (sem considerar espaços);

    #Quantas letras tem o primeiro nome.
    nome_completo = str(input('Digite o nome competeto: '))
    primeiro_nome = nome_completo.split()[0]
    print('O nome em maiúsculas é: ', nome_completo.upper())
    print('O nome em minúsculas é: ', nome_completo.lower()) 
    print('O nome tem ao todo {} letras'.format(len(nome_completo.replace(' ', ''))))
    print('O primeiro nome é: {}'.format(primeiro_nome))   
    print('O primeiro nome tem {} letras'.format(len(primeiro_nome)))
    