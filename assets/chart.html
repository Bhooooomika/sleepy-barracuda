<!DOCTYPE html>
<html>
<head>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
<canvas id="energyChart"></canvas>
<script>
let ctx = document.getElementById('energyChart').getContext('2d');
let labels = Array.from({length: 10}, (_, i) => `T-${10 - i}s`);
let dataPoints = Array(10).fill(0).map(() => Math.random() * 5);

const chart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: labels,
    datasets: [{
      label: 'Real-Time Usage (kW)',
      data: dataPoints,
      borderColor: 'rgba(0, 255, 200, 1)',
      backgroundColor: 'rgba(0, 255, 200, 0.1)',
      fill: true,
      tension: 0.3,
      pointRadius: 0
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    animation: { duration: 0 },
    scales: {
      y: {
        beginAtZero: true,
        ticks: {
          color: '#ffffff',
          stepSize: 1,
          max: 6
        },
        grid: { color: 'rgba(255,255,255,0.2)' }
      },
      x: {
        ticks: { color: '#ffffff' },
        grid: { color: 'rgba(255,255,255,0.1)' }
      }
    },
    plugins: {
      legend: { labels: { color: '#ffffff' } }
    }
  }
});

setInterval(() => {
  dataPoints.push(Math.random() * 5);
  dataPoints.shift();
  chart.data.datasets[0].data = dataPoints;
  chart.update();
}, 2000);
</script>
</body>
</html>
