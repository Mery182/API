<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

// Состояние для хранения списка терминов
const terms = ref({});

// Функция для загрузки данных с API
const fetchTerms = async () => {
  try {
    const response = await axios.get("http://localhost:8000/terms"); // Замените URL на свой
    terms.value = response.data;
  } catch (error) {
    console.error("Ошибка при загрузке терминов:", error);
  }
};

// Загружаем данные при монтировании компонента
onMounted(() => {
  fetchTerms();
});
</script>
<template>
    <div class="container">
      <ul class="flex flex-wrap gap-4 mx-auto justify-between">
        <li
          v-for="(term, id) in terms"
          :key="id"
          class="p-4 border rounded-[20px] w-[350px]"
        >
          <h2 class="text-lg font-black">{{ term.term }}</h2>
          <p class="text-gray-700"><br>{{ term.definition }}</p>
          <!-- <p class="text-sm text-gray-500">Priority: {{ term.priority }}</p> -->
        </li>
      </ul>
    </div>
  </template>
  
  
  <style scoped>
  /* Стили для списка */
  </style>