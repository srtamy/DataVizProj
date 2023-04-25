import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

caminhoArquivoVest ="F:/Users/amand/Documentos/Projetos/DataVizProj/ENEM_Vestibulandos.csv"
VestibulandosDf = pd.read_csv(caminhoArquivoVest, sep=',', encoding='latin-1')

# Cria uma tabela pivot com o número de vestibulandos por classe social e tipo da escola
pivot_df = pd.pivot_table(VestibulandosDf, values='NU_INSCRICAO', index='CO_CLASSE', columns='TP_ESCOLA', aggfunc='count')

# Cria uma coluna com o total de vestibulandos por classe social
pivot_df['Total'] = pivot_df[2] + pivot_df[3]

# Calcula as porcentagens de vestibulandos por tipo da escola em cada classe social
pivot_df['Escola Pública'] = pivot_df[2] / pivot_df['Total']
pivot_df['Escola Privada'] = pivot_df[3] / pivot_df['Total']

order = ['A', 'B', 'C', 'D', 'E']

colors = ['skyblue', 'salmon']

# Cria uma lista com os valores percentuais de alunos da escola pública em cada classe social
porcentagemEscolaPublica = list(pivot_df['Escola Pública'].values * 100)

# Define a função para formatar os rótulos como porcentagem
def porcentagem_formatter(x,pos):
    return '{:.0f}%'.format(x * 100)

# Plota o gráfico de barras empilhadas com as porcentagens de vestibulandos por tipo de escola em cada classe social
sns.set_palette(sns.color_palette("Paired"))
ax = pivot_df[['Escola Pública', 'Escola Privada']].plot(kind='bar', stacked=True, figsize=(10,6), color = colors)
ax.set_xlabel('Classe Social')
ax.set_ylabel('Distribuição')
ax.set_title('Distribuição do Tipo de Ensino por Classe Social')
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)

# Cria a legenda personalizada
handles, labels = ax.get_legend_handles_labels()
new_labels = ['Escola Pública', 'Escola Privada']
legend = ax.legend(handles=handles, labels=new_labels, title=None)

# Formata as porcentagens como strings com uma casa decimal e um sinal de porcentagem
porcentagemEscolaPublica_str = [f"{p:.1f}%" for p in porcentagemEscolaPublica]

# Adiciona os rótulos de barra com as porcentagens de alunos da escola pública
ax.bar_label(ax.containers[0], labels=porcentagemEscolaPublica_str, label_type='edge')

# Formata os rótulos do eixo y como porcentagens
ax.yaxis.set_major_formatter(mtick.FuncFormatter(porcentagem_formatter))

plt.show()
plt.savefig('DistribuicaoTipoEnsinoClasseSocial.png')

#BloxPot - Distribuição da médias por classe social
sns.boxplot(x='CO_CLASSE', y='MEDIA_NOTAS', data=VestibulandosDf, order = order)
plt.title('Influencia da Classe Social na Nota Final (Vestibulandos)')
plt.xlabel('Classe Social')
plt.ylabel('Média')
plt.show()
plt.savefig('InfluenciaClasseSocialNotaFinalVestibulandos.png')
