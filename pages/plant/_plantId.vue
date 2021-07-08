<template>
  <div class="plant-page-container">
    <div class="header-container">
      <h2 class="title mobile">{{ plant.title }}</h2>
      <div class="images-container">
        <div class="mini-images">
          <img
            v-for="(image, index) in plant.pictures"
            v-show="index < 3"
            :key="index"
            class="mini-image"
            :src="image"
            :class="{ selected: image === bigImage }"
            @click="selectImage(image)"
          />
        </div>
        <img class="big-image" :src="bigImage" />
      </div>
      <div class="info-container">
        <div class="title-container">
          <h2 class="title desktop">{{ plant.title }}</h2>
          <div class="actions">
            <ig-icon-button
              style="margin: 0 4px"
              color="#FF2D55"
              icon="heart"
            />
            <ig-icon-button
              style="margin: 0 4px"
              color="#27AE60"
              icon="share-alt"
            />
            <ig-icon-button style="margin: 0 4px" icon="plus" />
          </div>
        </div>
        <div class="subtitle">
          در دسته‌های:
          <span
            v-for="category in plant.categories"
            :key="category"
            class="green"
          >
            {{ category[1] }}
          </span>
        </div>
        <div class="card-title">
          <div class="title">اسامی گیاه</div>
          <img src="/img/lightbulb.svg" />
        </div>
        <div class="card">
          <div class="info">نام علمی: {{ plant.scientific_name }}</div>
          <div class="info">خانواده: {{ plant.family }}</div>
          <div class="info">
            <div class="info-title">اسامی رایج</div>
            <div class="info-title">تلفظ</div>
          </div>
          <div
            v-for="(name, index) in plant.common_names"
            v-show="index < 3 || showMore"
            :key="index"
            class="info"
          >
            {{ name }}
            <img
              src="/img/player.svg"
              class="clickable"
              @click="showDownloadModal = true"
            />
          </div>
          <ig-button
            v-show="plant.common_names.length > 3 && !showMore"
            class="show-more"
            type="secondary"
            secondary-color="green"
            size="medium"
            @click="showMore = true"
          >
            اسامی بیشتر
          </ig-button>
        </div>
      </div>
    </div>
    <div class="tabs-container">
      <div
        :class="{ active: activeTab === 1 }"
        class="tab-text"
        @click="activeTab = 1"
      >
        معرفی
      </div>
      <div
        class="tab-text"
        :class="{ active: activeTab === 2 }"
        @click="activeTab = 2"
      >
        نگهداری
      </div>
      <div
        :class="{ active: activeTab === 3 }"
        class="tab-text"
        @click="activeTab = 3"
      >
        ویژگی‌ها
      </div>
    </div>
    <div class="content-container">
      <template v-if="activeTab === 1">
        <div class="info-col">
          <div class="card-title">
            <div class="title">معرفی کلی</div>
            <img src="/img/lightbulb.svg" />
          </div>
          <div class="info-card">
            {{ generalInfo[plantId - 1] }}
          </div>
        </div>
        <div class="info-col">
          <div class="card-title">
            <div class="title">چکیده مشخصات</div>
            <img src="/img/lightbulb.svg" />
          </div>
          <div class="abstract-container">
            <div class="abstract-row">
              <div class="abstract-card">
                <img src="/img/icons/abstract-ab.svg" />
                <div class="text">
                  {{ plantId === 6 ? 'آبیاری معمولی' : 'آبیاری کم' }}
                </div>
              </div>
              <div class="abstract-card">
                <img src="/img/icons/abstract-noor.svg" />
                <div class="text">{{ light }}</div>
              </div>
              <div class="abstract-card">
                <img src="/img/icons/abstract-residegi.svg" />
                <div class="text">{{ level }}</div>
              </div>
            </div>
            <div class="abstract-row">
              <div class="abstract-card">
                <img src="/img/icons/abstract-rotoobat.svg" />
                <div class="text">{{ humidity }}</div>
              </div>
              <div class="abstract-card">
                <img src="/img/icons/abstract-dama.svg" />
                <div class="text">دمای اتاق</div>
              </div>
              <div class="abstract-card">
                <img src="/img/icons/abstract-sami.svg" />
                <div class="text">{{ plant.toxic ? 'سمی' : 'غیر سمی' }}</div>
              </div>
            </div>
          </div>
        </div>
      </template>
      <template v-else-if="activeTab === 2">
        <div class="info-col">
          <div class="card-title">
            <div class="title">مراقبت و روش نگهداری</div>
            <img src="/img/lightbulb.svg" />
          </div>
          <div class="info-card">
            <div class="info-row">
              <img src="/img/icons/ab.svg" />
              <div class="info-row-title">آبیاری:</div>
              {{ plant.waterings }}
            </div>
            <div class="info-row">
              <img src="/img/icons/kood.svg" />
              <div class="info-row-title">کوددهی:</div>
              {{ plant.fertilizers }}
            </div>
            <div class="info-title-row">میزان رسیدگی</div>
            <div class="info-row">
              <img src="/img/icons/residegi.svg" />
              <div class="info-row-title">سطح رسیدگی:</div>
              {{ level }}
            </div>
            <div class="info-row">
              <img src="/img/icons/tamiz.svg" />
              <div class="info-row-title">تمیزکاری:</div>
              {{ cleanings }}
            </div>
            <div class="info-row">
              <img src="/img/icons/haras.svg" />
              <div class="info-row-title">هرس کردن:</div>
              {{ plant.pruning ? 'دارد' : 'ندارد' }}
            </div>
            <div class="info-row">
              <img src="/img/icons/meh.svg" />
              <div class="info-row-title">مه پاشی:</div>
              {{ plant.fogging ? 'دارد' : 'ندارد' }}
            </div>
            <div class="info-row">
              <img src="/img/icons/checkup.svg" />
              <div class="info-row-title">نیاز به چکاپ:</div>
              {{ needCheck }}
            </div>
          </div>
        </div>
        <div class="info-col">
          <div class="card-title">
            <div class="title">محل نگهداری</div>
            <img src="/img/lightbulb.svg" />
          </div>
          <div class="info-card">
            <div class="info-row">
              <img src="/img/icons/noor.svg" />
              <div class="info-row-title">نور:</div>
              {{ light }}
            </div>
            <div class="info-row">
              <img src="/img/icons/dama.svg" />
              <div class="info-row-title">دما:</div>
              دمای اتاق
            </div>
            <div class="info-row">
              <img src="/img/icons/rotoobat.svg" />
              <div class="info-row-title">رطوبت:</div>
              {{ humidity }}
            </div>
            <div class="info-row">
              <img src="/img/icons/khak.svg" />
              <div class="info-row-title">خاک:</div>
              {{ soil }}
            </div>
            <div class="info-row">
              <img src="/img/icons/goldan.svg" />
              <div class="info-row-title">گلدان:</div>
              {{ pot }}
            </div>
          </div>
        </div>
      </template>
      <template v-else-if="activeTab === 3">
        <div class="info-col">
          <div class="card-title">
            <div class="title">ویژگی‌های گیاه</div>
            <img src="/img/lightbulb.svg" />
          </div>
          <div class="info-card">
            <div class="info-row">
              <img src="/img/icons/sami.svg" />
              <div class="info-row-title">سمی:</div>
              {{ plant.toxic ? 'هست' : 'نیست' }}
            </div>
            <div class="info-row">
              <img src="/img/icons/hasasiat.svg" />
              <div class="info-row-title">حساسیت:</div>
              {{ plant.irritant ? 'دارد' : 'ندارد' }}
            </div>
            <div class="info-title-row">چرخه زمانی</div>
            <div class="info-row">
              <img src="/img/icons/omr.svg" />
              <div class="info-row-title">عمر گیاه:</div>
              {{ plant.life_span }} سال
            </div>
            <div class="info-row">
              <img src="/img/icons/goldehi.svg" />
              <div class="info-row-title">زمان گل‌دهی:</div>
              {{ plant.flower_time }}
            </div>
            <div class="info-row">
              <img src="/img/icons/residegi.svg" />
              <div class="info-row-title">زمان برگ‌دهی:</div>
              {{ plant.leaf_time }}
            </div>
            <div class="info-title-row">سایز رشد</div>
            <div class="info-row">
              <img src="/img/icons/arz.svg" />
              <div class="info-row-title">عرض گل:</div>
              {{ plant.max_width }} سانتی متر
            </div>
            <div class="info-row">
              <img src="/img/icons/tool.svg" />
              <div class="info-row-title">ارتفاع گل:</div>
              {{ plant.max_height }} سانتی متر
            </div>
          </div>
        </div>
        <div class="info-col">
          <div class="card-title">
            <div class="title">محل نگهداری</div>
            <img src="/img/lightbulb.svg" />
          </div>
          <div class="info-card">
            <div class="info-row">
              <img src="/img/icons/rang.svg" />
              <div class="info-row-title">رنگ:</div>
              <span v-for="(color, index) in plant.colors" :key="index">
                {{ color[1] }}{{ index != plant.colors.length - 1 ? '، ' : '' }}
              </span>
            </div>
            <div class="info-title-row">برگ‌ها</div>
            <div class="info-row">
              <img src="/img/icons/residegi.svg" />
              <div class="info-row-title">نوع برگ:</div>
              {{ plant.leaf_type }}
            </div>
            <div class="info-title-row">گل‌ها</div>
            <div class="info-row">
              <img src="/img/icons/goldehi.svg" />
              <div class="info-row-title">نوع گل:</div>
              {{ plant.flower_type }}
            </div>
          </div>
        </div>
      </template>
    </div>
    <div class="other-plants-title">سایر گیاهان</div>
    <div class="other-plants-container">
      <plant-card
        v-for="plant in plants"
        v-show="plant.id !== plantId"
        :key="plant.id"
        :plant-id="plant.id"
        :plant-image="plant.picture"
        :plant-name="plant.title"
      />
    </div>
    <ig-modal v-model="showDownloadModal" name="download" :width="480">
      <div class="modal-body">این امکان به زودی اضافه می‌‌‌شود.</div>
    </ig-modal>
  </div>
