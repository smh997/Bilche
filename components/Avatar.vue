<template>
  <div
    class="avatar-container"
    :style="{ height: `${size}px`, width: `${size}px` }"
  >
    <img
      v-if="source"
      :src="source"
      :style="{ height: `${size}px`, width: `${size}px` }"
    />
    <ig-icon
      v-else
      icon="user"
      color="var(--gray-70)"
      :size="size / 2.2"
      :font-weight="300"
    />
  </div>
</template>

<script lang="ts">
import Vue, { PropType } from 'vue'

import IgIcon from '~/components/IgIcon.vue'

export default Vue.extend({
  name: 'Avatar',
  components: { IgIcon },
  props: {
    size: {
      type: [Number, String],
      default: 45,
    },
    source: {
      type: String as PropType<string | null | undefined>,
      default: null,
    },
  },
})
</script>

<style scoped lang="scss">
.avatar-container {
  display: flex;
  align-items: center;
  justify-content: center;
  background: #e7e7e7;
  border-radius: 100%;
  overflow: hidden;

  img {
    object-fit: cover;
  }
}
</style>
