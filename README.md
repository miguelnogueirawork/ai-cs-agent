# AI Customer Success Agent

An AI-powered Python agent that analyzes customer health data, calculates a churn risk score, and uses an LLM (Groq API) to generate personalized retention emails and internal action plans.


## 🎯 The Problem
Customer Success Managers (CSMs) spend hours manually reviewing CRM data, support tickets, and customer sentiment to identify at-risk accounts. This manual process delays intervention and increases churn.


## 💡 The Solution
This agent automates the first layer of triage:
1. **Reads CRM Data:** Parses a JSON export of customer data (plan, MRR, open tickets, sentiment).
2. **Calculates Risk (Business Logic):** Applies a custom scoring model based on ticket volume, recency, and sentiment to calculate a Health Score (0-100).
3. **Generates Actions (AI):** Uses the Groq API to generate an empathetic retention email for the customer and an internal action plan for the support team.


## 🛠️ Tech Stack
- **Python 3**
- **Groq API** (LLM inference)
- **JSON** (Data format)
- **Environment Variables** (Security best practices)


## 🚀 How to Run

1. Clone the repository:
   `git clone https://github.com/miguelnogueirawork/ai-cs-agent.git`
   `cd ai-cs-agent`

2. Create a virtual environment:
   `python3 -m venv venv`
   `source venv/bin/activate`

3. Install dependencies:
   `pip install groq`

4. Set your Groq API key as an environment variable:
   `export GROQ_API_KEY="your_api_key_here"`

5. Run the agent:
   `python3 agent.py`


## 📊 Sample Output

When the agent detects a customer with a high churn risk (e.g., Acme Corp with a score of 100/100), it automatically generates two outputs:

### 1. Customer-Facing Email (Empathetic & Action-Oriented)
> **Subject:** Let's Resolve Your API Export Issue Together – Quick Call
> 
> Hi [First Name],
> 
> I'm really sorry to hear that your team is having trouble with the API export. I understand how frustrating that can be, especially when it's blocking critical workflows. We want to get this resolved as fast as possible...
> 
> *Suggested slots:*
> - **Today, 2 p.m. – 2:15 p.m. (GMT+1)**
> - **Tomorrow, 10 a.m. – 10:15 a.m. (GMT+1)**
> 
> *(Full email generated with a clear call-to-action and demo options).*

### 2. Internal Action Plan (For the Support Team)
The AI structures a 10-step plan with clear ownership, deadlines, and escalation paths.

| # | Task | Owner | Priority | Target Completion |
|---|------|-------|----------|-------------------|
| 1 | Re-open & Escalate Ticket | Support Lead | Highest | Within 30 min |
| 2 | Gather Diagnostic Data | Support Engineer | High | 24h |
| 3 | Reproduce Issue Locally | Senior API Engineer | High | 24h |
| 4 | Root-Cause Analysis | API Team Lead | High | 48h |
| 5 | Deploy Hotfix / Work-Around | DevOps + API Engineer | Medium | 72h |
| 6 | QA & Regression Testing | QA Lead | Medium | 48h |
| 7 | Notify Acme & Schedule Demo | CSM | High | 72h |
| 8 | Post-Resolution Follow-Up | CSM | Low | 7 days |
| 9 | Document in Knowledge Base | Technical Writer | Low | 5 days |
| 10 | Review and Preventive Measures | All Leads | Low | 10 days |

**Key Escalation:** If the fix takes longer than 5 days, the agent automatically suggests a temporary workaround (e.g., CSV export route) to mitigate churn risk.
