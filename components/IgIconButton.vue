<template>
  <button
    class="ig-icon-button"
    :class="{ 'shadow-level1': hasShadow }"
    :disabled="disabled"
    :style="{ '--color': color, '--background': background }"
    @click="$emit('click')"
  >
    <ig-icon
      class="icon"
      :icon="icon"
      :type="iconType"
      :size="iconSize"
      :font-weight="400"
    />
  </button>
</template>
<script lang="ts">
import Vue, { PropType } from 'vue'

// global components
import IgIcon, { IconType } from '~/components/IgIcon.vue'

export default Vue.extend({
  name: 'IgIconButton',
  components: { IgIcon },
  props: {
    color: {
      type: String,
      default: 'var(--palette-primary)',
    },
    background: {
      type: String,
      default: 'var(--gray-100)',
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    icon: {
      type: String,
      required: true,
    },
    iconType: {
      type: String as PropType<IconType>,
      default: 'fas',
    },
    iconSize: {
      type: Number,
      default: 15,
    },
    hasShadow: {
      type: Boolean,
      default: true,
    },
  },
})
</script>

<style scoped lang="scss">
.ig-icon-button {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background: var(--background);
  border-radius: 100%;
  border: 0;
  outline: none;
  cursor: pointer;
  overflow: hidden;
  box-sizing: border-box;
  &:hover {
    box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.25);
  }

  .icon {
    color: var(--color) !important;
  }

  &:active {
    box-shadow: 0px 0px 7px rgba(0, 0, 0, 0.1);
    background: var(--color);
    .icon {
      color: var(--background) !important;
    }
  }

  &:disabled {
    background: $gray-95;
    cursor: not-allowed;
    box-shadow: none;
    .icon {
      color: $gray-80 !important;
    }
  }
}
</style>
