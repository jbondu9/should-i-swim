<script setup lang="ts">
import axios from "axios";

import { ref, watch } from "vue";

import { Answer } from "../classes/Answer";
import { Pool } from "../classes/Pool";

import { ApiAnswer } from "../interfaces/ApiAnswer";
import { ApiPool } from "../interfaces/ApiPool";

const props = defineProps<{ pool?: Pool }>();

const answer = ref<Answer>();
const pool = ref<Pool>();

watch(
    () => props.pool,
    (initialPool?: Pool) => {
        axios
            .get<ApiPool>(`http://127.0.0.1:8000/api/pool/${initialPool?.id}`)
            .then(response => {
                pool.value = new Pool(response.data)

                let url = "http://127.0.0.1:8000/api/answer/?";

                if (pool.value) {
                    if (!pool.value.isOpened) {
                        url = `${url}open=false`;
                    } else {
                        url = `${url}open=true&bound=${pool.value.currentCapacity}`;
                    }

                    axios
                        .get<ApiAnswer[]>(url)
                        .then(response => {
                            answer.value = new Answer(
                                response.data[Math.floor(Math.random() * response.data.length)]
                            );
                        });
                }
            });
    }
)
</script>

<template>
    <div class="flex justify-center items-center max-w-4xl mx-auto h-[40vh]" v-if="answer && pool">
        <p class="w-full p-1 text-white text-2xl lg:text-5xl text-center uppercase font-bold">{{ answer.reasonDescription }}
        </p>
    </div>
</template>
