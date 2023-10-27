<script setup lang="ts">
import { Pool } from "../classes/Pool";

const props = defineProps<{ pool?: Pool }>();
</script>

<template>
    <div v-if="props.pool">
        <p>{{ props.pool.swimmingPoolName }} - {{ props.pool.poolName }}</p>
        <p>{{ props.pool.maximumCapacity }} - {{ props.pool.currentCapacity }}</p>
        <p>{{ props.pool.shouldISwim() }}</p>
    </div>
    <div v-else>
        <p>Click on a pool man!</p>
    </div>
</template>
