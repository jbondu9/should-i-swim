<script setup lang="ts">
import axios from "axios";

import { onMounted, ref } from "vue";

import PoolDetail from "./PoolDetail.vue";

import { Pool } from "../classes/Pool";
import { ApiPool } from "../interfaces/ApiPool";

const poolList = ref<Pool[]>([]);
const selectedPool = ref<Pool>();

onMounted(() => {
    axios
        .get<ApiPool[]>("http://127.0.0.1:8000/api/pool/")
        .then(response => poolList.value = response.data.map((pool: ApiPool) => new Pool(pool)));
});
</script>

<template>
    <PoolDetail :pool="selectedPool" />
    <div class="flex items-center max-w-xs mx-auto mb-4 h-24 bg-white rounded shadow-md" v-for="pool in poolList"
        @click="selectedPool = pool">
        <div class="w-full">
            <div class="flex">
                <div class="shrink-0">
                    <div class="-rotate-[8deg] h-20 w-20 bg-blue-800 rounded">
                        <img class="-rotate-[12deg] h-20 w-20 object-cover rounded shadow" src=""
                            :alt="pool.swimmingPoolName" />
                    </div>
                </div>
                <div class="px-6 py-4 w-full">
                    <div class="uppercase text-sm tracking-wide font-semibold">{{ pool.swimmingPoolName }}</div>
                    <p class="text-xs text-slate-500">{{ pool.poolName }}</p>
                </div>
            </div>
        </div>
    </div>
</template>
