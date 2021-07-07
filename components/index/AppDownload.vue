<template>
  <div class="download-container">
    <img src="/img/qr-code-scanning.svg" class="download-image desktop" />
    <div class="dl-links-container">
      <div class="title">اپلیکیشن بیلچه رو نصب کن</div>
      <img src="/img/qr-code-scanning.svg" class="download-image mobile" />
      <div class="subtitle">امکانات اپلیکیشن بیلچه</div>
      <div class="options">
        <div class="options-row">
          <div class="option first">
            <ig-icon
              class="bullet-icon"
              :size="12"
              icon="circle"
              color="#4D4D4D"
            />
            برنامه ریزی متناسب با گیاه و شرایط
          </div>
          <div class="option">
            <ig-icon
              class="bullet-icon"
              :size="12"
              icon="circle"
              color="#4D4D4D"
            />
            یادآوری آبیاری و اعمال گیاه
          </div>
        </div>
        <div class="options-row">
          <div class="option third">
            <ig-icon
              class="bullet-icon"
              :size="12"
              icon="circle"
              color="#4D4D4D"
            />
            تعریف گلخانه‌ها برای مدیریت بهتر
          </div>
          <div class="option">
            <ig-icon
              class="bullet-icon"
              :size="12"
              icon="circle"
              color="#4D4D4D"
            />
            نمودار عملکرد کاربر در نگهداری از گیاهان
          </div>
        </div>
        <ig-button
          class="mobile"
          type="secondary"
          secondary-color="green"
          size="big"
          style="margin: 0 auto"
          @click="download('d')"
        >
          دانلود اپلیکیشن
        </ig-button>
      </div>
      <div class="download-links desktop">
        <div class="ios-col">
          <div class="os-row">
            <img src="/img/ios.svg" />
          </div>
          <div class="download-col">
            <img
              class="download-badge"
              src="/img/sibapp.svg"
              @click="download('sa')"
            />
            <img
              class="download-badge"
              src="/img/sibche.svg"
              @click="download('s')"
            />
          </div>
        </div>
        <div class="android-col">
          <div class="os-row">
            <img src="/img/android.svg" />
            <div class="download-row">
              <div class="download-col">
                <img
                  class="download-badge"
                  src="/img/google-play.svg"
                  @click="download('g')"
                />
                <img
                  class="download-badge"
                  src="/img/bazaar.svg"
                  @click="download('b')"
                />
              </div>
              <img
                class="download-badge"
                src="/img/bilche-dl.svg"
                @click="download('d')"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
    <ig-modal v-model="showDownloadModal" name="download" :width="480">
      <div class="modal-body">این امکان به زودی اضافه می‌‌‌شود.</div>
    </ig-modal>
  </div>
</template>
<script lang="ts">
import Vue from 'vue'

// components
import IgIcon from '~/components/IgIcon.vue'
import IgButton from '~/components/IgButton.vue'
import IgModal from '~/components/IgModal.vue'

// store
import home, { HomeModule } from '~/store/home'
import { InstallappApplicationStoreEnum } from '~/api'

export default Vue.extend({
  name: 'AppDownload',
  components: { IgIcon, IgButton, IgModal },
  data: () => ({
    showDownloadModal: false,
  }),
  computed: {
    homeStore(): HomeModule {
      return home.of(this.$store)
    },
  },
  methods: {
    async download(link: InstallappApplicationStoreEnum) {
      this.showDownloadModal = true
      await this.homeStore.download(link)
    },
  },
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
  justify-content: flex-start;
  align-items: center;
  margin-bottom: 20px;
  margin-right: 37px;
  .option {
    display: inline-flex;
    &.first {
      margin-left: 100px;
    }
    &.third {
      margin-left: 110px;
    }
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
.modal-body {
  padding: 24px;
  text-align: center;
  font-size: 24px;
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
    align-items: flex-start;
    flex-direction: column;
    margin-bottom: 0px;
    margin-right: 0px;
    .option {
      margin-bottom: 12px;
      &.first {
        margin-left: 0px;
      }
      &.third {
        margin-left: 80px;
      }
    }
  }
}
</style>
