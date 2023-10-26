<script setup lang="ts">
import axios from "axios";

import { onMounted, ref } from "vue";

import { Pool } from "../interfaces/pool"

const poolList = ref<Pool[]>([]);

onMounted(() => {
    axios.get("http://127.0.0.1:8000/api/pool/").then(response => poolList.value = response.data)
})


</script>

<template>
    <div v-for="pool in poolList">
        <div>
            <p>{{ pool.swimming_pool_name }}</p>
        </div>
    </div>
</template>
