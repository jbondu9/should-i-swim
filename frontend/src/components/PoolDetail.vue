<script setup lang="ts">
import axios from "axios";

import { ref, watch } from "vue";

import { Answer } from "../classes/Answer";
import { Pool } from "../classes/Pool";

import { ApiAnswer } from "../interfaces/ApiAnswer";
import { ApiPool } from "../interfaces/ApiPool";

const props = defineProps<{ pool?: Pool }>();

const answer = ref<Answer>();
const poolRef = ref<Pool>();

watch(
  () => props.pool,
  (poolProps?: Pool) => {
    axios
      .get<ApiPool>(`http://127.0.0.1:8000/api/pool/${poolProps?.id}`)
      .then((response) => {
        poolRef.value = new Pool(response.data);

        let url = "http://127.0.0.1:8000/api/answer/?";

        if (poolRef.value) {
          if (!poolRef.value.isOpened) {
            url = `${url}open=false`;
          } else {
            url = `${url}open=true&bound=${poolRef.value.currentCapacity}`;
          }

          axios.get<ApiAnswer[]>(url).then((response) => {
            answer.value = new Answer(
              response.data[Math.floor(Math.random() * response.data.length)],
            );
          });
        }
      });
  },
);
</script>

<template>
  <div
    v-if="answer && poolRef"
    class="mx-auto flex h-[40vh] max-w-4xl items-center justify-center"
  >
    <p
      class="w-full p-1 text-center text-2xl font-bold uppercase text-white lg:text-5xl"
    >
      {{ answer.reasonDescription }}
    </p>
  </div>
</template>
