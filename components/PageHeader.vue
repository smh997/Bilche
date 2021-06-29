<template>
  <div class="website-layout-header-container">
    <div class="content desktop">
      <nuxt-link class="icon-link" to="/">
        <img src="/img/bilche-icon.svg" />
      </nuxt-link>
      <nuxt-link class="link" to="/"> صفحه اصلی </nuxt-link>
      <nuxt-link class="link" to="/tracking"> دسته بندی گیاهان </nuxt-link>
      <nuxt-link class="link" to="/tracking"> درباره ما </nuxt-link>
      <nuxt-link class="link" to="/tracking"> وبلاگ </nuxt-link>
      <nuxt-link class="link last-link" to="/tracking">
        ورود / ثبت نام
      </nuxt-link>
    </div>
    <div class="content mobile">
      <ig-icon-button
        color="#27AE60"
        background="rgba(0,0,0,0.1)"
        icon="bars"
        :icon-font-weight="300"
        :icon-size="20"
      />
      <img src="/img/bilche-persian-typo.svg" />
    </div>
  </div>
</template>
<script lang="ts">
import Vue from 'vue'
// import IgIcon from '~/components/IgIcon.vue'
import IgIconButton from '~/components/IgIconButton.vue'

export default Vue.extend({
  components: { IgIconButton },
})
</script>
<style lang="scss" scoped>
.website-layout-header-container {
  position: fixed;
  top: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 96px;
  width: 100%;
  background: white;
  box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.12);
  box-sizing: border-box;
  z-index: 100;
}
.content {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  // max-width: $website-max-width;
  padding: 0 20px;
  box-sizing: border-box;

  .avatar {
    margin-left: 40px;
  }
  .icon-link {
    width: 72px;
    height: 72px;
    margin-left: 41px;
  }
  .link {
    margin-left: 50px;
    // text
    font-style: normal;
    font-weight: 500;
    font-size: 14px;
    line-height: 30px;
    text-align: right;
    color: #27ae60;
    text-decoration-line: none;
  }
  .last-link {
    margin-right: auto;
  }
  .social-icons {
    display: inline-flex;
    margin-right: auto;
  }
  .social-icon {
    &.instagram {
      margin-right: auto;
    }
    &.telegram {
      margin-right: 30px;
    }
  }
}
@media (max-width: 760px) {
  .content {
    justify-content: space-between;
  }
}
</style>
