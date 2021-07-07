<template>
  <div class="comments">
    <div class="comments-container">
      <div class="title">نظرات کاربران:</div>
      <vue-slick-carousel v-bind="carouselSettings">
        <div
          v-for="(comment, index) in comments"
          :key="index"
          class="outer-container"
        >
          <div id="feature-1" class="comment-container">
            <img class="qoute-icon" src="/img/comments-qoute.svg" />
            <div class="comment-text">
              {{ comment.comment }}
            </div>
            <div class="leader-container">
              <avatar class="avatar" :source="comment.logo || null" />
              <div class="leader-name">
                {{ comment.name }}
              </div>
            </div>
          </div>
        </div>
        <template #prevArrow="">
          <div class="prevButton desktop">
            <img
              class="slick-icon"
              src="/img/comments-arrow-right.svg"
              alt="prev"
            />
          </div>
        </template>
        <template #nextArrow="">
          <div class="nextButton desktop">
            <img
              class="slick-icon"
              src="/img/comments-arrow-left.svg"
              alt="prev"
            />
          </div>
        </template>
      </vue-slick-carousel>
    </div>
  </div>
</template>
<script lang="ts">
import Vue from 'vue'
import VueSlickCarousel from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'

// components
import Avatar from '~/components/Avatar.vue'

export default Vue.extend({
  name: 'Comments',
  components: { VueSlickCarousel, Avatar },
  data: () => ({
    comments: [
      {
        name: '',
        comment:
          'داخل منزل ما پر از گل و گیاه است. پدر من به شدت به نگهداری از گل و گیاه علاقه‌مند بوده و هست اما هیچ‌وقت یک مرجع اطلاعاتی خوب، جایی برای ثبت وضعیت گیاهانش و مدیریت اطلاعات این تعداد زیاد گیاه نداشت. بیلچه به پدرم کمک کرد تا با وجود فراموش‌کاری، همیشه از آخرین وضعیت هر گیاهش خبر داشته باشد و راه حل و طریقه‌ی انجام هر کاری در مورد آن‌ها را پیدا کند.',
      },
      {
        name: '',
        comment:
          'مادرم علاقه زیادی به گل و گیاه داره و همیشه دوست داره گیاهان جدید بخره ولی چون روش نگهداری شون رو بلد نیست همیشه تجربه‌ی بدی داشت و اغلب اوقات خراب میشدن. حالا با بیلچه تونستیم اطلاعات خوبی کسب کنیم و راه و روش نگهداری از گیاهان جدید رو یاد بگیریم.',
      },
      {
        name: '',
        comment:
          'من همیشه در نگهداری از کاکتوس هایم مشکل داشتم چون هیچوقت اسم و گونه آنها را نمیشناختم و نمیدانستم میزان آب و نور و... مورد نیازشان چیست و در اکثر موارد در نگهداری از آن ها با شکست مواجه می‌شدم. بیلچه به من در تکرار نشدن این تجربه‌های بد کمک زیادی می‌کند و باعث شده بدون احساس گناه از خشکاندن گیاه وقتی گیاه زیبایی میبینم بخرم',
      },
    ],
    carouselSettings: {
      itemsToShow: 1,
      dots: false,
      infinite: true,
      speed: 500,
      slidesToShow: 1,
      initialSlide: 1,
      slidesToScroll: 1,
      arrows: true,
      autoplay: true,
      autoplaySpeed: 5000,
    },
  }),
})
</script>
<style scoped lang="scss">
.comments {
  position: relative;
  width: 100%;
  background: #fff4eb;
  min-height: 385px;
  padding-bottom: 50px;
}
.comments-container {
  width: 76%;
  margin: 0 auto;
  padding-top: 20px;
}
.title {
  font-weight: 500;
  font-size: 28px;
  line-height: 48px;
  margin-bottom: 32px;
}
.comments-quote {
  display: flex;
  justify-content: center;
  padding-top: 75px;
  margin-bottom: 42px;
}
.comment-container {
  position: relative;
  max-width: 776px;
  height: 167px;
  background: #ffffff;
  box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.12);
  border-radius: 50px 0px;
  margin: 0 auto;
  padding: 34px 30px;
  box-sizing: border-box;
  display: flex;
  align-items: center;
}
.qoute-icon {
  position: absolute;
  top: 12px;
  right: 15px;
}
.comment-text {
  font-size: 16px;
  line-height: 22px;
  text-align: right;
  color: $gray-10;
}
.outer-container {
  height: 212px;
  width: 80%;
}
.leader-container ::v-deep {
  display: flex;
  align-items: flex-end;
  position: absolute;
  bottom: -65px;
  .leader-name {
    font-weight: 500;
    font-size: 14px;
    line-height: 22px;
    text-align: center;
    color: $gray-10;
  }
  .avatar {
    margin-bottom: 22px;
  }
  .avatar,
  .avatar-container img {
    width: 85px !important;
    height: 85px !important;
  }
}
::v-deep .slick-dots li {
  button {
    width: 12px;
    height: 12px;
    background: #ffffff;
    border-radius: 50%;
    border: 1px solid #cccccc;
    &::before {
      display: none;
    }
  }

  &.slick-active {
    button {
      background: #fdbb11 !important;
      border: none !important;
    }
  }
}
.nextButton {
  left: 100px;
  .slick-icon {
    margin-top: -50px;
    z-index: 10;
  }
}
.prevButton {
  right: 100px;
  .slick-icon {
    margin-top: -50px;
    z-index: 10;
  }
}
.nextButton:before,
.prevButton:before {
  content: none !important;
}
@media (max-width: 768px) {
  .comments {
    min-height: 445px;
  }
  .comments-container {
    width: calc(100% - 30px);
  }
  .comments-quote {
    padding-top: 55px;
    margin-bottom: 36px;
  }
  .comment-container {
    height: 220px;
    padding: 36px 27px;
  }
  .leader-container ::v-deep {
    bottom: -35px;
    .leader-name {
      font-size: 13px;
      line-height: 20px;
    }
    .avatar {
      margin-bottom: 0px;
    }
    .avatar,
    .avatar-container img {
      width: 75px !important;
      height: 75px !important;
    }
  }
  .comment-text {
    font-size: 14px;
    line-height: 23px;
  }
  .outer-container {
    height: 260px;
  }
}
</style>
