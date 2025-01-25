<template>
    <div class="container">
      <div id="network" style="height: 800px;" ref="network"></div>
    </div>
 </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  import axios from "axios";
  import { Network } from "vis-network";
  
  // Ссылки на элементы и данные графа
  const network = ref(null);
  const graphData = ref({
    nodes: [],
    edges: []
  });
  
  // Функция для загрузки данных графа
  const loadGraph = async () => {
    try {
      const response = await axios.get("http://localhost:8000/graph");
      const data = response.data;
  
      console.log("Nodes from API:", data.nodes);
      console.log("Edges from API:", data.edges);
  
      // Преобразование данных для vis-network
      graphData.value = {
        nodes: data.nodes.map((node) => ({
          id: node.id,
          label: node.label,
          title: `<strong>${node.label}</strong><br>${node.definition}<br><a href="${node.source}" target="_blank">Source</a>`,
        })),
        edges: data.edges.map((edge) => ({
          from: edge.from_node, // Исправлено
          to: edge.to_node,     // Исправлено
          label: edge.relation,
          arrows: "to"
        }))
      };
  
      renderGraph();
    } catch (error) {
      console.error("Error loading graph data:", error);
    }
  };
  
  // Функция для рендеринга графа
  const renderGraph = () => {
    const container = network.value;
    const options = {
      nodes: {
        shape: "box",
            color: "#000000",
        font: {
          color: "#ffffff",
          size: 16
            },
        
      },
      edges: {
        color: {
          color: "#000000",
          highlight: "#ff0000"
        },
        arrows: {
          to: {
            enabled: true,
            scaleFactor: 1.2
          }
        },
        font: {
          align: "middle",
          color: "#000"
        },
        smooth: true
      },
      interaction: {
        hover: true
      },
      layout: {
        hierarchical: false
      },
      physics: {
        enabled: true,
        solver: "forceAtlas2Based",
        stabilization: { iterations: 200 }
      }
    };
  
    new Network(container, graphData.value, options);
  
    console.log("Processed nodes:", graphData.value.nodes);
    console.log("Processed edges:", graphData.value.edges);
  };
  

  onMounted(() => {
    loadGraph();
  });
  </script>
  
  <style lang="css" scoped>
 

  </style>