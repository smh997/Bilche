import 'package:bilche/utilities/app_constants.dart';
import 'package:bilche/utilities/themes/colors.dart';
import 'package:bilche/utilities/themes/text_styles.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

enum ButtonType { Contained, Outlined, TextOnly }

class BPushButton extends StatelessWidget {
  BPushButton(
      {this.text,
      this.icon,
      this.onTap,
      this.type = ButtonType.Contained,
      this.isRound = false});

  final String? text;
  final IconData? icon;
  final bool isRound;
  final ButtonType type;
  final VoidCallback? onTap;

  static final buttonBorder =
      Border.all(width: 2.0, color: PrimaryColor.semiLight);
  static final containedColor = PrimaryColor.main;

  @override
  Widget build(BuildContext context) {
    return InkWell(
      child: Container(
        padding: buttonPadding,
        height: buttonHeight,
        alignment: Alignment.center,
        decoration: BoxDecoration(
          color: type == ButtonType.Contained ? containedColor : null,
          borderRadius: BorderRadius.all(isRound ? roundBorder : normalBorder),
          border: type == ButtonType.Outlined ? buttonBorder : null,
          boxShadow: [if (type == ButtonType.Contained) buttonShadow],
        ),
        child: Wrap(
          alignment: WrapAlignment.center,
          crossAxisAlignment: WrapCrossAlignment.center,
          children: [
            if (icon != null)
              Padding(
                padding: const EdgeInsets.only(left: normalSpacing),
                child: Icon(
                  icon,
                  color: type == ButtonType.Contained
                      ? GrayColor.white
                      : containedColor,
                ),
              ),
            Text(
              text ?? '',
              style: BTypography.bodyText1.copyWith(
                color: type == ButtonType.Contained
                    ? GrayColor.white
                    : containedColor,
              ),
            ),
          ],
        ),
      ),
      onTap: onTap,
    );
  }
}
