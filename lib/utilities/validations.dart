//This File Contains Validator functions that are used through the Project.

String? validateEmail(String? email) {
  if (isValidEmail(email!)) return null;
  return 'فرمت ایمیل باید صحیح باشد!';
}

String? validatePassword(String? pass) {
  if (pass!.length < 8) return 'حداقل 8 کاراکتر';
  return null;
}

String? validateRepeatedPassword(String? pass, String? repass) {
  if (pass != repass) return 'با رمز عبور مطابقت ندارد!';
  return null;
}

String? validateNotnull(String? value) {
  if (value == null || value == '') return 'نمی‌تواند خالی باشد';
  return null;
}

bool isValidPhoneNumber(String phoneNumber) =>
    RegExp(r"^(\+98|0)?9\d{9}$").hasMatch(phoneNumber);

bool isValidEmail(String email) => RegExp(
        r"^[a-zA-Z0-9.a-zA-Z0-9.!#$%&'*+-/=?^_`{|}~]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
    .hasMatch(email);
