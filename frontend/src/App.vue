<script setup lang="ts">
import { Pool } from "./classes/Pool";
import PoolDetail from "./components/PoolDetail.vue";
import PoolList from "./components/PoolList.vue";
import { ref } from "vue";

const selectedPool = ref<Pool>();
</script>

<template>
  <div
    class="flex h-screen flex-col justify-between overflow-hidden bg-gradient-to-b from-blue-800 to-cyan-600"
  >
    <div>
      <PoolDetail :pool="selectedPool" />
    </div>
    <div>
      <PoolList @selected-pool="(pool: Pool) => (selectedPool = pool)" />
    </div>
  </div>
</template>
