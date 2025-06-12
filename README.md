# BetData Generator

## Descrição do Projeto
Projeto full stack para geração de dados fictícios de transações financeiras no contexto de casas de apostas. Desenvolvido para auxiliar nos meus estudos em análises de dados e desenvolvimento full stack. Simulando operações reais como depósitos, saques e apostas.

## Funcionalidades Principais
- Geração de transações financeiras realistas via PIX
- Controle sobre quantidade de registros (10 a 10.000 linhas)
- Dados temporais variados com horários estratégicos
- Valores aleatórios dentro de parâmetros configuráveis
- Diferentes status de transação (completo, pendente, falha)

## Tecnologias Utilizadas
### Backend:
- Python 3.10+
- Flask
- Biblioteca datetime para geração de timestamps

### Frontend:
- HTML5
- CSS3
- JavaScript puro

### Ferramentas:
- Git para controle de versão
- GitHub para hospedagem do código
- GCP para deploy futuro

## Como Usar
1. Clone o repositório:
```bash
git clone https://github.com/alannasantos/BetData-Generator.git
```
2. Configure o backend:
```bash
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Acesse o frontend:
Abra o arquivo frontend/index.html no navegador.

## Objetivos
- Praticar programação full stack
- Criar ferramenta útil para análise de dados
- Simular cenários realistas para estudo

## Roadmap
- Versão 1.0: Gerador básico de transações
- Versão 2.0: Deploy no GCP + integração com BigQuery


Desenvolvido por Alanna Santos como parte do processo de transição de carreira para área de tecnologia. Contribuições e sugestões são bem-vindas.

- Observação: Todos os dados gerados são fictícios e destinados apenas para fins de estudo.

