<script setup>
import { ref, onMounted, nextTick } from 'vue'
import axios from 'axios'

import {
  Chart,
  LineController,
  LineElement,
  PointElement,
  LinearScale,
  CategoryScale
} from 'chart.js'

Chart.register(
  LineController,
  LineElement,
  PointElement,
  LinearScale,
  CategoryScale
)

// canvas DOM
const canvasRef = ref(null)

// chart instance
let chart = null

// CPU data array
const cpuData = ref([])

// 建立圖表
const createChart = () => {
  if (!canvasRef.value) return

  chart = new Chart(canvasRef.value, {
    type: 'line',

    data: {
      labels: [],

      datasets: [
        {
          label: 'CPU Usage %',
          data: [],
          borderWidth: 2,
          borderColor:'white',
          fill: false
        }
      ]
    },

    options: {
      responsive: true,

      scales: {
        y: {
          min: 0,
          max: 100
        }
      }
    }
  })
}

// 更新圖表
const updateChart = () => {
  if (!chart) return

  chart.data.labels = [...cpuData.value.map((_, i) => i)]

  chart.data.datasets[0].data = [...cpuData.value]

  chart.update()
}

// 拿後端資料
const fetchData = async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/system')

    cpuData.value.push(res.data.cpu)

    // 只保留最近 10 筆
    if (cpuData.value.length > 10) {
      cpuData.value.shift()
    }

    updateChart()
  } catch (error) {
    console.log(error)
  }
}

// 畫面載入後執行
onMounted(async () => {
  // 等待 DOM render 完成
  await nextTick()

  // 建立 chart
  createChart()

  // 第一次抓資料
  fetchData()

  // 每秒更新一次
  setInterval(fetchData, 1000)
})
</script>

<template>
  <div>
    <h1>CPU Monitor</h1>

    <canvas ref="canvasRef"></canvas>
  </div>
</template>