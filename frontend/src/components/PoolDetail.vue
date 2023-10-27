<script setup lang="ts">
import axios from "axios";

import { ref, watch } from "vue";

import { Answer } from "../classes/Answer";
import { Pool } from "../classes/Pool";

import { ApiAnswer } from "../interfaces/ApiAnswer";

const props = defineProps<{ pool?: Pool }>();

const answer = ref<Answer>();

watch(
    () => props.pool,
    (pool?: Pool) => {
        let url = "http://127.0.0.1:8000/api/answer/?";

        if (pool) {
            if (!pool.open) {
                url = `${url}open=false`;
            } else {
                const occupancyRate = pool.maximumCapacity > 0
                    ? (pool.currentCapacity / pool.maximumCapacity) * 100
                    : 0;

                url = `${url}open=true&bound=${occupancyRate}`;
            }

            axios
                .get<ApiAnswer[]>(url)
                .then(response => {
                    answer.value = new Answer(
                        response.data[Math.floor(Math.random() * response.data.length)]
                    );
                });
        }
    }
)



</script>

<template>
    <div v-if="answer && props.pool">
        <p>{{ answer.reasonDescription }}</p>
        <p>{{ props.pool.swimmingPoolName }} - {{ props.pool.poolName }}</p>
        <p>{{ props.pool.maximumCapacity }} - {{ props.pool.currentCapacity }}</p>
    </div>
    <div v-else>
        <p>Click on a pool man!</p>
    </div>
</template>
