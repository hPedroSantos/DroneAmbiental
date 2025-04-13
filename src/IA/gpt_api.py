import openai
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Substitua sua chave de API
openai.api_key = os.getenv('API_KEY_IA')

# Buscar os dados na URL 127.0.0.1:5000/all_data
response = requests.get("http://127.0.0.1:5000/all_data")
data = response.json()  # Supondo que os dados retornados sejam em formato JSON

# Pegando o último item dos dados
last_data = data[-1]  # Último item da lista

# Ajuste o prompt para enviar dados mínimos (sem muitos detalhes)
prompt = f"""
O último dado coletado é o seguinte:

- Tópico: {last_data['topico']}
- Data: {last_data['data']}
- Valor: {last_data['valor']}

Seu trabalho é analisar os dados e fornecer um insight sobre a qualidade do ar com base nesse dado. Se o valor for elevado ou indicar uma condição prejudicial, avise sobre o possível impacto na saúde humana. Caso o dado seja dentro dos limites seguros, forneça uma confirmação de que o ambiente está seguro.

Por favor, use suas habilidades de análise de dados para fazer uma recomendação com base nas informações fornecidas. Lembrando, consulte métricas para ter uma base de comparação e retornar uma reposta de qualidade.
"""

# Realizar a chamada ao modelo mais barato (gpt-4o-2024-08-06), usando o formato de chat
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Modelo mais barato
    messages=[
        {"role": "system", "content": "Você é um assistente inteligente que analisa dados de sensores de ar e fornece recomendações sobre a qualidade do ar."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=150  # Limite de tokens de saída maior para maior análise
)

# Exibir a resposta do modelo
print(response.choices[0].message["content"].strip())
