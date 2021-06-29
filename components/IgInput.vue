<template>
  <ig-inputs-container
    v-bind="$props"
    :invalid="localInvalid"
    :error-text="errorTxt"
  >
    <label class="input-container" :class="{ textarea: textArea }">
      <input
        v-if="!textArea"
        ref="input"
        v-model="localValue"
        class="input"
        :class="{
          invalid: localInvalid,
          success: isSuccess,
          'with-button': withButton,
        }"
        :type="type"
        :min="min"
        :max="max"
        :placeholder="placeholder"
        :maxlength="maxLength"
        :minlength="minLength"
        :readonly="disabled"
        :autocomplete="autocomplete"
        @keypress.enter.prevent="$emit('submit')"
        @keypress="$emit('keypress', $event)"
        @focus="$emit('focus')"
        @blur="$emit('blur')"
      />
      <textarea
        v-else
        v-model="localValue"
        class="input textarea"
        :class="{ 'disable-resizable': !resizable }"
        :min="min"
        :max="max"
        :placeholder="placeholder"
        :maxlength="maxLength"
        :minlength="minLength"
        :readonly="disabled"
        :autocomplete="autocomplete"
      />
      <ig-icon
        class="input-icon"
        :icon="icon"
        :color="localInvalid ? 'var(--alert-red)' : 'var(--gray-70)'"
        :size="20"
        :font-weight="300"
        :type="iconType"
      />
      <button
        v-if="withButton"
        class="input-button"
        :class="{ 'is-loading': isLoading }"
      >
        <div v-show="isLoading">
          <ig-loading :scale="0.5" color="var(--palette-primary)" />
        </div>
        <div v-show="!isLoading" class="button-label">
          {{ buttonText }}
        </div>
      </button>
    </label>
  </ig-inputs-container>
</template>

<script lang="ts">
import Vue, { PropType } from 'vue'

// global components
import IgInputsContainer, {
  inputContainerProps,
} from '~/components/IgInputsContainer.vue'
import IgIcon, { IconType } from '~/components/IgIcon.vue'
import IgLoading from '~/components/IgLoading.vue'

export default Vue.extend({
  name: 'IgInput',
  components: { IgIcon, IgInputsContainer, IgLoading },
  props: {
    ...inputContainerProps,
    validation: {
      type: Function,
      default: null,
    },
    value: {
      type: [String, Number] as PropType<string | number | null>,
      default: '',
    },
    icon: {
      type: String,
      default: '',
    },
    iconType: {
      type: String as PropType<IconType>,
      default: 'far',
    },
    placeholder: {
      type: String,
      default: '',
    },
    type: {
      type: String,
      default: 'text',
    },
    min: {
      type: Number,
      default: Infinity,
    },
    max: {
      type: Number,
      default: Infinity,
    },
    minLength: {
      type: Number,
      default: 0,
    },
    maxLength: {
      type: Number,
      default: Infinity,
    },
    autocomplete: {
      type: String,
      default: 'on',
    },
    withButton: {
      type: Boolean,
      default: false,
    },
    buttonText: {
      type: String,
      default: '',
    },
    isLoading: {
      type: Boolean,
      default: false,
    },
    isSuccess: {
      type: Boolean,
      default: false,
    },
    textArea: {
      type: Boolean,
      default: false,
    },
    resizable: {
      type: Boolean,
      default: true,
    },
  },
  computed: {
    errorTxt(): string {
      if (this.localInvalid) {
        if (this.required && !this.value) {
          return 'خطا: این فیلد نمی‌تواند خالی باشد.'
        } else {
          return 'خطا: مقدار واردشده معتبر نیست.'
        }
      } else {
        return ''
      }
    },
    localValue: {
      get(): any {
        return this.value
      },
      set(value: any): void {
        this.$emit('input', value)
      },
    },
    localInvalid(): boolean {
      if (this.validation) {
        return this.invalid && !this.validation(this.localValue)
      } else {
        return this.invalid
      }
    },
  },
  methods: {
    handleEvent(event: any) {
      this.$emit(event)
    },
  },
})
</script>

<style scoped lang="scss">
.input-container {
  position: relative;
  height: 50px;

  .input-icon {
    position: absolute;
    left: 17px;
    top: 50%;
    transform: translate(0, -50%);
  }

  &.textarea {
    height: 100%;
    width: 100%;

    .input-icon {
      top: 15px;
      transform: unset;
    }
  }
}

.input {
  width: 100%;
  height: 100%;
  font-family: IRANSansWebFaNum;
  // background: $gray-100;
  // border: 1px solid $gray-90;
  border-radius: 20px;
  text-align: right;
  padding: 0px 15px;
  // caret-color: $palette-primary;
  outline: none;
  // text
  // color: $gray-00;
  font-size: 13px;
  line-height: 30px;

  &.invalid {
    // border-color: $alert-red !important;
    // color: $alert-red;
  }
  &.success {
    // background: $alert-green-light;
    // border-color: $alert-green;
    // color: $alert-green;
    ~ .input-button > .tg-label-medium {
      // color: $alert-green !important;
    }
  }

  &.textarea {
    min-height: 140px;
    width: 100%;
    padding-top: 10px;

    &.disable-resizable {
      resize: none;
    }
  }

  &.with-button {
    padding-left: 65px;
  }
}
.input::placeholder {
  font-family: IRANSansWebFaNum;
  // color: $gray-70;
  font-weight: 300;
  font-size: 13px;
  line-height: 30px;
}
.input:focus {
  // border-color: $palette-primary;
}
.input:read-only {
  cursor: not-allowed;
  // background: $gray-95;
  // border-color: $gray-90;
}
// button
.input-button {
  position: absolute;
  left: 5px;
  top: 50%;
  transform: translate(0, -50%);
  display: flex;
  align-items: center;
  justify-content: center;
  width: 56px;
  height: 40px;
  // background: $gray-100;
  padding: 10px 15px;
  border-radius: 20px;
  border: 0;
  outline: none;
  cursor: pointer;
  overflow: hidden;
  box-sizing: border-box;
  // text
  font-family: IRANSansWebFaNum;
  text-align: center;

  &:hover {
    // background: $palette-primary-light;
  }

  &.is-loading {
    // background: $palette-primary-light;
    div {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 20px;
      height: 20px;
    }
  }

  .button-label {
    // @include tg-label-medium;
    // color: $palette-primary;
    font-size: 13px;
  }
}
</style>
