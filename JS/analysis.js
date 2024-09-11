const data = [
    {
      time: '2022-01-01',
      category: 'Food',
      amount: 100
    },
    {
      time: '2022-01-05',
      category: 'Transportation',
      amount: 50
    },
    {
      time: '2022-01-10',
      category: 'Entertainment',
      amount: 200
    },
    // ...
];


  const ctx = document.getElementById('bar-chart-canvas').getContext('2d');
  const chart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: data.map(item => item.category),
      datasets: [{
        label: 'Amount',
        data: data.map(item => item.amount),
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          // ...
        ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          // ...
        ],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });


  const ctx = document.getElementById('line-chart-canvas').getContext('2d');
  const chart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: data.map(item => item.time),
      datasets: [{
        label: 'Monthly Expense',
        data: data.map(item => item.amount),
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });



  const tableBody = document.getElementById('expense-table-body');
data.forEach(item => {
  const row = document.createElement('tr');
  row.innerHTML = `
    <td>${item.time}</td>
    <td>${item.category}</td>
    <td>${item.amount}</td>
    <td>${item.description}</td>
  `;
  tableBody.appendChild(row);
});