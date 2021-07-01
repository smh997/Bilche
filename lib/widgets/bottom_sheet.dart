import 'package:bilche/utilities/app_constants.dart';
import 'package:bilche/utilities/themes/colors.dart';
import 'package:bilche/utilities/themes/text_styles.dart';
import 'package:bilche/widgets/menu_item.dart';
import 'package:flutter/material.dart';

Future<dynamic> bottomSheet(BuildContext context,
        {required String title, required List<MenuItem> body}) =>
    showModalBottomSheet(
      backgroundColor: Colors.transparent,
      useRootNavigator: true,
      context: context,
      builder: (context) => Container(
        decoration: BoxDecoration(
          color: GrayColor.white,
          borderRadius: BorderRadius.only(
            topLeft: Radius.circular(extraSpacing),
            topRight: Radius.circular(extraSpacing),
          ),
        ),
        padding: cardPadding,
        width: double.infinity,
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Container(
                width: d36,
                child:
                    Divider(thickness: d4, height: d4, color: GrayColor.g50)),
            SizedBox(height: mediumSpacing),
            Directionality(
              textDirection: TextDirection.rtl,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  Text(title, style: BTypography.subtitle1),
                  SizedBox(height: hugeSpacing),
                  Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: body,
                  )
                ],
              ),
            ),
          ],
        ),
      ),
    );
