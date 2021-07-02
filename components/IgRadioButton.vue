<template>
  <div>
    <ig-checkbox
      v-for="radio in radios"
      :key="radio.value"
      is-radio
      :disabled="disabled"
      :value="checkedValue === radio.value"
      :label="radio.label"
      @input="() => onSelect(radio.value)"
    />
  </div>
</template>

<script lang="ts">
import Vue, { PropType } from 'vue'

// global components
import IgCheckbox from '~/components/IgCheckbox.vue'

// types
type Radio = {
  label: string
  value: any
}

export default Vue.extend({
  name: 'IgRadioButton',
  components: { IgCheckbox },
  props: {
    radios: {
      type: Array as PropType<Radio[]>,
      default: () => [],
    },
    value: {
      type: [Number, String],
      required: true,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      checkedValue: this.value,
    }
  },
  methods: {
    onSelect(value: any) {
      if (value) {
        this.checkedValue = value
        this.$emit('input', value)
      } else {
        this.$emit('input', null)
      }
    },
  },
})
</script>