</template>
<script lang="ts">
import Vue from 'vue'
import { typedMapState } from 'vuex-module-accessor'
import IgButton from '~/components/IgButton.vue'

// components
import IgIconButton from '~/components/IgIconButton.vue'
import IgModal from '~/components/IgModal.vue'
import PlantCard from '~/components/PlantCard.vue'

// store
import plant, { PlantModule } from '~/store/plant'
import search, { SearchModule } from '~/store/search'

const levelChoices = {
  e: 'آسان',
  m: 'متوسط',
  h: 'سخت',
}

const needToCheckChoices = {
  no: 'ندارد',
  aw: 'بعد از آبیاری',
  '1w': 'هفتگی',
  '2w': 'دو هفته یکبار',
}

const lightChoices = {
  d: 'مستقیم',
  i: 'غیر مستقیم',
  l: 'کم‌نور',
  a: 'نور مصنوعی',
}

const humidityChoices = {
  d: 'خشک',
  n: 'معمولی',
  h: 'مرطوب',
}

const soilTypeChoices = {
  w: 'آب',
  l: 'خاک سبک',
  c: 'خاک مخلوط',
}

const potTypeChoices = {
  p: 'پلاستیکی',
  e: 'سفالی',
}

// export type season_choices = {
//         sp: 'بهار',
//         'su': 'تابستان',
//         'f': 'پاییز',
//         'w': 'زمستان'
//     }

