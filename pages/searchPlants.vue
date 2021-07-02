<template>
  <div class="page-container">
    <div class="search-input-container">
      <div class="input-container">
        <input placeholder="دنبال چه می‌گردی؟" class="search-input" />
      </div>
      <div class="search-button">
        <ig-icon class="search-icon" icon="search" color="#ffffff" :size="18" />
        جستجو
      </div>
    </div>
    <div class="search-result-container">
      <div class="first-col desktop">
        <search-filters />
      </div>
      <div class="second-col">
        <div class="plants-container">
          <plant-card v-for="i in 10" :key="i" />
        </div>
        <pagination
          class="pagination"
          style="width: 100%"
          :count="10"
          :value="2"
        />
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import Vue from 'vue'

// components
import SearchFilters from '~/components/SearchFilters.vue'
import PlantCard from '~/components/PlantCard.vue'
import Pagination from '~/components/Pagination.vue'

export default Vue.extend({
  components: { SearchFilters, PlantCard, Pagination },
})
</script>
<style lang="scss" scoped>
.page-container {
  padding-top: 99px;
  min-height: 100vh;
  width: 81%;
  margin: 0 auto;
}
.search-input-container {
  display: flex;
  height: 76px;
  margin-top: 56px;
  margin-bottom: 86px;
  .input-container {
    width: calc(100% - 210px);
    border-radius: 0px 10px 10px 0px;
    filter: drop-shadow(0px 0px 8px rgba(0, 0, 0, 0.12));
    background: white;
    height: 70px;
    .search-input {
      width: 90%;
      height: 100%;
      border-radius: 0px 10px 10px 0px;
      border: none;
      outline: none;
      font-family: IRANSansWebFaNum;
      margin-right: 10px;
    }
  }
  .search-button {
    width: 210px;
    height: 70px;
    font-weight: 500;
    font-size: 16px;
    line-height: 27px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    /* Gray/White */
    color: #ffffff;
    /* Primary / Semi Light */
    background: #32c770;
    border-radius: 8px 0px 0px 8px;
    .search-icon {
      margin-left: 8px;
    }
  }
}
.search-result-container {
  display: flex;
  width: 100%;
  justify-content: center;
  align-items: flex-start;
  .first-col {
    width: 266px;
    margin-left: 60px;
    flex-grow: 0;
  }
  .second-col {
    width: calc(100% - 326px);
  }
  .plants-container {
    display: flex;
    align-items: flex-start;
    justify-content: center;
    flex-wrap: wrap;
  }
}
.pagination {
  width: 100%;
  margin-top: 90px;
  margin-bottom: 125px;
}
@media (max-width: $app-mobile-max-width) {
  .second-col {
    width: 100% !important;
  }
}
</style>
