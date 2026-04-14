import math

def numero_de_moleculas(A=6.02214076 * math.pow(10, 23)):

	print('Forneça os seguintes dados: \n')
	print('Densidade em kg por metro cúbico: ')
	d = float(input('Densidade: '))
	print('Massa molar da sua substância em kg/mol: ')
	MM = float(input('Massa molar: '))
	print('Volume da caixa em nm cúbicos (Informe o volume do seu objeto): ')
	V = float(input('Volume: '))

	print('--------------------------------------------------')
	print('Informe a quantidade de partículas que você gostaria (alternativa)')
	n = float(input('Quantidade de partículas: '))

	N = ((V * math.pow(10,-27)) * A * d) / MM

	V2 = (n * MM) / (A * d)

	print('\n')
	print(f'Número de moléculas para {round(V, 4)} nm3 com densidade de {round(d, 4)} kg/m3 e massa molar {round(MM, 4)} kg/mol: {round(N, 4)} moléculas')
	print('\n')
	print(f'Volume necessário para {round(n, 4)} moléculas com densidade de {round(d, 4)} kg/m3 e massa molar {round(MM, 4)} kg/mol: {round(V2 * math.pow(10, 27), 4)} nm3')
	print('\n')

	a = math.pow(V2 * math.sqrt(2) * math.pow(10, 27), 1/3)

	b = math.pow(V2 * math.pow(10,27), 1/3)

	print(f'Para {n} moléculas: ')
	print(f'Caso seja um dodecaedro: {round(a, 4)} --> Para definir a "caixa dodecaédrica" no GROMACS')
	print(f'Caso seja um cubo: {round(b, 4)} --> Para definir a "caixa cúbica" no GROMACS')
	print('\n')

numero_de_moleculas()
