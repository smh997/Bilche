import 'package:bilche/utilities/app_constants.dart';
import 'package:bilche/utilities/themes/colors.dart';
import 'package:flutter/material.dart';

class BCard extends Container {
  BCard({
    Key? key,
    this.child,
    this.height,
    this.width,
    this.alignment,
    BoxConstraints? constraints,
  })  : constraints = (width != null || height != null)
            ? constraints?.tighten(width: width, height: height) ??
                BoxConstraints.tightFor(width: width, height: height)
            : constraints,
        super(key: key);

  final Widget? child;
  final double? height;
  final double? width;
  final BoxConstraints? constraints;
  final AlignmentGeometry? alignment;
  final EdgeInsetsGeometry? padding = regularPadding;
  final BoxDecoration? decoration = BoxDecoration(
    color: GrayColor.white,
    boxShadow: [cardShadow],
    borderRadius: BorderRadius.all(normalBorder),
  );
}
