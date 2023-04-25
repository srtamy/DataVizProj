import pandas as pd
import os
import subprocess
import seaborn as sns

#Verificar se já criei arquivo contendo apenas as colunas que quero. Caso não, executa o script de conversão
if not os.path.exists('F:/Users/amand/Documentos/Projetos/DataVizProj/ENEM_RendaPerCapita.csv'):

    script_path = r'F:\Users\amand\Documentos\Projetos\DataVizProj\ENEM_RendaConversion.py'
    subprocess.run(['python', script_path])

#Separar o dataset entre treineiros e não treineiros

if not os.path.exists('F:/Users/amand/Documentos/Projetos/DataVizProj/ENEM_Treineiros.csv'):

    script_path = r'F:\Users\amand\Documentos\Projetos\DataVizProj\ENEM_DivideByTipoAplicacao.py'
    subprocess.run(['python', script_path])

#VIZ - Treineiros

script_path = r'F:\Users\amand\Documentos\Projetos\DataVizProj\Treineiros_Composition.py'
subprocess.run(['python', script_path])

#Viz - Vestibulandos

script_path = r'F:\Users\amand\Documentos\Projetos\DataVizProj\Vestibulandos_Composition.py'
subprocess.run(['python', script_path])

#Viz - Vestibulando (dados específicos)

script_path = r'F:\Users\amand\Documentos\Projetos\DataVizProj\Vestibulandos_Specific.py'
subprocess.run(['python', script_path])

#Viz - Relação entre as notas e outros parâmetros

script_path = r'F:\Users\amand\Documentos\Projetos\DataVizProj\SocialInterference.py'
subprocess.run(['python', script_path])