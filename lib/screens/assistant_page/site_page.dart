import 'package:bilche/utilities/app_constants.dart';
import 'package:bilche/utilities/themes/text_styles.dart';
import 'package:bilche/widgets/app_bar.dart';
import 'package:bilche/widgets/bottom_sheet.dart';
import 'package:bilche/widgets/custom_widgets/plant_card.dart';
import 'package:bilche/widgets/menu_item.dart';
import 'package:bilche/widgets/table.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class SitePage extends StatelessWidget {
  const SitePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Directionality(
      textDirection: TextDirection.rtl,
      child: Scaffold(
        appBar: BAppBar(
          title: Text(
            'گلخانه فلان',
            style: BTypography.headline3,
          ),
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
                onTap: () => bottomSheet(
                      context,
                      title: 'افزودن',
                      body: <MenuItem>[
                        MenuItem(
                          text: 'گلخانه',
                          onTap: () {
                            print('Sosk');
                          },
                        ),
                        MenuItem(
                          text: 'گیاه',
                          leading: Icon(CupertinoIcons.plus),
                        ),
                        MenuItem(
                          text: 'فعالیت',
                          leading: Icon(CupertinoIcons.plus),
                          trailing: Icon(CupertinoIcons.plus),
                          hasDivider: false,
                        ),
                      ],
                    )),
          ],
        ),
        body: Padding(
          padding: scaffoldPadding,
          child: Wrap(
            crossAxisAlignment: WrapCrossAlignment.start,
            runSpacing: extraSpacing,
            children: [
              Text('گیاهان', style: BTypography.subtitle1),
              BTable(
                crossAxisCount: 2,
                children: [
                  PlantCard(
                    title: 'گلخانه فلان',
                    image: AssetImage('assets/images/images.jpg'),
                  ),
                  PlantCard(
                    title: 'گلخانه فلان',
                    image: AssetImage('assets/images/images.jpg'),
                  ),
                  PlantCard(
                    title: 'گلخانه فلان',
                    image: AssetImage('assets/images/images.jpg'),
                  ),
                ],
              )
            ],
          ),
        ),
      ),
    );
  }
}
