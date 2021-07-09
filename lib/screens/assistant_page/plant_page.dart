import 'package:bilche/utilities/app_constants.dart';
import 'package:bilche/utilities/themes/text_styles.dart';
import 'package:bilche/widgets/app_bar.dart';
import 'package:bilche/widgets/bottom_sheet.dart';
import 'package:bilche/widgets/menu_item.dart';
import 'package:bilche/widgets/notification.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import 'local_widgets/site_card.dart';

class SitePlantPage extends StatelessWidget {
  const SitePlantPage({Key? key}) : super(key: key);

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
            SizedBox(width: normalSpacing),
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
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text('پیام جدید', style: BTypography.subtitle1),
              SizedBox(height: extraSpacing),
              BNotificationCard(
                notificationType: NotificationType.Warning,
                title: 'تیتر پیام جدید',
                dateTime: DateTime.now().subtract(Duration(hours: 5)),
                message:
                    'این متن پیامی است که به شما ارسال شده است تا از محتوای آن آگاه شوید. کافی است برای رفع آن، اقدام به رسیدگی کنید.',
                onButtonTap: () {},
              ),
              SizedBox(height: extraSpacing),
              Text('گلخانه‌ها', style: BTypography.subtitle1),
              SizedBox(height: extraSpacing),
              SiteCard(
                title: 'گلخانه فلان',
                lightFactor: 'کم‌نور',
                tempFactor: 'استاندارد',
                humidityFactor: 'مرطوب',
                placeType: 'حمام و سرویس بهداشتی',
              ),
            ],
          ),
        ),
      ),
    );
  }
}
