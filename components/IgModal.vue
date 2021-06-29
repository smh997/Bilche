<template>
  <client-only>
    <v-modal
      :style="{ '--background': backgroundColor }"
      :class="{ 'hide-shadow': hideShadow, 'show-overflow': showOverflow }"
      :name="name"
      :adaptive="adaptive"
      :scrollable="scrollable"
      :height="!isMobile ? height : '100%'"
      :min-height="minHeight"
      :max-height="maxHeight"
      :width="!isMobile ? width : '100%'"
      :min-width="minWidth"
      :max-width="maxWidth"
      :shift-x="shiftX"
      :shift-y="shiftY"
      :click-to-close="clickToClose"
      @opened="opened"
      @closed="closed"
    >
      <slot />
    </v-modal>
  </client-only>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'Modal',
  props: {
    value: {
      type: Boolean,
      default: false,
    },
    name: {
      type: String,
      required: true,
    },
    backgroundColor: {
      type: String,
      default: '#FFF',
    },
    hideShadow: {
      type: Boolean,
      default: false,
    },
    showOverflow: {
      type: Boolean,
      default: false,
    },
    adaptive: {
      type: Boolean,
      default: false,
    },
    scrollable: {
      type: Boolean,
      default: false,
    },
    height: {
      type: [Number, String],
      default: 'auto',
    },
    minHeight: {
      type: Number,
      default: 0,
    },
    maxHeight: {
      type: Number,
      default: Infinity,
    },
    width: {
      type: [Number, String],
      default: '100%',
    },
    minWidth: {
      type: Number,
      default: 0,
    },
    maxWidth: {
      type: Number,
      default: Infinity,
    },
    clickToClose: {
      type: Boolean,
      default: true,
    },
    shiftX: {
      type: Number,
      default: 0.5,
    },
    shiftY: {
      type: Number,
      default: 0.5,
    },
  },
  data: () => ({
    isMobile: false,
  }),
  watch: {
    value() {
      if (this.value) {
        this.show()
      } else {
        this.hide()
      }
    },
  },
  beforeMount() {
    if (window.innerWidth <= 768) {
      this.isMobile = true
    }
  },
  mounted() {
    setTimeout(() => {
      // next tick or normal not working
      if (this.value) {
        this.show()
      }
    })
  },
  methods: {
    show() {
      this.$modal.show(this.name)
      this.$emit('opened')
    },
    hide() {
      this.$modal.hide(this.name)
      this.$emit('closed')
    },
    opened() {
      this.$emit('input', true)
      this.$emit('opened')
    },
    closed() {
      this.$emit('input', false)
      this.$emit('closed')
    },
  },
})
</script>

<style scoped lang="scss">
.show-overflow ::v-deep {
  .vm--modal {
    overflow: visible !important;
  }
}

.hide-shadow ::v-deep {
  .vm--modal {
    box-shadow: none !important;
  }
}

.vm--container ::v-deep {
  direction: ltr;
  z-index: 100000 !important;

  .vm--modal {
    direction: rtl;
    background: var(--background) !important;
  }
}
</style>
