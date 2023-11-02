<script setup lang="ts">
import { ref } from "vue";

import { Pool } from "./classes/Pool";

import PoolDetail from "./components/PoolDetail.vue";
import PoolList from "./components/PoolList.vue";

const selectedPool = ref<Pool>();
</script>

<template>
  <div class="flex flex-col justify-between h-screen overflow-hidden bg-gradient-to-b from-blue-800 to-cyan-600">
    <div>
      <PoolDetail :pool="selectedPool" />
    </div>
    <div>
      <PoolList @selected-pool="(pool: Pool) => selectedPool = pool" />
    </div>
  </div>
</template>
