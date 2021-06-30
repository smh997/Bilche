import 'package:bilche/utilities/themes/text_styles.dart';
import 'package:flutter/material.dart';

import 'colors.dart';

class BTheme {
  static ThemeData light = ThemeData(
    scaffoldBackgroundColor: backgroundColor,
    primaryColor: PrimaryColor.main,
    accentColor: SecondaryColor.main,
    shadowColor: ShadowColor.card,
    dividerColor: GrayColor.g50,
    hoverColor: GrayColor.g70,
    textTheme: BTypography.textTheme,
    primaryTextTheme: BTypography.textTheme,
  );

  static ThemeData dark = light;
}
