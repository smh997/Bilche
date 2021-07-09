import 'dart:convert';

import 'package:bilche/models/user.dart';
import 'package:bilche/providers/base_provider.dart';
import 'package:bilche/services/bilche_apis.dart';
import 'package:bilche/utilities/network_helper.dart';

class SignUpProvider extends BaseProvider {
  String? fullName;
  String? phone;
  String? email;
  String? password;
  User? user;
  String? _errorMessage;

  setName(value) => {fullName = value, notifyListeners()};
  setPhone(value) => {phone = value, notifyListeners()};
  setEmail(value) => {email = value, notifyListeners()};
  setPassword(value) => {password = value, notifyListeners()};

  String? get errorMessage => _errorMessage;

  register() async {
    var helper = NetworkHelper(url: BilcheAPI.register);
    user = User(
        fullname: fullName,
        username: email!,
        password: password!,
        email: email!);
    await helper.httpPost(body: user!.toJson());
    if (helper.statusCode == 201) return true;
    _errorMessage = jsonDecode(helper.body!)['error'];
    return false;
  }
}
