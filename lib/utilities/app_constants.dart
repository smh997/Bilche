import 'package:bilche/utilities/themes/colors.dart';
import 'package:flutter/cupertino.dart';

//Borders
const normalBorder = const Radius.circular(d8);
const roundBorder = const Radius.circular(1000);

//Spacing
const captionSpacing = d4;
const normalSpacing = d8;
const mediumSpacing = d12;
const extraSpacing = d16;
const hugeSpacing = d20;

//Paddings
const scaffoldPadding = const EdgeInsets.all(d16);
const inputPadding = mediumPadding;
const cardPadding = const EdgeInsets.all(d20);
const regularPadding = const EdgeInsets.all(d8);
const mediumPadding = const EdgeInsets.all(d12);
const buttonPadding = regularPadding;

//Heights
const menuItemHeight = d48;
const buttonHeight = d48;
const appBarHeight = d56;

//Shadows
const cardShadow = const BoxShadow(
  color: ShadowColor.card,
  blurRadius: extraSpacing,
  offset: Offset(2.0, 2.0),
);
const buttonShadow = const BoxShadow(
  color: ShadowColor.button,
  blurRadius: mediumSpacing,
  offset: Offset.zero,
);
const tabItemShadow = const BoxShadow(
  color: ShadowColor.tabItems,
  blurRadius: mediumSpacing,
  offset: Offset.zero,
);
const inputShadow = const BoxShadow(
  color: ShadowColor.input,
  blurRadius: d4,
  offset: Offset(0.0, 2.0),
);

//All Sizes
const double d4 = 4.0;
const double d8 = 8.0;
const double d12 = 12.0;
const double d16 = 16.0;
const double d20 = 20.0;
const double d24 = 24.0;
const double d36 = 36.0;
const double d48 = 48.0;
const double d56 = 56.0;
