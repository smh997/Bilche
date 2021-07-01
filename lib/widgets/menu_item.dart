import 'package:bilche/utilities/app_constants.dart';
import 'package:bilche/utilities/themes/colors.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class MenuItem extends StatelessWidget {
  const MenuItem(
      {Key? key,
      required this.text,
      this.leading,
      this.trailing,
      this.onTap,
      this.hasDivider = true})
      : super(key: key);

  final String text;
  final Widget? leading;
  final Widget? trailing;
  final bool hasDivider;
  final VoidCallback? onTap;

  @override
  Widget build(BuildContext context) {
    return InkWell(
      child: Container(
        constraints: BoxConstraints(minHeight: menuItemHeight),
        alignment: Alignment.center,
        child: Column(
          children: [
            Padding(
              padding: EdgeInsets.symmetric(vertical: normalSpacing),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Row(
                    children: [
                      leading ?? SizedBox(),
                      SizedBox(width: normalSpacing),
                      Text(text),
                    ],
                  ),
                  trailing ?? SizedBox(),
                ],
              ),
            ),
            hasDivider
                ? Divider(
                    thickness: 0.75,
                    color: GrayColor.g85,
                  )
                : SizedBox(),
          ],
        ),
      ),
      onTap: onTap,
    );
  }
}
