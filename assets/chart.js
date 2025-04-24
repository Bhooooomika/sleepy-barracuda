<canvas id="energyChart" width="600" height="300"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
let ctx = document.getElementById('energyChart').getContext('2d');
let labels = Array.from({length: 20}, (_, i) => `T-${20 - i}s`);
let data = Array.from({length: 20}, () => Math.random() * 3);
let chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: 'Energy Usage (kW)',
            data: data,
            borderColor: 'rgba(0, 200, 83, 1)',
            fill: false,
            tension: 0.4
        }]
    },
    options: {
        animation: false,
        responsive: true,
        scales: {
            y: { beginAtZero: true, max: 5 }
        }
    }
});

setInterval(() => {
    data.push(Math.random() * 3);
    data.shift();
    chart.data.datasets[0].data = data;
    chart.update();
}, 1000);
</script>
