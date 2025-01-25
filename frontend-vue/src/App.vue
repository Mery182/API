<script setup>
import { RouterLink, RouterView } from 'vue-router'
import DocumentationIcon from './components/icons/IconDocumentation.vue'
</script>

<template>
  <div id="app" >
    <header class="flex space-x-8 items-center bg-black text-white rounded-full h-[70px]  mx-auto px-8">
    <DocumentationIcon class="mr-10"  />
    <button class="text-xl cursor-pointer py-2 px-10 rounded-full "><RouterLink to="/">Глоссарий</RouterLink> </button>
    <button class="text-xl cursor-pointer py-2 px-10 rounded-full  ">  <RouterLink to="/graph">Semantic MindMap</RouterLink></button>
    </header>
    <!-- <Graph /> -->
    <Transition name="slide-fade">
    <RouterView />
  </Transition>
  </div>
</template>

<style scoped>
.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}
header {
  margin: 8px;
}
.router-link-active {
  background-color: white;
  border-radius: 20px;
  color: black;
  padding: 8px 15px;
}
</style>
