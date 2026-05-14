<script setup>
import {ref, onMounted} from 'vue' 
import axios from 'axios' //connect from front

const cpu = ref(0)
const memory = ref(0)

const fetchdata = async() =>{
  const res = await axios.get('http://127.0.0.1:8000/system')
  cpu.value = res.data.cpu
  memory.value = res.data.memory
}
onMounted(()=>
  fetchdata()
)
</script>

<template>
  <div style = "padding:20px">
  <h1>Ai Monitor MVP</h1>
  
  <p>cpu: {{cpu}}</p>
  <p>memory: {{memory}}</p>
  
  <button @click="fetchdata">refresh</button>
  </div>
</template>
