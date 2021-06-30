import 'package:bilche/screens/assistant_page/local_widgets/site_card.dart';
import 'package:bilche/utilities/app_constants.dart';
import 'package:bilche/widgets/app_bar.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class AssistantPage extends StatelessWidget {
  const AssistantPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Directionality(
      textDirection: TextDirection.rtl,
      child: Scaffold(
        appBar: BAppBar(
          title: InkWell(
              child: Padding(
                  padding: buttonPadding,
                  child: Icon(Icons.notification_important_outlined)),
              onTap: () {}),
          actions: [
            InkWell(
                child: Padding(
                    padding: buttonPadding,
                    child: Icon(Icons.notification_important_outlined)),
                onTap: () {}),
            InkWell(
                child: Padding(
                    padding: buttonPadding,
                    child: Icon(Icons.notification_important_outlined)),
                onTap: () {}),
          ],
        ),
        body: Padding(
          padding: scaffoldPadding,
          child: Center(
              child: SiteCard(
            title: 'گلخانه فلان',
            lightFactor: 'کم‌نور',
            tempFactor: 'استاندارد',
            humidityFactor: 'مرطوب',
            placeType: 'حمام و سرویس بهداشتی',
          )),
        ),
      ),
    );
  }
}
