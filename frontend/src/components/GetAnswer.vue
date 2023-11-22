<script setup lang="ts">
import axios from "axios";
import { ref, watch } from "vue";

import { Answer } from "../classes/Answer";
import { Pool } from "../classes/Pool";
import { ApiAnswer } from "../interfaces/ApiAnswer";
import { ApiError } from "../interfaces/ApiError";
import { ApiPool } from "../interfaces/ApiPool";

const props = defineProps<{ pool?: Pool }>();

const answer = ref<Answer>();
const poolRef = ref<Pool>();

watch(
  () => props.pool,
  (poolProps?: Pool) => {
    if (poolProps) {
      axios
        .get<ApiPool>(`http://127.0.0.1:8000/api/pool/${poolProps.id}`)
        .then((response) => {
          poolRef.value = new Pool(response.data);

          let url = "http://127.0.0.1:8000/api/answer/?";

          if (poolRef.value) {
            if (!poolRef.value.isOpened) {
              url = `${url}open=false`;
            } else {
              url = `${url}open=true&bound=${poolRef.value.currentCapacity}`;
            }

            axios
              .get<ApiAnswer>(url)
              .then((response) => {
                answer.value = new Answer(response.data);
              })
              .catch((error: ApiError) => {
                answer.value = new Answer({
                  description: error.message,
                });
              });
          }
        });
    }
  },
);
</script>

<template>
  <div class="m-auto self-center text-center">
    <h2
      class="mb-4 py-3.5 text-xl font-light uppercase text-gray-500 md:text-4xl"
    >
      Should I swim now?
    </h2>
    <div v-if="answer && poolRef">
      <h3 class="mb-4 px-8 text-4xl font-black uppercase md:px-24 md:text-7xl">
        {{ answer.description }}
      </h3>
      <ul class="flex justify-center text-sm">
        <li>
          Opening status:
          <span class="text-gray-500">{{
            poolRef.isOpened ? "Open" : "Close"
          }}</span>
        </li>
        <li class="mx-2">-</li>
        <li>
          Current capacity:
          <span class="text-gray-500">{{ poolRef.currentCapacity }}%</span>
        </li>
      </ul>
    </div>
  </div>
</template>
