<template functional>
  <div
    class="ig-loading"
    :class="{ absolute: props.absolute }"
    :style="{ '--color': props.color, '--scale': props.scale }"
  >
    <div v-for="n in 7" :key="n" />
  </div>
</template>
<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  name: 'IgLoading',
  props: {
    color: {
      type: String,
      default: 'var(--gray-100)',
    },
    scale: {
      type: Number,
      default: 1,
    },
    absolute: {
      type: Boolean,
      default: false,
    },
  },
})
</script>

<style scoped lang="scss">
.ig-loading {
  flex-shrink: 0;
  display: inline-block;
  width: 40px;
  height: 40px;
  transform: scale(var(--scale));

  &.absolute {
    position: absolute;
  }
}
.ig-loading div {
  animation: loading 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
  transform-origin: 20px 20px;
}
.ig-loading div:after {
  content: ' ';
  display: block;
  position: absolute;
  width: 7px;
  height: 7px;
  background: var(--color);
  border-radius: 50%;
  margin: -4px 0 0 -4px;
}
.ig-loading div:nth-child(1) {
  animation-delay: -0.036s;
}
.ig-loading div:nth-child(1):after {
  top: 31.5px;
  left: 31.5px;
}
.ig-loading div:nth-child(2) {
  animation-delay: -0.072s;
}
.ig-loading div:nth-child(2):after {
  top: 34px;
  left: 28px;
}
.ig-loading div:nth-child(3) {
  animation-delay: -0.108s;
}
.ig-loading div:nth-child(3):after {
  top: 35.5px;
  left: 24px;
}
.ig-loading div:nth-child(4) {
  animation-delay: -0.144s;
}
.ig-loading div:nth-child(4):after {
  top: 36px;
  left: 20px;
}
.ig-loading div:nth-child(5) {
  animation-delay: -0.18s;
}
.ig-loading div:nth-child(5):after {
  top: 35.5px;
  left: 16px;
}
.ig-loading div:nth-child(6) {
  animation-delay: -0.216s;
}
.ig-loading div:nth-child(6):after {
  top: 34px;
  left: 12px;
}
.ig-loading div:nth-child(7) {
  animation-delay: -0.252s;
}
.ig-loading div:nth-child(7):after {
  top: 31.5px;
  left: 8.5px;
}
@keyframes loading {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
