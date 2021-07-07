export const phoneNumberValidation = (text: string) => {
  const phone =
    /^\(?([0]{1})\)?[-. ]?([9]{1})[-. ]?[-. ]?([0-9]{2})[-. ]?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/
  if (text && text.match(phone)) {
    return true
  } else {
    return false
  }
}

export const validateEmail = (text: string): boolean => {
  const email =
    /^(([^<>()\\[\]\\.,;:\s@"]+(\.[^<>()\\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
  return !!text.match(email)
}
