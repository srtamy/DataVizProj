import pandas as pd

# Como minha database é bastante extensa e algumas informações não estão apresentadas da forma que quero, fiz as seguintes adaptações:
# Removi as colunas que não me interessam
# Adaptei a coluna 'Q006' para que me apresentasse, no lugar da renda familiar, uma renda per capita aproximada
# Foram removidos da base todos os usuários eliminados ou ausentes em qualquer um dos dias 


caminhoArquivo ="F:/Users/amand/Documentos/Projetos/DataVizProj/MICRODADOS_ENEM_2021.csv"
ENEMDf = pd.read_csv(caminhoArquivo, sep=';', encoding='latin-1')
EnemImportColumns = ENEMDf.loc[(ENEMDf['TP_PRESENCA_CN'] == 1) & 
                                          (ENEMDf['TP_PRESENCA_CH'] == 1) & 
                                          (ENEMDf['TP_PRESENCA_LC'] == 1) & 
                                          (ENEMDf['TP_PRESENCA_MT'] == 1)]

#REMOVER (usado para melhorar a performance durante a execução dos testes)
#ENEMDfAmostra = ENEMDf.sample(frac=0.1, random_state=42)
EnemImportColumns = ENEMDf.loc[:, ['NU_INSCRICAO', 'NU_ANO', 'TP_FAIXA_ETARIA', 'TP_SEXO', 'TP_ESTADO_CIVIL', 'TP_COR_RACA', 'TP_NACIONALIDADE', 'TP_ST_CONCLUSAO', 'TP_ANO_CONCLUIU', 'TP_ESCOLA', 'TP_ENSINO', 'IN_TREINEIRO', 'CO_MUNICIPIO_ESC', 'NO_MUNICIPIO_ESC', 'CO_UF_ESC', 'SG_UF_ESC', 'TP_DEPENDENCIA_ADM_ESC', 'TP_LOCALIZACAO_ESC', 'TP_SIT_FUNC_ESC', 'CO_MUNICIPIO_PROVA', 'NO_MUNICIPIO_PROVA', 'CO_UF_PROVA', 'SG_UF_PROVA', 'TP_PRESENCA_CN', 'TP_PRESENCA_CH', 'TP_PRESENCA_LC', 'TP_PRESENCA_MT', 'CO_PROVA_CN', 'CO_PROVA_CH', 'CO_PROVA_LC', 'CO_PROVA_MT', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'TX_RESPOSTAS_CN', 'TX_RESPOSTAS_CH', 'TX_RESPOSTAS_LC', 'TX_RESPOSTAS_MT', 'TP_LINGUA', 'TX_GABARITO_CN', 'TX_GABARITO_CH', 'TX_GABARITO_LC', 'TX_GABARITO_MT', 'TP_STATUS_REDACAO', 'NU_NOTA_COMP1', 'NU_NOTA_COMP2', 'NU_NOTA_COMP3', 'NU_NOTA_COMP4', 'NU_NOTA_COMP5', 'NU_NOTA_REDACAO', 'Q001', 'Q002', 'Q003', 'Q004', 'Q005', 'Q006', 'Q024', 'Q025'
]]

#Converte as faixas salariais em uma média da faixa salarial 
EnemImportColumns.loc[EnemImportColumns['Q006'] == 'A', 'Q006'] =0
EnemImportColumns.loc[EnemImportColumns['Q006'] == 'B', 'Q006'] =1100
EnemImportColumns.loc[EnemImportColumns['Q006'] == 'C', 'Q006'] =1375
EnemImportColumns.loc[EnemImportColumns['Q006'] == 'D', 'Q006'] =1925
EnemImportColumns.loc[EnemImportColumns['Q006'] == 'E', 'Q006'] =2475
EnemImportColumns.loc[EnemImportColumns['Q006'] == 'F', 'Q006'] =3025
EnemImportColumns.loc[EnemImportColumns['Q006'] == 'G', 'Q006'] =3850
EnemImportColumns.loc[EnemImportColumns['Q006'] == 'H', 'Q006'] =4950
EnemImportColumns.loc[EnemImportColumns['Q006'] == 'I', 'Q006'] =6050
EnemImportColumns.loc[EnemImportColumns['Q006'] == 'J', 'Q006'] =7150
EnemImportColumns.loc[EnemImportColumns['Q006'] == 'K', 'Q006'] =8250
EnemImportColumns.loc[EnemImportColumns['Q006'] == 'L', 'Q006'] =9350
EnemImportColumns.loc[EnemImportColumns['Q006'] == 'M', 'Q006'] =10450
EnemImportColumns.loc[EnemImportColumns['Q006'] == 'N', 'Q006'] =12100
EnemImportColumns.loc[EnemImportColumns['Q006'] == 'O', 'Q006'] =14850
EnemImportColumns.loc[EnemImportColumns['Q006'] == 'P', 'Q006'] =19250
EnemImportColumns.loc[EnemImportColumns['Q006'] == 'Q', 'Q006'] =22000

#Converte Q006 na renda percapita
divide = lambda x: x['Q006'] / x['Q005']

EnemImportColumns['Q006'] = EnemImportColumns.apply(divide, axis=1)

#Cria coluna de classe social baseada nas rendas per capitado IBGE
def define_classe(renda):
    if renda >= 3755.77:
        return 'A'
    elif renda >= 1543.20 and renda <= 3755.76:
        return 'B'
    elif renda >= 667.87 and renda <= 1543.19:
        return 'C'
    elif renda >= 122.68 and renda <= 667.86:
        return 'D'
    else:
        return 'E'
EnemImportColumns['CO_CLASSE'] = EnemImportColumns['Q006'].apply(define_classe)

# Calcula a média das notas nos 5 eixos
EnemImportColumns['MEDIA_NOTAS'] = EnemImportColumns[['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']].mean(axis=1)

#Converte em CSV
EnemImportColumns.to_csv('ENEM_RendaPerCapita.csv', index=True)
