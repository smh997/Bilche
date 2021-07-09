import 'package:bilche/providers/sign_in_provider.dart';
import 'package:bilche/screens/assistant_page/assistant_page.dart';
import 'package:bilche/screens/sign_in/sign_in_pass.dart';
import 'package:bilche/utilities/app_constants.dart';
import 'package:bilche/utilities/sizes_helpers.dart';
import 'package:bilche/utilities/themes/colors.dart';
import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:provider/provider.dart';

class Splash extends StatefulWidget {
  @override
  _SplashState createState() => _SplashState();
}

class _SplashState extends State<Splash> {
  Future disposeSplash() async {
    await Future.delayed(Duration(seconds: 2)).then((value) async {
      var provider = Provider.of<SignInProvider>(context, listen: false);
      await provider.getFromPreferences();
      Navigator.pushReplacement(
          context,
          MaterialPageRoute(
            builder: (context) => (provider.user != null)
                ? AssistantPage()
                : SignInPasswordPage(),
          ));
    });
  }

  @override
  initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
      future: disposeSplash(),
      builder: (context, snapshot) => Container(
        color: GrayColor.white,
        child: Stack(
          children: <Widget>[
            Positioned(
              bottom: displaySize(context).height / 2,
              right: d56,
              left: d56,
              child: Image(
                fit: BoxFit.cover,
                image: AssetImage(
                  "assets/bilche_logo/Logo.png",
                ),
              ),
            ),
            Positioned(
              right: 0,
              left: 0,
              bottom: displayHeight(context) / 4,
              child: SpinKitThreeBounce(
                color: PrimaryColor.main,
                size: 20,
                duration: Duration(milliseconds: 800),
              ),
            )
          ],
        ),
      ),
    );
  }
}
