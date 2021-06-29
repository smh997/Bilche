<template>
  <div class="news-container">
    <div class="title mobile">در خبرنامه بیلچه عضو شو</div>
    <div class="flex-reverse-container">
      <img class="news-letter-image" src="/img/newsLetter-image.svg" />
      <div class="inputs-container">
        <div class="title desktop">در خبرنامه بیلچه عضو شو</div>
        <div class="subtitle">
          شماره موبایل یا ایمیلت رو وارد کن. قراره با خبرای خوب برگردیم :)
        </div>
        <div class="input-container">
          <ig-input placeholder="شماره موبایل یا ایمیل" />
          <ig-button
            type="secondary"
            secondary-color="green"
            class="submit-button"
            size="big"
          >
            عضویت
          </ig-button>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import Vue from 'vue'

// components
import IgInput from '~/components/IgInput.vue'
import IgButton from '~/components/IgButton.vue'

export default Vue.extend({
  name: 'NewsLetter',
  components: { IgInput, IgButton },
})
</script>
<style lang="scss" scoped>
.news-container {
  width: 100%;
  min-height: 464px;
  background: #fff4eb;
  .title {
    font-weight: bold;
    font-size: 43px;
    line-height: 73px;
    color: $gray-10;
    margin-bottom: 36px;
    &.mobile {
      text-align: center;
      font-size: 24px;
      line-height: 41px;
      margin-bottom: 16px;
    }
  }
}
.flex-reverse-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-direction: row-reverse;
  flex-wrap: wrap;
}
.news-letter-image {
  margin-left: 76px;
}
.inputs-container {
  margin-right: 76px;
  .subtitle {
    font-weight: 500;
    font-size: 19px;
    line-height: 32px;
    text-align: right;
    color: $gray-10;
    margin-bottom: 24px;
  }
}
.input-container {
  display: flex;
  .submit-button {
    margin-top: 5px;
    margin-right: 16px;
    width: 130px;
  }
}
@media (max-width: 768px) {
  .news-container {
    padding: 16px;
  }
  .flex-reverse-container {
    justify-content: center;
  }
  .news-letter-image {
    width: 80%;
    margin: 0 auto;
  }
  .input-container {
    flex-direction: column;
    align-items: center;
  }
  .inputs-container {
    margin-right: 0px;
    margin-bottom: 16px;
    .subtitle {
      margin-top: 16px;
    }
  }
}
</style>
