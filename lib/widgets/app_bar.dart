import 'package:bilche/utilities/app_constants.dart';
import 'package:bilche/utilities/themes/colors.dart';
import 'package:bilche/utilities/themes/text_styles.dart';
import 'package:flutter/material.dart';

class BAppBar extends AppBar {
  BAppBar({required this.title, this.centerTitle, List<Widget>? actions})
      : super(actions: [
          Padding(
              padding: regularPadding,
              child: Wrap(
                  direction: Axis.horizontal,
                  spacing: normalSpacing,
                  children: actions ?? []))
        ]);
  final Widget? title;
  final bool? centerTitle;

  @override
  Color? get backgroundColor => Colors.transparent;
  TextStyle? get toolbarTextStyle => titleTextStyle;
  TextStyle? get titleTextStyle => BTypography.headline3;
  TextTheme? get textTheme => BTypography.textTheme;
  double? get toolbarHeight => appBarHeight;
  Color? get shadowColor => Colors.transparent;
  double? get titleSpacing => normalSpacing;
  double? get leadingWidth => d48;
  IconThemeData? get actionsIconTheme => iconTheme;
  Widget? get leading => super.leading;
  IconThemeData? get iconTheme =>
      IconThemeData(size: d24, color: GrayColor.g10);

  @override
  StatefulElement createElement() {
    return super.createElement();
  }
}
