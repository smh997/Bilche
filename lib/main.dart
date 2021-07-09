import 'package:bilche/providers/sign_in_provider.dart';
import 'package:bilche/providers/sign_up_provider.dart';
import 'package:bilche/screens/intro/splash.dart';
import 'package:bilche/utilities/themes/themes_config.dart';
import 'package:flutter/material.dart';
import 'package:overlay_support/overlay_support.dart';
import 'package:provider/provider.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (context) => SignInProvider()),
        ChangeNotifierProvider(create: (context) => SignUpProvider()),
        // ChangeNotifierProvider(create: (context) => UserProvider()),
      ],
      child: OverlaySupport.global(
        child: MaterialApp(
          title: 'Bilche App',
          theme: BTheme.light,
          home: Splash(),
        ),
      ),
    );
  }
}
