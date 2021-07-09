class MyAuthToken {
  String username;
  String password;
  String? token;

  MyAuthToken({required this.username, required this.password, this.token});

  factory MyAuthToken.fromJson(Map<String, dynamic> json) {
    return MyAuthToken(
        username: json['username'],
        password: json['password'],
        token: json['token']);
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['username'] = this.username;
    data['password'] = this.password;
    // data['token'] = this.token;
    return data;
  }
}
