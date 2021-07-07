<template functional>
  <div class="ig-inputs-container">
    <div
      v-if="!props.hideContainer"
      class="tg-regular label"
      :class="{ 'disabled-label': props.disabled }"
    >
      {{ props.label }}
    </div>
    <slot />
    <div
      v-if="props.invalid && props.errorText"
      class="tg-label-light error-text"
      :class="{ shake: props.invalid }"
    >
      {{ props.errorText }}
    </div>
    <div v-if="!props.hideContainer" class="tg-label-light description">
      {{ props.description }}
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

export const inputContainerProps = {
  label: {
    type: String,
    default: '',
  },
  errorText: {
    type: String,
    default: '',
  },
  description: {
    type: String,
    default: '',
  },
  disabled: {
    type: Boolean,
    default: false,
  },
  invalid: {
    type: Boolean,
    default: false,
  },
  required: {
    type: Boolean,
    default: false,
  },
  hideContainer: {
    type: Boolean,
    default: false,
  },
}
export default Vue.extend({
  name: 'IgInputsContainer',
  props: inputContainerProps,
})
</script>

<style scoped lang="scss">
.ig-inputs-container {
  position: relative;
  display: flex;
  flex-direction: column;
  width: 100%;
  height: fit-content;
}
.label {
  margin-bottom: 5px;
  &.disabled-label {
    color: $gray-50;
  }
}
//
.error-text {
  position: absolute;
  bottom: 0px;
  right: 15px;
  color: $alert-red;
  padding: 0 5px;
  z-index: 1001;
}
.description {
  margin-top: 5px;
  // color: $gray-50;
  min-height: 19px;
}
</style>
