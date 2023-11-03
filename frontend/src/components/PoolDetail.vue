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
              response.data[Math.floor(Math.random() * response.data.length)]
            );
          });
        }
      });
  }
);
</script>

<template>
  <div
    v-if="answer && poolRef"
    class="flex justify-center items-center max-w-4xl mx-auto h-[40vh]"
  >
    <p
      class="w-full p-1 text-white text-2xl lg:text-5xl text-center uppercase font-bold"
    >
      {{ answer.reasonDescription }}
    </p>
  </div>
</template>
