from flask import Flask, request, jsonify
import random
from datetime import datetime, timedelta

app = Flask(__name__)

# Função para gerar transações com PIX
def generate_transaction(rows=10):
    transactions = []
    for _ in range(rows):
        timestamp = datetime.now() - timedelta(
            days=random.randint(0, 30),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59)
        )
        amount = round(random.uniform(50, 5000), 2)
        transactions.append({
            "id": f"TXN{random.randint(100000, 999999)}",
            "user_id": f"USER{random.randint(1000, 9999)}",
            "timestamp": timestamp.isoformat(),
            "amount": amount,
            "payment_method": "PIX",
            "type": random.choice(["deposit", "withdraw", "bet"]),
            "status": random.choice(["completed", "pending", "failed"])
        })
    return transactions

@app.route('/generate', methods=['GET'])
def generate():
    rows = int(request.args.get('rows', 10))
    return jsonify(generate_transaction(rows))

if __name__ == '__main__':
    app.run(debug=True)