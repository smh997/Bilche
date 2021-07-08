<template>
  <a :href="`http://localhost:3000/plant/${plantId}`" class="plant-card">
    <img class="card-image" :src="plantImage" />
    <div class="card-title">{{ plantName }}</div>
  </a>
</template>
<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  name: 'PlantCard',
  props: {
    plantId: {
      type: Number,
      default: 0,
    },
    plantName: {
      type: String,
      default: '',
    },
    plantImage: {
      type: String,
      default: '',
    },
  },
})
</script>
<style lang="scss" scoped>
.plant-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 8px;
  width: 201px;
  height: 229px;
  box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.12);
  background: $gray-100;
  border-radius: 8px;
  margin: 8px 16px;
  .card-image {
    margin-top: 22px;
    width: 185px;
    height: 146px;
    margin-bottom: 8px;
  }
  .card-title {
    font-size: 14px;
    line-height: 24px;
    color: $gray-10;
    margin-bottom: 8px;
  }
  .card-subtitle {
    font-weight: 300;
    font-size: 12px;
    line-height: 20px;
    color: $gray-10;
  }
}
</style>
