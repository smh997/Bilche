import 'package:bilche/screens/assistant_page/assistant_page.dart';
import 'package:bilche/utilities/themes/themes_config.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: BTheme.light,
      home: AssistantPage(),
    );
  }
}
