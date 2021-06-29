type PropertyValidation = {
  isValid?: boolean
  isRequired?: boolean
}
type FormValidation<T> = {
  [k in keyof T]?: PropertyValidation
}

type ChangeByIndex<T> = Partial<T> & { index: number }

declare module '*.json' {
  const value: any
  export default value
}

declare module '~/assets/scss/theme-colors.scss' {
  const value: any
  export const paletteFirstColor: any
  export const paletteSecondColor: any
  export const paletteThirdColor: any
  export const paletteForthColor: any
  export const paletteFifthColor: any
  export const paletteSixthColor: any
  export default value
}
