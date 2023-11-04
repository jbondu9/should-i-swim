<script setup lang="ts">
import { Pool } from "../classes/Pool";
import { ApiPool } from "../interfaces/ApiPool";
import axios from "axios";
import { onMounted, ref } from "vue";

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
  <div v-if="poolList" class="h-[50vh]">
    <div
      v-for="pool in poolList"
      :key="pool.id"
      class="mx-auto mb-4 flex h-24 max-w-xs items-center rounded bg-white shadow-md transition-opacity duration-700"
      :class="{ 'opacity-50': selectedPool?.id != pool.id }"
      @click="
        selectedPool = pool;
        $emit('selectedPool', pool);
      "
    >
      <div class="w-full">
        <div class="flex">
          <div class="shrink-0">
            <div class="h-20 w-20 rotate-[-11deg] rounded bg-blue-900">
              <img
                class="h-20 w-20 rotate-[-12deg] rounded object-cover shadow"
                src="https://images.unsplash.com/photo-1576610616656-d3aa5d1f4534?auto=format&fit=crop&q=80&w=1470&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                :alt="pool.swimmingPoolName"
              />
            </div>
          </div>
          <div class="w-full px-6 py-4">
            <div class="text-sm font-semibold capitalize tracking-wide">
              {{ pool.swimmingPoolName }}
            </div>
            <p class="text-xs capitalize text-slate-500">{{ pool.poolName }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
