<script setup>
import { ref, onMounted } from "vue"
import { api } from "../api"
import Chart from "chart.js/auto" 

const dataList = ref([])

const fetchData = async () => {
  const res = await api.get("/system")

  dataList.value.push(res.data.cpu)

  if (dataList.value.length > 20) {
    dataList.value.shift()
  }

  updateChart()
}

let chart = null
const canvasRef = ref(null)

const createChart = () => {
  chart = new Chart(canvasRef.value, {
    type: "line",
    data: {
      labels: [],
      datasets: [
        {
          label: "CPU",
          data: [],
          borderColor: "white",
          borderWidth: 2,
          fill: false
        }
      ]
    }
  })
}

const updateChart = () => {
  chart.data.labels = dataList.value.map((_, i) => i)
  chart.data.datasets[0].data = [...dataList.value]
  chart.update()
}

onMounted(() => {
  createChart()
  setInterval(fetchData, 1000)
})
</script>

<template>
  <canvas ref="canvasRef"></canvas>
</template>