import json
from groq import Groq

# 1. Configurar o cliente da Groq
import os
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# 2. Carregar os dados do JSON
with open('customer_data.json', 'r') as file:
    customer = json.load(file)

# 3. Calcular o Health Score (Lógica de Negócio)
risk_score = 0
if customer['open_tickets'] >= 3: risk_score += 40
if customer['last_ticket_days_ago'] <= 3: risk_score += 30
if customer['sentiment'] == 'Frustrated': risk_score += 30

print(f"Cliente: {customer['company_name']}")
print(f"Health Risk Score: {risk_score}/100")

# 4. O Prompt para a IA
prompt = f"""
Act as a Senior Customer Success Manager.
Analyze this customer data: {json.dumps(customer)}
The calculated churn risk score is {risk_score}/100.

Task:
1. Write a short, empathetic email to the customer ({customer['company_name']}) to schedule a call and address their frustration.
2. Create an internal action plan for the support team on how to fix their API issue.
"""

# 5. Chamar a IA (Groq usa o formato de chat)
print("\n--- A GERAR RESPOSTA COM IA ---\n")

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    # O modelo mais rápido e estável da Groq atualmente:
    model="openai/gpt-oss-20b", 
)

print(response.choices[0].message.content)
