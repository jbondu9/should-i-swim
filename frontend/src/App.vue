<script setup lang="ts">
import { ref } from "vue";

import { Pool } from "./classes/Pool";

import GetAnswer from "./components/GetAnswer.vue";
import PoolList from "./components/PoolList.vue";

const selectedPool = ref<Pool>();
</script>

<template>
  <div class="grid min-h-screen grid-rows-[1fr_auto] justify-center">
    <GetAnswer :pool="selectedPool" />
    <PoolList @selected-pool="(pool: Pool) => (selectedPool = pool)" />
  </div>
</template>
