document.getElementById('generate-btn').addEventListener('click', async () => {
    const rows = document.getElementById('rows').value;
    const response = await fetch(`http://localhost:5000/generate?rows=${rows}`);
    const data = await response.json();
    
    let output = '<table><tr><th>ID</th><th>User ID</th><th>Valor</th><th>Tipo</th></tr>';
    data.forEach(txn => {
        output += `<tr>
            <td>${txn.id}</td>
            <td>${txn.user_id}</td>
            <td>R$ ${txn.amount.toFixed(2)}</td>
            <td>${txn.type}</td>
        </tr>`;
    });
    output += '</table>';
    document.getElementById('output').innerHTML = output;
});