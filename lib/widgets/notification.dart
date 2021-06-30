import 'package:bilche/utilities/app_constants.dart';
import 'package:bilche/utilities/themes/text_styles.dart';
import 'package:bilche/widgets/card.dart';
import 'package:bilche/widgets/push_button.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

enum NotificationType {
  Watering,
  Fertilizing,
  PlantCheckup,
  Warning,
  Suggestion
}

class BNotificationCard extends BCard {
  final String title;
  final NotificationType notificationType;
  final DateTime dateTime;
  final String message;
  final VoidCallback? onButtonTap;

  final AlignmentGeometry? alignment = Alignment.center;
  final EdgeInsetsGeometry? padding = mediumPadding;

  BNotificationCard({
    required this.title,
    required this.notificationType,
    required this.dateTime,
    required this.message,
    this.onButtonTap,
  }) : super(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Card(),
              //Title Bar
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  //Type and Title
                  Row(
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      Icon(Icons.notification_important),
                      SizedBox(width: normalSpacing),
                      Text(title, style: BTypography.bodyText1),
                    ],
                  ),
                  //Date Time
                  Text(
                    (DateTime.now().difference(dateTime).inHours.toString()) +
                        ' ساعت پیش',
                    style: BTypography.overline,
                  )
                ],
              ),
              SizedBox(height: mediumSpacing),
              //Message
              Text(message, style: BTypography.caption),
              SizedBox(height: mediumSpacing),
              BPushButton(
                text: 'مشاهده',
                type: ButtonType.TextOnly,
                onTap: onButtonTap,
              )
            ],
          ),
        );
}
