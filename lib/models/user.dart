class User {
  String? username;
  String? password;
  String email;
  String? level;
  String? fullname;
  String? phoneNumber;
  bool? isGardener;
  String? preferredHour;
  String? sPreferredDays;

  User(
      {this.username,
      this.password,
      required this.email,
      this.level,
      this.fullname,
      this.phoneNumber,
      this.isGardener,
      this.preferredHour,
      this.sPreferredDays});

  factory User.fromJson(Map<String, dynamic> json) {
    print(json);
    return User(
        username: json['username'],
        password: json['password'],
        email: json['email'] ?? '',
        level: json['level'],
        fullname: json['fullname'],
        phoneNumber: json['phone_number'],
        isGardener: json['is_gardener'],
        preferredHour: json['preferred_hour'],
        sPreferredDays: json['_preferred_days']);
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['username'] = this.username;
    data['password'] = this.password;
    data['email'] = this.email;
    // data['level'] = this.level;
    data['fullname'] = this.fullname;
    // data['phone_number'] = this.phoneNumber;
    // data['is_gardener'] = this.isGardener;
    // data['preferred_hour'] = this.preferredHour;
    // data['_preferred_days'] = this.sPreferredDays;
    return data;
  }
}
