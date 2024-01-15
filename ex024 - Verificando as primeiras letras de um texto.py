'''Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".'''
cidade = str(input('Digite o nome da sua cidade: ')).strip()
rspt = cidade[:5].upper() == 'SANTO'

print(f'Se a sua cidade conter a plavra "SANTO" no inicio a resposta será "T" de True(Verdadeiro), se não a resposta será "F" de False(Falso): {rspt}')


