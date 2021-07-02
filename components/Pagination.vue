<template>
  <div v-show="count > 0" class="pagination-container">
    <ig-icon
      style="margin-left: 60px"
      icon="angle-right"
      color="#999999"
      :size="25"
      @click="value > 1 && $emit('input', value - 1)"
    />
    <div class="num-list">
      <a
        v-for="num in count"
        v-show="
          count < 7 ||
          num == 1 ||
          num == count ||
          (Math.abs(num - value) <= 3 && Math.abs(num - value) >= 0)
        "
        :key="num"
        class="num"
        :class="{ selected: value === num }"
        @click="$emit('input', num)"
      >
        {{
          Math.abs(num - value) == 3 && num != 1 && num != count ? '...' : num
        }}
      </a>
    </div>
    <ig-icon
      icon="angle-left"
      color="#999999"
      style="margin-right: 60px"
      :size="25"
      @click="value < count && $emit('input', value + 1)"
    />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

// global components
import IgIcon from '~/components/IgIcon.vue'

export default Vue.extend({
  name: 'DashboardHeader',
  components: { IgIcon },
  props: {
    value: {
      type: Number,
      required: true,
    },
    count: {
      type: Number,
      required: true,
    },
  },
})
</script>
<style lang="scss" scoped>
.pagination-container {
  align-self: center;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 90%;
  margin: 30px 0;
}
.num-list {
  display: flex;
  align-items: center;
  justify-content: center;
}

.num {
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 10px;
  box-sizing: border-box;
  cursor: pointer;
  margin: 0 20px;
  // text
  font-size: 25px;
  line-height: 29px;
  text-align: center;
  color: #999999;

  &:hover {
    background: #efefef;
  }

  &.selected {
    background: #27ae60;
    // text
    font-style: normal;
    font-weight: 500;
    color: #ffffff;
  }
}

@media print {
  .pagination-container {
    display: none;
  }
}
</style>
