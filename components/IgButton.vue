<template>
  <button
    class="ig-button"
    :class="[
      type,
      size,
      secondaryColor,
      {
        loading: loading,
        'icon-right': iconPos === 'right',
        'icon-left': iconPos === 'left',
      },
    ]"
    :disabled="disabled"
    @click="!loading && $emit('click')"
  >
    <ig-loading
      v-if="loading"
      class="loading-component"
      :color="type === 'primary' ? 'var(--palette-primary)' : 'var(--gray-100)'"
      absolute
      :scale="scaleLoading"
    />
    <slot />
    <ig-icon
      v-if="icon !== ''"
      class="icon"
      :icon="icon"
      :type="iconType"
      :size="13"
    />
  </button>
</template>
<script lang="ts">
import Vue, { PropType } from 'vue'

// components
import IgIcon, { IconType } from '~/components/IgIcon.vue'
import IgLoading from '~/components/IgLoading.vue'

// types
type ButtonType = 'primary' | 'secondary'
type SecondaryColor = 'green' | 'orange'
type ButtonSize = 'small' | 'medium' | 'big'

export default Vue.extend({
  name: 'IgButton',
  components: { IgIcon, IgLoading },
  props: {
    type: {
      type: String as PropType<ButtonType>,
      default: 'primary',
    },
    secondaryColor: {
      type: String as PropType<SecondaryColor>,
      default: 'green',
    },
    size: {
      type: String as PropType<ButtonSize>,
      default: 'small',
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    loading: {
      type: Boolean,
      default: false,
    },
    iconPos: {
      type: String as PropType<'right' | 'left'>,
      default: 'left',
    },
    icon: {
      type: String,
      default: '',
    },
    iconType: {
      type: String as PropType<IconType>,
      default: 'far',
    },
  },
  computed: {
    scaleLoading(): number {
      if (this.size === 'medium') {
        return 0.85
      } else if (this.size === 'small') {
        return 0.65
      } else {
        return 1
      }
    },
  },
})
</script>

<style scoped lang="scss">
.ig-button {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  border: 0;
  outline: none;
  cursor: pointer;
  overflow: hidden;
  box-sizing: border-box;
  // text
  font-family: IRANSansWebFaNum;
  text-align: center;

  &.loading {
    cursor: progress !important;
    color: transparent !important;
    .icon {
      visibility: hidden;
    }
  }
  // icon pos
  &.icon-left {
    flex-direction: row;
    .icon {
      margin-right: 10px;
    }
  }
  &.icon-right {
    flex-direction: row-reverse;
    .icon {
      margin-left: 10px;
    }
  }

  // size
  &.big {
    height: 50px;
    padding: 10px 15px;
    // text
    @extend .tg-regular;
  }
  &.medium {
    height: 39px;
    padding: 10px 15px;
    // text
    @extend .tg-label-regular;
  }
  &.small {
    height: 29px;
    padding: 5px 10px;
    // text
    @extend .tg-label-regular;
  }

  // type
  &.primary {
    @extend .shadow-level1;
    background: $gray-100;
    color: $gray-00;
    .icon {
      color: $palette-primary !important;
    }
    &:hover {
      @extend .shadow-level2;
    }
    &:active {
      background: $palette-primary;
      color: $gray-100;
      box-shadow: none;
      .icon {
        color: $gray-100 !important;
      }
    }
    &:disabled {
      cursor: not-allowed;
      background: $gray-95;
      color: $gray-70;
      box-shadow: none;
      .icon {
        color: $gray-70 !important;
      }
      &:hover {
        border: none;
        background: $gray-95;
        box-shadow: none;
      }
    }
  }
  &.secondary {
    color: $gray-100;
    .icon {
      color: $gray-100 !important;
    }
    &.green {
      background: #32c770;
      &:hover {
        background: #32c770;
      }
      &:active {
        background: $palette-secondary;
      }
    }
    &.orange {
      background: $palette-primary;
      &:hover {
        background: #f26e0c;
      }
      &:active {
        background: #ff8326;
      }
    }

    &:disabled {
      cursor: not-allowed;
      background: $gray-90;
      color: $gray-70;
      box-shadow: none;
      .icon {
        color: $gray-70 !important;
      }
      &:hover {
        border: none;
        background: $gray-90;
        box-shadow: none;
      }
    }
  }
}
</style>
