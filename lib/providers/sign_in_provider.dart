import 'dart:convert';

import 'package:bilche/models/my_auth_token.dart';
import 'package:bilche/models/user.dart';
import 'package:bilche/providers/base_provider.dart';
import 'package:bilche/services/bilche_apis.dart';
import 'package:bilche/utilities/network_helper.dart';
import 'package:shared_preferences/shared_preferences.dart';

class SignInProvider extends BaseProvider {
  String? phone;
  String? email;
  String? password;
  User? _user;
  MyAuthToken? myAuthToken;
  String? _errorMessage;

  User? get user => _user;
  String? get errorMessage => _errorMessage;

  setUser(User value) => {_user = value, notifyListeners()};
  setPhone(String value) => {phone = value, notifyListeners()};
  setEmail(String value) => {email = value, notifyListeners()};
  setPassword(String value) => {password = value, notifyListeners()};

  login() async {
    var helper = NetworkHelper(url: BilcheAPI.login);
    myAuthToken = MyAuthToken(username: email!, password: password!);

    await helper.httpPost(body: myAuthToken!.toJson());

    if (helper.statusCode == 200) {
      _user = User.fromJson(jsonDecode(helper.body!)['user']!);
      myAuthToken!.token = jsonDecode(helper.body!)['token'];
      _user!.username = myAuthToken!.username;
      _saveToPreferences();
      return true;
    }
    _errorMessage = jsonDecode(helper.body!)['error'];
    return false;
  }

  _saveToPreferences() async {
    var sp = await SharedPreferences.getInstance();
    sp.setString('user', jsonEncode(_user!.toJson()));
    sp.setString('token', myAuthToken!.token!);
  }

  getFromPreferences() async {
    var sp = await SharedPreferences.getInstance();
    var json = sp.getString('user');
    var token = sp.getString('token');
    print(json);
    if (json != null && token != null) {
      Map<String, dynamic> tmp = jsonDecode(json);
      _user = User.fromJson(tmp);
      print(token);
      myAuthToken = MyAuthToken(
        username: _user!.username ?? '',
        password: _user!.password ?? '',
        token: token,
      );
    } else
      _user = null;
  }
}
