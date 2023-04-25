import pandas as pd

#Serão criados 2 novos tipos DB, um para treineiros e outro para aplicações oficiais

caminhoArquivo ="F:/Users/amand/Documentos/Projetos/DataVizProj/ENEM_RendaPerCapita.csv"
ENEMDf = pd.read_csv(caminhoArquivo, sep=',', encoding='latin-1')

TreineirosDf = ENEMDf.loc[ENEMDf['IN_TREINEIRO']== 1]

TreineirosDf.to_csv('ENEM_Treineiros.csv', index=True)

VestibulandosDf = ENEMDf.loc[ENEMDf['IN_TREINEIRO']== 0]

VestibulandosDf.to_csv('ENEM_Vestibulandos.csv', index=True)