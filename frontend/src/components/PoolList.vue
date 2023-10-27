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
    <div v-for="pool in poolList" @click="selectedPool = pool">
        <div>
            <p>{{ pool.swimmingPoolName }} - {{ pool.poolName }}</p>
        </div>
    </div>
</template>
