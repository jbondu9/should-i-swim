<script setup lang="ts">
import axios from "axios";

import { onMounted, ref } from "vue";

import { Pool } from "../classes/Pool";
import { ApiPool } from "../interfaces/ApiPool";

const poolList = ref<Pool[]>([]);
const selectedPool = ref<Pool>();

const emit = defineEmits(["selectedPool"]);

onMounted(() => {
  axios.get<ApiPool[]>("http://127.0.0.1:8000/api/pool/").then((response) => {
    poolList.value = response.data.map((pool: ApiPool) => new Pool(pool));
    selectedPool.value = poolList.value[0];
    emit("selectedPool", selectedPool.value);
  });
});
</script>

<template>
  <div class="h-[50vh]" v-if="poolList">
    <div
      v-for="pool in poolList"
      class="flex items-center max-w-xs mx-auto mb-4 h-24 bg-white rounded shadow-md transition-opacity duration-700"
      :class="{ 'opacity-50': selectedPool?.id != pool.id }"
      @click="
        selectedPool = pool;
        $emit('selectedPool', pool);
      "
    >
      <div class="w-full">
        <div class="flex">
          <div class="shrink-0">
            <div class="-rotate-[11deg] h-20 w-20 bg-blue-900 rounded">
              <img
                class="-rotate-[12deg] h-20 w-20 object-cover rounded shadow"
                src="https://images.unsplash.com/photo-1576610616656-d3aa5d1f4534?auto=format&fit=crop&q=80&w=1470&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                :alt="pool.swimmingPoolName"
              />
            </div>
          </div>
          <div class="px-6 py-4 w-full">
            <div class="capitalize text-sm tracking-wide font-semibold">
              {{ pool.swimmingPoolName }}
            </div>
            <p class="capitalize text-xs text-slate-500">{{ pool.poolName }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
