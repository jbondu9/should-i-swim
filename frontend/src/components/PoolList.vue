<script setup lang="ts">
import axios from "axios";
import { onMounted, ref, watch } from "vue";

import { Pool } from "../classes/Pool";
import { ApiPool } from "../interfaces/ApiPool";

const poolList = ref<Pool[]>([]);
const selectedPool = ref<Pool>();

const emit = defineEmits(["selectedPool"]);

onMounted(() => {
  axios.get<ApiPool[]>("http://127.0.0.1:8000/api/pool/").then((response) => {
    poolList.value = response.data.map((pool: ApiPool) => new Pool(pool));
    const k = Math.floor(Math.random() * poolList.value.length);
    selectedPool.value = poolList.value[k];
    emit("selectedPool", selectedPool.value);
  });
});

watch(selectedPool, (newSelectedPool) => {
  emit("selectedPool", newSelectedPool);
});
</script>

<template>
  <div class="self-end py-4 text-center">
    <div v-if="poolList && selectedPool" class="mb-6 text-lg md:text-sm">
      <label for="pool-list">Choose another pool:</label>
      <select
        id="pool-list"
        v-model="selectedPool"
        name="pools"
        class="ml-1 rounded border border-gray-500 bg-white p-1"
      >
        <option
          v-for="pool in poolList"
          :key="pool.id"
          :value="pool"
          :selected="pool.id === selectedPool.id"
        >
          {{ pool.swimmingPool }} - {{ pool.basin }}
        </option>
      </select>
    </div>
    <div class="text-sm">
      <ul>
        <li>
          Source:
          <a
            href="https://github.com/jbondu9/should-i-swim"
            target="_blank"
            class="text-gray-500 underline"
            >Github</a
          >
        </li>
      </ul>
    </div>
  </div>
</template>
