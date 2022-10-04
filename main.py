import requests
import json
import pandas as pd
import time

while True:
  data = requests.get('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')
  
  try:
    json_data = json.loads(data.content)

    candidato = []
    votos = []
    porcentagem = []

    for informacoes in json_data['cand']:
      if informacoes['seq'] == '1' or informacoes['seq'] == '2':
        candidato.append(informacoes['nm'])
        votos.append(informacoes['vap'])
        porcentagem.append(informacoes['pvap'])
        
    horario = json_data['hg']
    urnas_apuradas = json_data['pst']

    df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns=['', '', ''])
    
    print("\nUltima atualização: ", horario, '-', urnas_apuradas, "% das urnas apuradas", "\n", df_eleicao)
  except:
    print("Não chegou dados")
  
  time.sleep(10)