let selectedImage = ''

export default Vue.extend({
  components: { IgIconButton, IgButton, IgModal, PlantCard },
  data: () => ({
    showDownloadModal: false,
    bigImage: selectedImage,
    plantId: 0,
    showMore: false,
    activeTab: 1,
    generalInfo: [
      `گل شمعدانی با نام علمی “Pelargonium spp” از گیاهان گل‌دار از خانواده (Geraniaceae) است و دارای حدود ۲۰۰ گونه بوده و بومی آفریقای جنوبی می‌باشد. گیاه شمعدانی گیاه بسیار پرطرفداری است. پروش دادن این گیاه آسان است و رنگ‌های متنوع با بوی مطبوعی دارد. گل شمعدانی گیاهانی علفی، یکساله (یا چندساله) و پایا هستند و خیلی کم در برخی از آن‌ها بوته‌های پیچان با ساقه گوشتی وجود دارد. برگ‌ها در این گیاه، منفرد یا متقابل، غالباً گوشوارک دار، پهنک، برگ‌ها همیشه منقسم، دارای بریدگی‌های بسیار، بطور کلی پنجه‌ای و پوشیده از کرک‌های غده‌ای و اسانس‌دار هستند. در ادامه نکات مهم در نگهداری گل شمعدانی و بیماری‌ها و راه‌های درمان آن را برای شما شرح خواهیم داد.`,
      `زامیفولیا، در حال حاضر، یکی از محبوب‌ترین گیاهانِ فضای بسته، در جهان است.
      این گیاه، برگ‌های گوشتی و روغنی شکلی دارد که ظاهرِ آن را به یک گیاه دوست داشتنی تبدیل کرده است، اما دلیل محبوبیت زامیفولیا در میان مردم جهان، ظاهر زیبایش نیست!
      اصلی‌ترین دلیل علاقه مردم٬ نگهداری آسان و ساده این گیاه است.
      زامیفولیا برای کسانی که مسافرت می‌روند و یا از نگهداریِ گیاه خود غافل می‌شوند٬ یک گزینه عالی محسوب می‌شود.
      با کمی مطالعه در حوزه گیاهان آپارتمانی، متوجه خواهید شد که گیاهانی شبیه زامیفولیا، بسیار کم نظیر هستند.
      زامیفولیا یک گیاه بسیار سر‌سخت است که به راحتی شرایط دشوار را تاب می‌آورد.
      شاید به همین دلیل است که به زامیفولیا٬ گیاه کمدی هم می‌گویند؛ چون این گیاه مقادیر زیادی از آب را در برگ‌های گوشتی خود ذخیره می‌کند.
      به همین دلیل، در نور کم و آبیاری کم، به خوبی به رشد خود ادامه می‌دهد.
      به قول معروف اگر زامیفولیا را در یک کمد هم نگهداری کنید، رشد خواهد کرد.

      البته مطمئن باشید که اگر زامیفولیای خود را در محیطی پر نور قرار دهید و مرتب آبیاری کنید، شاهد جلوه‌گری و شکوه بیشتر آن خواهید بود.`,
      `سانسوریا (sansevieria) یکی از گیاهان بومیِ آفریقا، ماداگاسکار و جنوب آسیا می‌باشد.
        سانسوریا، در واقع یک گروه بسیار متنوع از گیاهان است.
        این گروه با بیش از ۷۰ گونه، رنگ‌ ها و ابعاد متنوعی دارد.
        این گیاه سرسخت، برخلاف بسیاری از گیاهان آپارتمانی، عمری طولانی دارد. 
        اصطلاحا به سانسوریا، نامیرا نیز می‌گویند.
        در واقع سانسوریا، از دسته گیاهان کم توقع محسوب می‌شود؛ چون گیاهی کم آب به شمار می‌آید و از طرفی، محیط کم نور را تحمل می‌کند.
        اگر در زمینه ی نگهداریِ گیاهان، مبتدی هستید، بهتر است با گیاهان کم توقع و مقاومی مثل سانسوریا شروع کنید.
        شما می توانید این گیاه را در داخل خانه، بالکن و باغچه ی خود نیز داشته باشید.`,
      `دیفن باخیا ( Dieffenbachia amoena ) یک گیاه رایج و مرسوم از سالهای بسیار دور است.
        این گیاه حدود ۱۲ گونه مختلف در جهان دارد و از خانواده اراسه است و بومی برزیل محسوب می‌شود.
        این گیاه زیبا برگ‌های بزرگی دارد که ترکیبی از رنگ‌های زرد، سبز و سفید است.
        برگ‌های این گیاه همزمان با بلند شدن ساقه رشد می‌کنند و به مرور زمان ساقه را لخت می‌کنند.
        چون در اثر رشد گیاه برگ‌های پایینی میریزند و ساقه را به صورت یک میله تک انشعابی تنها می‌گذارند.
        علاوه بر اینها این گیاه از دسته گیاهان سمی محسوب می‌شود.
        پس از تماس کودکان و حیوانات با گیاه خودداری کنید. چون این گیاه موادی دارد که میتواند چشم یک انسان را هم نابینا کند. البته با مراقبت میتوانید از داشتن این گیاه زیبا لذت ببرید.`,
      `اشک تمساح با نام علمی Kalanchoe Daigremontiana و نام انگلیسی Bryophyllum از ساکولنت‌های خانواده Crassulaceae یا گل نازیان می‌باشد.
        اشک نوب آفریقا و مناطق گرمسیری ماداگاسکار است.
        اشک تمساح به نام  گل لوستر، اشک عروس، Alligator plant ، Mother of Thousands و هم معروف است.
        ارتفاع گیاه اشک تمساح گاهی تا یک متر هم می‍رسد.
        برگ‌های این گیاه دندانه دار، خالدار و به رنگ‌های سبز روشن با لبه‌های سیاه رنگ دیده می‌شوند.
        شاخ و برگ‌ها‌ی لوله‌ای شکل همراه با برگ‌هایی با نقوش تیره خالدار از ویژگی‌های بارز این گونه از کالانوئه می‌باشد.`,
      `حسن یوسف یک گیاه خاطره انگیز برای ما ایرانیان است. نگهداری حسن یوسف در حیاط خانه‌های قدیمی ، تصویری است که مارا به خاطرات کودکی‌مان می‌برد. حسن یوسف یک گروه بسیار متنوع از گونه‌های رنگارنگ است که در غرب به نام « ملکه ای با دنباله های قرمز » شهرت یافته است. حسن یوسف نگهداری آسانی دارد و به همین سبب مردم به آن علاقه خاصی دارند. اگر نحوه نگهداری حسن یوسف را خوب بلد باشید ، می‌توانید گلدان‌های زیادی در ابعاد کوچک تا بسیار بزرگ مانند یک درخت ، با این گیاه داشته باشید.`,
    ],
  }),
  async fetch(context) {
    const plantIdString = context.route.params.plantId
    await plant.of(context.store).getPlant(plantIdString)
    selectedImage = plant.of(context.store).state.plant?.pictures?.[0] || ''
  },
  computed: {
    plantStore(): PlantModule {
      return plant.of(this.$store)
    },
    searchStore(): SearchModule {
      return search.of(this.$store)
    },
    ...typedMapState(search, {
      plants: (state) => state.plants,
    }),
    ...typedMapState(plant, {
      plant: (state) => state.plant,
      needCheck: (state) =>
        needToCheckChoices[state.plant?.need_to_check || ''],
      level: (state) => levelChoices[state.plant?.level || ''],
      light: (state) => lightChoices[state.plant?.light],
      humidity: (state) => humidityChoices[state.plant?.humidity],
      soil: (state) => soilTypeChoices[state.plant?.soil_type],
      pot: (state) => potTypeChoices[state.plant?.pot_type],
    }),
    cleanings(): string {
      const text =
        this.plant?.cleaning_leaves || this.plant?.cleaning_pot
          ? `${this.plant?.cleaning_pot ? 'گلدان' : ''}${
              this.plant?.cleaning_leaves && this.plant?.cleaning_pot
                ? ' و '
                : ''
            }${this.plant?.cleaning_leaves ? 'برگ‌ها' : ''}`
          : 'ندارد'
      return text
    },
  },
  beforeMount() {
    this.plantId = Number(this.$route.params.plantId)
    this.searchStore.searchPlants()
  },
  methods: {
    selectImage(src: string) {
      this.bigImage = src
    },
  },
})
</script>
<style lang="scss" scoped>
.plant-page-container {
  width: 100%;
  margin-top: 96px;
}
.header-container {
  width: 100%;
  padding: 76px;
  display: flex;
}
.images-container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 19px;
}
.title {
  &.mobile {
    margin-bottom: 8px;
    font-weight: 500;
    font-size: 28px;
    line-height: 48px;
    text-align: center;
    color: $gray-10;
  }
}
.mini-images {
  display: flex;
  flex-direction: column;
  gap: 40px;
}
.mini-image {
  width: 95px;
  border-radius: 12px;
  border: 0.2px solid #808080;
  cursor: pointer;
  &.selected {
    border: 4px solid #f7821a;
  }
}
.big-image {
  width: 512px;
  border-radius: 16px;
  border: 0.2px solid #808080;
}
.info-container {
  width: calc(50% - 45px);
  margin-right: 45px;
  .title-container {
    display: flex;
    justify-content: space-between;
    .title {
      margin-bottom: 8px;
      font-weight: 500;
      font-size: 28px;
      line-height: 48px;
      color: $gray-10;
    }
    .actions {
      display: inline-flex;
    }
  }
  .subtitle {
    .green {
      color: #27ae60;
      margin: 0px 8px;
    }
  }
}
.card-title {
  display: inline-flex;
  margin-top: 36px;
  margin-bottom: 16px;
  .title {
    font-weight: 500;
    font-size: 19px;
    line-height: 32px;
    color: $gray-10;
    margin-left: 24px;
  }
}
.card {
  width: 100%;
  padding: 16px 20px 8px 20px;
  background: #ffffff;
  box-shadow: 2px 2px 16px rgba(77, 77, 77, 0.1);
  border-radius: 8px;
  .info {
    font-size: 16px;
    line-height: 27px;
    color: #1a1a1a;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
  }
  .info-title {
    font-weight: 500;
    font-size: 16px;
    line-height: 27px;
    color: #1a1a1a;
    margin: 4px 0px 12.5px 0px;
  }
  .show-more {
    width: 240px;
    margin: 0 auto;
    margin-top: 16px;
    margin-bottom: 16px;
  }
}
.modal-body {
  padding: 24px;
  text-align: center;
  font-size: 24px;
}
.clickable {
  cursor: pointer;
}
.tabs-container {
  display: flex;
  width: 100%;
  padding: 10px 76px;
  display: flex;
  gap: 73px;
  .tab-text {
    font-weight: 500;
    font-size: 24px;
    line-height: 41px;
    color: #f7821a;
    cursor: pointer;
    width: 96px;
    height: 52px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .active {
    background: #f7821a;
    box-shadow: 0px 0px 12px rgba(165, 79, 2, 0.2);
    border-radius: 12px;
    color: $gray-100;
  }
}
.content-container {
  display: flex;
  width: 100%;
  padding: 10px 76px;
  gap: 44px;
  margin-bottom: 76px;
}
.info-col {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width: 49%;
}
.info-card {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 12px;
  padding: 12px;
  background: $gray-100;
  box-shadow: 2px 2px 16px rgba(77, 77, 77, 0.1);
  width: 100%;
  border-radius: 8px;
}
.info-row {
  display: inline-flex;
  gap: 5px;
  align-items: center;
}
.info-title-row {
  font-weight: 500;
  font-size: 19px;
  line-height: 32px;
  text-align: right;
  color: $gray-10;
}
.info-row-title {
  font-weight: 500;
  font-size: 16px;
  line-height: 27px;
}
.abstract-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 24px;
  width: 100%;
}
.abstract-row {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 24px;
}
.abstract-card {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 5px 0px;
  width: 96px;
  height: 96px;
  background: $gray-100;
  box-shadow: 2px 2px 16px rgba(77, 77, 77, 0.1);
  border-radius: 10px;
  .text {
    color: #999999;
    font-size: 14px;
    line-height: 24px;
    margin-top: 4px;
  }
}
.other-plants-title {
  font-weight: 500;
  font-size: 24px;
  line-height: 41px;
  text-align: right;
  color: #1a1a1a;
  padding: 0px 76px;
}
.other-plants-container {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-wrap: wrap;
  padding: 0px 76px;
  margin-bottom: 76px;
}
@media (max-width: $app-mobile-max-width) {
  .header-container {
    flex-direction: column;
    padding: 12px 0px;
  }
  .info-container {
    width: calc(100% - 32px);
    margin: 0 auto;
  }
  .images-container {
    margin-bottom: 20px;
  }
  .mini-images {
    gap: 10px;
    width: 14%;
  }
  .mini-image {
    width: 110%;
  }
  .big-image {
    width: 60%;
  }
  .title-container {
    justify-content: center !important;
    margin-bottom: 10px;
  }
  .content-container {
    flex-direction: column;
    padding: 10px 0px;
    gap: 0px;
  }
  .info-col {
    width: calc(100% - 32px) !important;
    margin: 0 auto;
  }
  .tabs-container {
    padding: 10px 16px;
  }
  .other-plants-title {
    padding: 0px 16px;
  }
  .other-plants-container {
    padding: 0px 16px;
    margin-bottom: 76px;
  }
}
</style>
