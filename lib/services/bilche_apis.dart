class BilcheAPI {
  static String _host = 'http://10.0.2.2';
  static int _port = 8000;

  static String baseURL = '$_host:$_port/';

  static get login => Uri.parse('${baseURL}api/accounts/login/');
  static get register => Uri.parse('${baseURL}api/accounts/register/');
}
