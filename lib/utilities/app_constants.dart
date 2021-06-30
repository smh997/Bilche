import 'package:bilche/utilities/themes/colors.dart';
import 'package:flutter/cupertino.dart';

//Borders
const normalBorder = const Radius.circular(8.0);
const roundBorder = const Radius.circular(1000);

//Spacing
const captionSpacing = 4.0;
const normalSpacing = 8.0;
const mediumSpacing = 12.0;
const extraSpacing = 16.0;

//Paddings
const scaffoldPadding = const EdgeInsets.all(16.0);
const cardPadding = const EdgeInsets.all(20.0);
const regularPadding = const EdgeInsets.all(8.0);
const mediumPadding = const EdgeInsets.all(12.0);
const buttonPadding = regularPadding;

//Heights
const buttonHeight = 48.0;
const appBarHeight = 56.0;

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
