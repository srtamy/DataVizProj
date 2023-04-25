import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

caminhoArquivoVest ="F:/Users/amand/Documentos/Projetos/DataVizProj/ENEM_Vestibulandos.csv"
VestibulandosDf = pd.read_csv(caminhoArquivoVest, sep=',', encoding='latin-1')

# Separando os dataframes por escolaridade dos tutores
def defineEscolarizacao(nivel):
    if nivel in ('A', 'B', 'C', 'D'):
        return 'Não concluiu o EM'
    elif nivel == 'E':
        return 'Concluiu o EM'
    elif nivel in ('F', 'G'):
        return 'Ensino superior ou maior'
    else:
        return 'H'

# Define a função para formatar os rótulos como porcentagem
def porcentagem_formatter(x,pos):
    return '{:.0f}%'.format(x * 100)





VestibulandosDf['Q002'] = VestibulandosDf['Q002'].apply(defineEscolarizacao)
VestibulandosDf['Q001'] = VestibulandosDf['Q001'].apply(defineEscolarizacao)

# Seleciona colunas relevantes com valores relevantes
df = VestibulandosDf.loc[VestibulandosDf['Q001'] != 'H', ['CO_CLASSE', 'Q001', 'NU_INSCRICAO']]

# Calcula proporção de cada nível de escolaridade em cada classe social
df_prop = df.groupby(['CO_CLASSE', 'Q001'])['NU_INSCRICAO'].count() / df.groupby(['CO_CLASSE'])['NU_INSCRICAO'].count()

# Transforma índice em colunas
df_prop = df_prop.unstack()

# Plota gráfico de barras empilhadas
ax = df_prop.plot(kind='bar', stacked=True)

# Define legendas e rótulos dos eixos
ax.set_xlabel('Classe social')
ax.set_ylabel('Proporção')
ax.set_title('Distribuição da Escolaridade dos Pais por Classe Social')

ax.set_xticklabels(ax.get_xticklabels(), rotation=0)

# Cria a legenda personalizada
handles, labels = ax.get_legend_handles_labels()
new_labels = ['Concluiu o EM','Possui no mínimo ES' , 'Não concluiu o EM']

legend = ax.legend(handles=handles, labels=new_labels, title=None)

# Formata os rótulos do eixo y como porcentagens
ax.yaxis.set_major_formatter(mtick.FuncFormatter(porcentagem_formatter))

# Exibe o gráfico
plt.show()
plt.savefig('DistribuiçãoEscolaridadePaisClasseSocial.png')
# Seleciona colunas relevantes
df2 = VestibulandosDf.loc[VestibulandosDf['Q002'] != 'H', ['CO_CLASSE', 'Q002', 'NU_INSCRICAO']]

# Calcula proporção de cada nível de escolaridade em cada classe social
df_prop = df2.groupby(['CO_CLASSE', 'Q002'])['NU_INSCRICAO'].count() / df2.groupby(['CO_CLASSE'])['NU_INSCRICAO'].count()

# Transforma índice em colunas
df_prop = df_prop.unstack()

# Plota gráfico de barras empilhadas
ax = df_prop.plot(kind='bar', stacked=True)

# Define legendas e rótulos dos eixos
ax.set_xlabel('Classe social')
ax.set_ylabel('Proporção')
ax.set_title('Distribuição da Escolaridade das Mães por Classe Social')

ax.set_xticklabels(ax.get_xticklabels(), rotation=0)

# Cria a legenda personalizada
handles, labels = ax.get_legend_handles_labels()
new_labels = ['Concluiu o EM','Possui no mínimo ES' , 'Não concluiu o EM']

legend = ax.legend(handles=handles, labels=new_labels, title=None)

# Formata os rótulos do eixo y como porcentagens
ax.yaxis.set_major_formatter(mtick.FuncFormatter(porcentagem_formatter))

# Exibe o gráfico
plt.show()

plt.savefig('DistribuiçãoEscolaridadeMaesClasseSocial.png')

def defineAcessoInternet(possui):
    if(possui == 'A'):
        return 'Não Possui'
    else:
        return 'Possui'
    


# Comparativo de acesso à internet
VestibulandosDf['Q025'] = VestibulandosDf['Q025'].apply(defineAcessoInternet)
acessoInternetDf = VestibulandosDf.groupby(['CO_CLASSE', 'Q025'])['NU_INSCRICAO'].count() / df2.groupby(['CO_CLASSE'])['NU_INSCRICAO'].count()

acessoInternetDf = acessoInternetDf.unstack()

# Plota gráfico de barras empilhadas
ax = acessoInternetDf.plot(kind='bar', stacked=True)

# Define legendas e rótulos dos eixos
ax.set_xlabel('Classe social')
ax.set_ylabel('Proporção')
ax.set_title('Acesso à Internet por Classe Social')

ax.set_xticklabels(ax.get_xticklabels(), rotation=0)

# Cria a legenda personalizada
handles, labels = ax.get_legend_handles_labels()
new_labels = ['Não possui acesso','Possui acesso']

legend = ax.legend(handles=handles, labels=new_labels, title=None)

# Formata os rótulos do eixo y como porcentagens
ax.yaxis.set_major_formatter(mtick.FuncFormatter(porcentagem_formatter))

# Exibe o gráfico
plt.show()
plt.savefig('AcessoInternetClasseSocial.png')



