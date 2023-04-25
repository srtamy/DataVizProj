import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

caminhoArquivoTr ="F:/Users/amand/Documentos/Projetos/DataVizProj/ENEM_Treineiros.csv"
TreineirosDf = pd.read_csv(caminhoArquivoTr, sep=',', encoding='latin-1')

caminhoArquivoVest ="F:/Users/amand/Documentos/Projetos/DataVizProj/ENEM_Vestibulandos.csv"
VestibulandosDf = pd.read_csv(caminhoArquivoVest, sep=',', encoding='latin-1')

#Cria dataframe contendo o consolidado de cada classe 

df = pd.DataFrame({'Classe Social': ['A', 'B', 'C', 'D', 'E'],
                   'Vestibulandos': [VestibulandosDf[VestibulandosDf['CO_CLASSE'] == 'A'].shape[0],
                                     VestibulandosDf[VestibulandosDf['CO_CLASSE'] == 'B'].shape[0],
                                     VestibulandosDf[VestibulandosDf['CO_CLASSE'] == 'C'].shape[0],
                                     VestibulandosDf[VestibulandosDf['CO_CLASSE'] == 'D'].shape[0],
                                     VestibulandosDf[VestibulandosDf['CO_CLASSE'] == 'E'].shape[0]],
                   'Treineiros': [TreineirosDf[TreineirosDf['CO_CLASSE'] == 'A'].shape[0],
                                  TreineirosDf[TreineirosDf['CO_CLASSE'] == 'B'].shape[0],
                                  TreineirosDf[TreineirosDf['CO_CLASSE'] == 'C'].shape[0],
                                  TreineirosDf[TreineirosDf['CO_CLASSE'] == 'D'].shape[0],
                                  TreineirosDf[TreineirosDf['CO_CLASSE'] == 'E'].shape[0]]})

# Calcula o número total de alunos em cada classe social
df['Total'] = df['Vestibulandos'] + df['Treineiros']

# Calcula as porcentagens de treineiros em relação ao total de alunos em cada classe social
df['% Treineiros'] = (df['Treineiros'] / df['Total']) * 100

# Define a ordem das classes sociais para o gráfico
order = ['A', 'B', 'C', 'D', 'E']

# Define as labels das legendas para cada categoria
labels = ['Vestibulandos', 'Treineiros']

# Define as cores para cada categoria
colors = ['skyblue', 'salmon']

# Cria o gráfico de barras empilhadas
ax = sns.barplot(x='Classe Social', y='Total', data=df, order=order, color=colors[0], label=labels[0])
ax = sns.barplot(x='Classe Social', y='Treineiros', data=df, order=order, color=colors[1], label=labels[1])

# Adiciona as legendas
ax.legend(fontsize=14)

# Adiciona as porcentagens de treineiros dentro das barras
for i in range(len(df)):
    ax.text(i, df.iloc[i]['Treineiros'] + 3000, '{:.1f}%'.format(df.iloc[i]['% Treineiros']), ha='center', va='center')

# Define o título e os rótulos dos eixos
ax.set_title('Composição de Participantes por Classe Social', fontsize=20)
ax.set_xlabel('Classe Social', fontsize=16)
ax.set_ylabel('Número de Participantes', fontsize=16)

# Mostra o gráfico
plt.show()

plt.savefig('ComposicaoParticipantesClasseSocial.png')

#Bloxpot para comparar as notas de alunos advindos de cada classe

sns.boxplot(x='CO_CLASSE', y='MEDIA_NOTAS', data=TreineirosDf, order = order)
plt.title('Influência da Classe Social na Nota Final (Treineiros)')
plt.xlabel('Classe Social')
plt.ylabel('Média')
plt.show()
plt.savefig('InfluenciaClasseSocialNotaFinalTreineiros.png')
