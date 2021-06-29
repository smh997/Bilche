import 'package:flutter/material.dart';

import 'colors.dart';

class BTypography {
  static TextStyle _base = TextStyle(
    fontFamily: 'IRANSansMobile(FaNum)',
    fontSize: 14.0,
    // height: 24.0,
    fontWeight: FontWeight.normal,
    fontStyle: FontStyle.normal,
    color: GrayColor.g10,
  );

  static TextTheme textTheme = TextTheme(
    headline1: headline1,
    headline2: headline2,
    headline3: headline3,
    subtitle1: subtitle1,
    bodyText1: bodyText1,
    bodyText2: bodyText2,
    button: bodyText2,
    subtitle2: bodyText2,
    caption: caption,
    overline: overline,
  );

  static TextStyle headline1 = _base.copyWith(
      fontSize: 24.0, /*height: 41.0,*/ fontWeight: FontWeight.normal);
  static TextStyle headline2 = _base.copyWith(
      fontSize: 21.0, /*height: 36.0,*/ fontWeight: FontWeight.w500);
  static TextStyle headline3 = _base.copyWith(
      fontSize: 19.0, /*height: 32.0,*/ fontWeight: FontWeight.w500);
  static TextStyle subtitle1 = _base.copyWith(
      fontSize: 16.0, /*height: 27.0,*/ fontWeight: FontWeight.w500);
  static TextStyle bodyText1 = _base.copyWith(
      fontSize: 14.0, /*height: 24.0,*/ fontWeight: FontWeight.w500);
  static TextStyle bodyText2 = _base.copyWith(
      fontSize: 14.0, /*height: 24.0,*/ fontWeight: FontWeight.normal);
  static TextStyle caption = _base.copyWith(
      fontSize: 12.0, /*height: 20.0,*/ fontWeight: FontWeight.normal);
  static TextStyle overline = _base.copyWith(
      fontSize: 11.0, /*height: 19.0,*/ fontWeight: FontWeight.w300);
}
