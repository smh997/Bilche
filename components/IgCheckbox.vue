<template>
  <label
    class="ig-checkbox-container"
    :class="{ disabled: disabled, radio: isRadio }"
  >
    <input
      id="input-checkbox"
      class="input"
      type="checkbox"
      :value="value"
      :checked="value"
      :readonly="disabled"
      @change="!disabled && $emit('input', $event.target.checked)"
    />
    <ig-icon
      class="icon"
      :type="isRadio ? 'far' : 'fas'"
      color="var(--gray-100)"
      :icon="icon"
      :size="13"
    />
    <div v-if="label" class="tg-light checkbox-label">
      {{ label }}
    </div>
  </label>
</template>

<script lang="ts">
import Vue from 'vue'

// global components
import IgIcon from '~/components/IgIcon.vue'

export default Vue.extend({
  name: 'IgCheckbox',
  components: { IgIcon },
  props: {
    value: {
      type: Boolean,
      default: false,
    },
    label: {
      type: String,
      default: '',
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    isRadio: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    icon(): string {
      if (this.value) {
        if (this.isRadio) {
          return 'circle'
        } else {
          return 'check'
        }
      } else {
        return ''
      }
    },
  },
})
</script>

<style scoped lang="scss">
.ig-checkbox-container {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  height: 30px;
  box-sizing: border-box;
  font-style: normal;
  font-weight: normal;
  font-size: 14.5px;
  line-height: 23px;
  text-align: right;
  color: #2d2a22;
  cursor: pointer;

  &:hover > .icon {
    background: $palette-primary-light;
  }

  &.disabled {
    cursor: not-allowed;
    &:hover > .icon {
      background: unset;
    }
    .input:checked ~ .icon {
      background: $gray-90 !important;
    }
    .icon {
      border-color: $gray-90;
    }
  }

  .input:checked {
    ~ .icon {
      background: $palette-primary;
    }
  }

  &.radio {
    .icon {
      border-radius: 100%;
      &::before {
        // background: red;
        border-width: 2px;
        border-color: $gray-100;
      }
    }
  }
}
.icon {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 17px;
  width: 17px;
  background: $gray-100;
  border: 1px solid $palette-primary;
  border-radius: 4px;
  margin: 6.5px;
  box-sizing: border-box;
}

.checkbox-label {
  margin-right: 5px;
}

input {
  display: none;
}
</style>
