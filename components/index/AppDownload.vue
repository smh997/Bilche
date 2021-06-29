<template>
  <div class="download-container">
    <img src="/img/qr-code-scanning.svg" class="download-image desktop" />
    <div class="dl-links-container">
      <div class="title">اپلیکیشن بیلچه رو نصب کن</div>
      <img src="/img/qr-code-scanning.svg" class="download-image mobile" />
      <div class="subtitle">امکانات اپلیکیشن بیلچه</div>
      <div class="options">
        <div class="options-row">
          <div class="option">
            <ig-icon
              class="bullet-icon"
              :size="12"
              icon="circle"
              color="#4D4D4D"
            />
            امکانات اپلیکیشن بیلچه
          </div>
          <div class="option">
            <ig-icon
              class="bullet-icon"
              :size="12"
              icon="circle"
              color="#4D4D4D"
            />
            امکانات اپلیکیشن بیلچه
          </div>
        </div>
        <div class="options-row">
          <div class="option">
            <ig-icon
              class="bullet-icon"
              :size="12"
              icon="circle"
              color="#4D4D4D"
            />
            امکانات اپلیکیشن بیلچه
          </div>
          <div class="option">
            <ig-icon
              class="bullet-icon"
              :size="12"
              icon="circle"
              color="#4D4D4D"
            />
            امکانات اپلیکیشن بیلچه
          </div>
        </div>
        <ig-button
          class="mobile"
          type="secondary"
          secondary-color="green"
          size="big"
          style="margin: 0 auto"
          >دانلود اپلیکیشن</ig-button
        >
      </div>
      <div class="download-links desktop">
        <div class="ios-col">
          <div class="os-row">
            <img src="/img/ios.svg" />
          </div>
          <div class="download-col">
            <img class="download-badge" src="/img/sibapp.svg" />
            <img class="download-badge" src="/img/sibche.svg" />
          </div>
        </div>
        <div class="android-col">
          <div class="os-row">
            <img src="/img/android.svg" />
            <div class="download-row">
              <div class="download-col">
                <img class="download-badge" src="/img/google-play.svg" />
                <img class="download-badge" src="/img/bazaar.svg" />
              </div>
              <img class="download-badge" src="/img/bilche-dl.svg" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import Vue from 'vue'

// components
import IgIcon from '~/components/IgIcon.vue'
import IgButton from '~/components/IgButton.vue'

export default Vue.extend({
  name: 'AppDownload',
  components: { IgIcon, IgButton },
})
</script>
<style lang="scss" scoped>
.download-container {
  display: flex;
  align-items: center;
  width: 100%;
  min-height: 540px;
  padding: 50px;
}
.download-image {
  margin-right: 76px;
  &.mobile {
    width: 50%;
  }
}
.dl-links-container {
  .title {
    font-weight: bold;
    font-size: 43px;
    line-height: 73px;
    text-align: right;
    color: $gray-10;
    margin-bottom: 40px;
  }
  .subtitle {
    font-weight: 500;
    font-size: 28px;
    line-height: 48px;
    text-align: right;
    color: $gray-10;
    margin-bottom: 40px;
  }
}
.options-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  margin-right: 37px;
  .option {
    display: inline-flex;
    .bullet-icon {
      margin-left: 8px;
    }
  }
}
.download-links {
  display: flex;
  margin-right: 50px;
  margin-bottom: 30px;
  .ios-col {
    margin-left: 36px;
  }
  .os-row {
    text-align: center;
  }
  .download-badge {
    margin-bottom: 11px;
    margin-right: 20px;
    cursor: pointer;
  }
  .download-col {
    display: flex;
    flex-direction: column;
  }
  .download-row {
    display: flex;
  }
}
@media (max-width: $app-mobile-max-width) {
  .download-container {
    align-items: flex-start;
  }
  .download-image {
    margin-right: 0px;
    margin-bottom: 16px;
  }
  .dl-links-container {
    display: flex;
    align-items: center;
    flex-direction: column;
    .title {
      font-size: 24px;
      margin-bottom: 16px;
    }
    .subtitle {
      font-size: 21px;
      line-height: 36px;
      margin-bottom: 16px;
    }
  }
  .options-row {
    justify-content: center;
    flex-direction: column;
    margin-bottom: 0px;
    margin-right: 0px;
    .option {
      margin-bottom: 12px;
    }
  }
}
</style>
