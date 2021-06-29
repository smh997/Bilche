<template>
  <div class="footer-container">
    <div class="content-container">
      <div class="first-col">
        <div class="title mobile">در وبسایت</div>
        <div class="link">صفحه اصلی</div>
        <div class="link">دسته بندی گیاهان</div>
        <div class="link">وبلاگ</div>
        <div class="link">درباره ما</div>
      </div>
      <div class="second-col">
        <div class="title mobile">درباره بیلچه</div>
        <div class="link">دانلود اپلیکیشن</div>
        <div class="link">نظرات کاربران</div>
        <div class="link">ثبت نظر</div>
        <div class="link">عضویت در خبرنامه</div>
      </div>
      <div class="vue-app">
        <img class="banner-image" src="/img/banner.svg" />
        <div class="download-container">
          <div class="download-row">
            <ig-icon
              icon="twitter"
              type="fab"
              class="download-icon"
              color="#808080"
              :size="25"
            />
            <ig-icon
              icon="youtube"
              type="fab"
              class="download-icon"
              color="#808080"
              :size="25"
            />
            <ig-icon
              icon="telegram"
              type="fab"
              class="download-icon"
              color="#808080"
              :size="25"
            />
            <ig-icon
              icon="instagram"
              type="fab"
              class="download-icon"
              color="#808080"
              :size="25"
            />
          </div>
          <div class="download-row">
            <img class="icon-margin" src="/img/virgool.svg" />
            <img class="icon-margin" src="/img/aparat.svg" />
            <ig-icon
              icon="whatsapp"
              type="fab"
              class="download-icon"
              color="#808080"
              :size="25"
            />
            <ig-icon
              icon="linkedin"
              type="fab"
              class="download-icon"
              color="#808080"
              :size="25"
            />
          </div>
        </div>
      </div>
    </div>
    <div class="copy-right">
      تمام حقوق مادی و معنوی این سایت متعلق به بیلچه است.
    </div>
  </div>
</template>
<script lang="ts">
import Vue from 'vue'

// components
import IgIcon from '~/components/IgIcon.vue'

export default Vue.extend({
  name: 'Footer',
  components: { IgIcon },
})
</script>
<style lang="scss" scoped>
.footer-container {
  width: 100%;
  min-height: 400px;
  background: #292a31;
}
.content-container {
  display: flex;
  padding: 50px;
}
.first-col {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  margin-left: 92px;
  margin-right: 150px;
}
.title {
  font-weight: 500;
  font-size: 21px;
  line-height: 36px;
  color: $gray-100;
  margin-bottom: 18px;
}
.link {
  font-weight: 500;
  font-size: 19px;
  line-height: 32px;
  /* Primary / Semi Light */
  color: #32c770;
  margin-bottom: 25px;
}
.vue-app {
  margin-right: auto;
  margin-left: 26px;
}
.download-container {
  border-top: 4px solid #808080;
  margin-top: 24px;
  padding: 16px;
  .download-row {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .download-icon {
    border: 2px solid #808080;
    border-radius: 50%;
    padding: 10px;
    margin: 8px;
  }
}
.icon-margin {
  margin: 0px 10px;
}
.copy-right {
  width: 100%;
  padding: 28px;
  margin: 0 auto;
  font-weight: 500;
  font-size: 19px;
  line-height: 32px;
  text-align: center;
  /* Gray/85 */
  color: #d9d9d9;
  background: #292a31;
}
@media (max-width: 768px) {
  .content-container {
    padding: 24px;
    flex-direction: column;
  }
  .first-col {
    margin: 0;
  }
}
</style>
