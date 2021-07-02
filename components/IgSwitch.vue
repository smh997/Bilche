<template>
  <div class="ig-switch-container">
    <label class="switch" :class="[size, { disabled: disabled }]">
      <input
        id="input-checkbox"
        v-model="localState"
        class="input"
        type="checkbox"
        :disabled="disabled"
      />
      <span class="slider" />
    </label>
    <div v-if="localLabel" class="tg-light">
      {{ localLabel }}
    </div>
  </div>
</template>

<script lang="ts">
import Vue, { PropType } from 'vue'

// types
type Size = 'small' | 'big'

export default Vue.extend({
  name: 'IgSwitch',
  props: {
    value: {
      type: Boolean,
      default: false,
    },
    size: {
      type: String as PropType<Size>,
      default: 'small',
    },
    label: {
      type: String,
      default: '',
    },
    activeLabel: {
      type: String,
      default: '',
    },
    inactiveLabel: {
      type: String,
      default: '',
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    localState: {
      get(): boolean {
        return this.value
      },
      set(newValue: boolean) {
        this.$emit('input', newValue)
      },
    },
    localLabel(): string {
      if (this.activeLabel && this.inactiveLabel) {
        return this.localState ? this.activeLabel : this.inactiveLabel
      } else {
        return this.label
      }
    },
  },
})
</script>

<style scoped lang="scss">
.ig-switch-container {
  display: flex;
  justify-content: flex-start;
  align-items: center;

  .tg-light {
    margin-right: 10px;
  }
}

.switch {
  position: relative;
  display: inline-block;

  &.small {
    width: 28px;
    height: 17px;
    .slider:before {
      height: 13px;
      width: 13px;
    }
  }
  &.big {
    width: 45px;
    height: 25px;
    .slider:before {
      height: 21px;
      width: 21px;
    }
  }
  &.disabled {
    .slider {
      background: $gray-90 !important;
    }
  }

  input {
    visibility: hidden;
  }

  input:checked + .slider {
    background-color: $palette-primary;
  }

  input:checked + .slider:before {
    -webkit-transform: translateX(calc(100% - 2px));
    -ms-transform: translateX(calc(100% - 2px));
    transform: translateX(calc(100% - 2px));
  }
}
/* The slider */
.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: $gray-80;
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 34px;

  &:hover {
    background: $gray-70;
  }
}

.slider:before {
  position: absolute;
  content: '';
  left: 2px;
  bottom: 2px;
  background-color: white;
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 50%;
}
</style>
