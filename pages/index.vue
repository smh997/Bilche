<template>
  <div class="home-container">
    <search-header />
    <popular-plants />
    <what-is-bilche />
    <comments />
    <app-download />
    <news-letter />
    <survay />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

// components
import SearchHeader from '~/components/index/SearchHeader.vue'
import PopularPlants from '~/components/index/PopularPlants.vue'
import WhatIsBilche from '~/components/index/WhatIsBilche.vue'
import Comments from '~/components/index/Comments.vue'
import AppDownload from '~/components/index/AppDownload.vue'
import NewsLetter from '~/components/index/NewsLetter.vue'
import Survay from '~/components/index/Survay.vue'

export default Vue.extend({
  components: {
    SearchHeader,
    PopularPlants,
    WhatIsBilche,
    Comments,
    AppDownload,
    NewsLetter,
    Survay,
  },
})
</script>

<style lang="scss" scoped>
.home-container {
  min-height: 100vh;
  width: 100%;
}
</style>
