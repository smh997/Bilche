<template>
  <div class="search-header">
    <div class="search-container">
      <div class="title">بیلچه</div>
      <div class="subtitle">جستجوی گیاه، آموزش نگهداری و پرورش گیاهان</div>
      <div class="search-input-container">
        <div class="input-container">
          <input placeholder="دنبال چه می‌گردی؟" class="search-input" />
        </div>
        <div class="search-button">
          <ig-icon
            class="search-icon"
            icon="search"
            color="#ffffff"
            :size="18"
          />
          جستجو
        </div>
      </div>
      <div class="classifications-container">
        <div class="title">انتخاب از دسته بندی</div>
        <div class="cards-container">
          <div
            v-for="category in categories"
            :key="category"
            class="card-container"
          >
            <img :src="category.image" class="card-image" />
            <div class="card-title">{{ category.title }}</div>
          </div>
        </div>
      </div>
    </div>
    <img class="desktop" src="/img/search-header-background.svg" />
  </div>
</template>
<script lang="ts">
import Vue from 'vue'

// components
import IgIcon from '~/components/IgIcon.vue'

export default Vue.extend({
  name: 'SearchHeader',
  components: { IgIcon },
  data: () => ({
    categories: [
      {
        title: 'آپارتمانی',
        image: '/img/apartmani.svg',
      },
      {
        title: 'گیاهان مقاوم',
        image: '/img/moghavem.svg',
      },
      {
        title: 'باغچه‌ای',
        image: '/img/baqche.svg',
      },
      {
        title: 'گلدار',
        image: '/img/goldar.svg',
      },
      {
        title: 'کاکتوس و ساکولنت',
        image: '/img/cactus&saculnet.svg',
      },
    ],
  }),
})
</script>
<style lang="scss" scoped>
.search-header {
  width: 100%;
  min-height: 610px;
  background: #f8f9fb;
  margin-top: 90px;
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  padding: 75px;
}
.search-container {
  width: 59%;
  .title {
    font-weight: bold;
    font-size: 43px;
    line-height: 73px;
    /* Primary/Main */
    color: #27ae60;
  }
  .subtitle {
    font-weight: 500;
    font-size: 24px;
    line-height: 41px;
    margin-top: 8px;
    /* Gray/30 */
    color: #4d4d4d;
  }
  .search-input-container {
    display: flex;
    height: 70px;
    margin-top: 56px;
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
}
.classifications-container {
  margin-top: 56px;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  .title {
    margin-left: 40px;
    font-weight: 500;
    font-size: 24px;
    line-height: 41px;
    text-align: right;
    /* Gray/20 */
    color: #333333;
    max-width: 105px;
  }
  .cards-container {
    display: flex;
    align-items: center;
    justify-content: center;
    .card-container {
      width: 93px;
      padding: 8px;
      height: 133px;
      background: #ffffff;
      font-size: 14px;
      line-height: 24px;
      text-align: center;
      margin: 14px;
      /* card */
      box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.12);
      border-radius: 8px;
      cursor: pointer;
    }
  }
}
@media (max-width: 768px) {
  .search-header {
    padding: 30px;
  }
  .search-container {
    width: 100%;
    .title {
      text-align: center;
    }
    .subtitle {
      text-align: center;
    }
    .input-container {
      width: calc(100% - 100px) !important;
    }
    .search-button {
      width: 100px !important;
    }
  }
  .classifications-container {
    flex-wrap: wrap;
    justify-content: center;
    .title {
      margin-left: 0px;
    }
    .cards-container {
      flex-wrap: wrap;
    }
  }
}
</style>
