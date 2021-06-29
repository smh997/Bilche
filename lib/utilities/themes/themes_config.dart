import 'package:bilche/utilities/themes/text_styles.dart';
import 'package:flutter/material.dart';

import 'colors.dart';

class BTheme {
  static ThemeData light = ThemeData(
    scaffoldBackgroundColor: backgroundColor,
    primaryTextTheme: BTypography.textTheme,
    primaryColor: PrimaryColor.main,
    accentColor: SecondaryColor.main,
    shadowColor: ShadowColor.card,
    textTheme: BTypography.textTheme,
  );

  static ThemeData dark = light;
}
