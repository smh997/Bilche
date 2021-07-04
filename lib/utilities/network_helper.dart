import 'dart:convert';
import 'dart:io';

import 'package:http/http.dart' as http;
import 'package:http_parser/http_parser.dart';

class NetworkHelper {
  NetworkHelper({required this.url, this.token});

  Uri url;
  String? token;
  static const Map<String, String> baseHeader = <String, String>{
    "accept": "*/*",
    "Content-Type": "application/json; charset=UTF-8",
  };

  http.Response? _response;
  int? _statusCode;
  String? _body;

  http.Response? get response => _response;
  int? get statusCode => _statusCode;
  String? get body => _body;

  //methods
  httpGet({
    Map<String, String>? headers,
  }) async {
    print('GET: ' + url.path);
    return http
        .get(url,
            headers: headers ?? {"Authorization": "Bearer $token"}
              ..addAll(baseHeader))
        .then((value) {
      _response = value;
      _statusCode = _response?.statusCode;
      _body = _response?.body;
      // print(jsonEncode(_body));
    }).timeout(Duration(seconds: 10), onTimeout: () {
      throw ('TimeOut Error!');
    }).catchError((error) {
      _statusCode = 0;
      print(error);
    });
  }

  httpPost(
      {Map<String, String>? headers,
      body,
      Encoding? encoding,
      bool jsonEncoding = true}) async {
    print('POST: ' + url.path);
    print('=> Request Body: ' + jsonEncode(body));
    return await http
        .post(url,
            headers: headers ?? {"Authorization": "Bearer $token"}
              ..addAll(baseHeader),
            body: jsonEncoding ? jsonEncode(body) : body,
            encoding: encoding)
        .then((value) {
      _response = value;
      _statusCode = _response?.statusCode;
      _body = _response?.body;
      // print(jsonEncode(_body));
    }).timeout(Duration(seconds: 10), onTimeout: () {
      throw ('TimeOut Error!');
    }).catchError((error) {
      _statusCode = 0;
      print(error);
    });
  }

  httpDelete({Map<String, String>? headers, bool jsonEncoding = true}) async {
    print('DELETE: ' + url.path);
    return await http
        .delete(
      url,
      headers: headers ?? {"Authorization": "Bearer $token"}
        ..addAll(baseHeader),
    )
        .then((value) {
      _response = value;
      _statusCode = _response?.statusCode;
      _body = _response?.body;
      // print(jsonEncode(_body));
    }).timeout(Duration(seconds: 10), onTimeout: () {
      throw ('TimeOut Error!');
    }).catchError((error) {
      _statusCode = 0;
      print(error);
    });
  }

  httpPut({
    Map<String, String>? headers,
    body,
    Encoding? encoding,
  }) async {
    print('PUT: ' + url.path);
    return await http
        .put(url,
            headers: headers ?? {"Authorization": "Bearer $token"}
              ..addAll(baseHeader),
            body: jsonEncode(body),
            encoding: encoding)
        .then((value) {
      _response = value;
      _statusCode = _response?.statusCode;
      _body = _response?.body;
      // print(jsonEncode(_body));
    }).timeout(Duration(seconds: 10), onTimeout: () {
      throw ('TimeOut Error!');
    }).catchError((error) {
      _statusCode = 0;
      print(error);
    });
  }

  httpMultipartRequest(
      {List<String>? fileDirectories, required File imageFile}) async {
    var request = http.MultipartRequest('POST', url);
    var h = <String, String>{
      "Content-Type": "multipart/form-data",
      "accept": "application/json",
      if (token != null) "Authorization": "Bearer $token",
    };
    request.headers.addAll(h);
    request.files.add(http.MultipartFile(
        'file', imageFile.readAsBytes().asStream(), imageFile.lengthSync(),
        filename: 'image', contentType: MediaType('image', 'jpeg')));
    print(request.files);
    return await request.send().then((streamedResponse) async {
      _response = await http.Response.fromStream(streamedResponse);
      _statusCode = _response?.statusCode;
      _body = _response?.body;
      // print(jsonEncode(_body));
    }).timeout(Duration(seconds: 10), onTimeout: () {
      throw ('TimeOut Error!');
    }).catchError((error) {
      _statusCode = 0;
      print(error);
    });
  }
}
