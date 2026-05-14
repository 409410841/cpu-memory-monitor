<script setup>
import CpuChart from "./component/CpuChart.vue"
import MemoryChart from "./component/MemoryChart.vue"
import DiskChart from "./component/DiskChart.vue"
import NetworkChart from "./component/NetworkChart.vue"
</script>

<template>
  <div class="grid">
    <CpuChart />
    <MemoryChart />
    <DiskChart />
    <NetworkChart />
  </div>
</template>

<style>
.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}
</style>
