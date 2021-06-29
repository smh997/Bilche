<template>
  <i
    class="icon-container"
    :class="[type, `fa-${icon}`]"
    :style="{
      color: color,
      'font-size': `${size}px`,
      'font-weight': fontWeight,
    }"
    @mouseenter="$emit('mouseenter')"
    @mouseleave="$emit('mouseleave')"
    @click="$emit('click')"
  ></i>
</template>
<script lang="ts">
import Vue, { PropType } from 'vue'

// types
export type IconType = 'far' | 'fas' | 'fal' | 'fab'

export default Vue.extend({
  name: 'IgIcon',
  props: {
    type: {
      type: String as PropType<IconType>,
      default: 'fas',
    },
    icon: {
      type: String,
      default: '',
    },
    color: {
      type: String,
      default: '#FFF',
    },
    size: {
      type: Number,
      default: 16,
    },
    fontWeight: {
      type: [String, Number],
      default: '',
    },
  },
})
</script>

<style scoped lang="scss">
.icon-container {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
