import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

caminhoArquivoVest ="F:/Users/amand/Documentos/Projetos/DataVizProj/ENEM_Vestibulandos.csv"
VestibulandosDf = pd.read_csv(caminhoArquivoVest, sep=',', encoding='latin-1')

# Define a função para formatar os rótulos como porcentagem
def porcentagem_formatter(x,pos):
    return '{:.0f}%'.format(x * 100)

# Separando os dataframes por escolaridade das mães
def defineEscolarizacao(nivel):
    if nivel in ('A', 'B', 'C', 'D'):
        return '1'
    elif nivel == 'E':
        return '2'
    elif nivel in ('F', 'G'):
        return '3'
    else:
        return '4'


# Seleciona colunas relevantes
NotasDf = VestibulandosDf[['TP_ESCOLA', 'Q002', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO', 'MEDIA_NOTAS']]


# Separando os dataframes por tipo de escola
escola2 = NotasDf[NotasDf['TP_ESCOLA'] == 2]
escola3 = NotasDf[NotasDf['TP_ESCOLA'] == 3]

# Criando o histograma para a escola 2
plt.hist(escola2['MEDIA_NOTAS'], bins=30, alpha=0.5, density=True, label='Escola pública')

# Criando o histograma para a escola 3
plt.hist(escola3['MEDIA_NOTAS'], bins=30, alpha=0.5, density=True, label='Escola privada')

# Configurando o gráfico
plt.xlabel('Médias')
plt.ylabel('Volume')
plt.title('Influência do Tipo de Ensino')
plt.legend()

# Exibindo o gráfico
plt.show()
plt.savefig('InfluenciaTipoEnsino.png')


NotasDf['Q002'] = NotasDf['Q002'].apply(defineEscolarizacao)
paisFund = NotasDf[NotasDf['Q002'] == '1']
paisMedio = NotasDf[NotasDf['Q002'] =='2']
paisSuperior = NotasDf[NotasDf['Q002'] =='3']

# Criando o histograma para a escola 2
plt.hist(paisFund['MEDIA_NOTAS'], bins=30, alpha=0.5, density=True, label='Não concluiu o ensino médio')

# Criando o histograma para a escola 3
plt.hist(paisMedio['MEDIA_NOTAS'], bins=30, alpha=0.5, density=True, label='Ensino médio concluído')

# Criando o histograma para a escola 3
plt.hist(paisSuperior['MEDIA_NOTAS'], bins=30, alpha=0.5, density=True, label='Possui graduação/pós')

# Configurando o gráfico
plt.xlabel('Média')
plt.ylabel('Volume')
plt.title('Influência da Escolaridade das Mães')
plt.legend()

# Exibindo o gráfico
plt.show()
plt.savefig('InfluenciaEscolaridadeMaes.png')
possui_internet = VestibulandosDf[VestibulandosDf['Q025'] == 'A']
nao_possui_internet = VestibulandosDf[VestibulandosDf['Q025'] == 'B']

bins = 20

# Calculando as densidades para cada grupo
densidade1, bins1, _ = plt.hist(possui_internet['MEDIA_NOTAS'], bins=bins, alpha=0.5, density=True)
densidade2, bins2, _ = plt.hist(nao_possui_internet['MEDIA_NOTAS'], bins=bins, alpha=0.5, density=True)

# Convertendo a densidade em porcentagem
total1 = possui_internet.shape[0]
total2 = nao_possui_internet.shape[0]
largura_bin = bins1[1] - bins1[0]
porcentagem1 = densidade1 / (total1 * largura_bin) * 100
porcentagem2 = densidade2 / (total2 * largura_bin) * 100

# Plotando os histogramas com as densidades em porcentagem
plt.bar(bins1[:-1], porcentagem1, width=largura_bin, alpha=0.5, label='Possui internet')
plt.bar(bins2[:-1], porcentagem2, width=largura_bin, alpha=0.5, label='Não possui internet')

plt.xlabel('Média')
plt.ylabel('Volume')
plt.title('Influência do Acesso à Internet')
plt.legend(loc='upper right')

plt.show()
plt.savefig('InfluenciaAcessoInternet.png')