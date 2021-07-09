import 'package:bilche/utilities/app_constants.dart';
import 'package:bilche/utilities/themes/text_styles.dart';
import 'package:bilche/widgets/card.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class PlantCard extends BCard {
  final String title;
  final ImageProvider image;
  final double imageSize;
  final VoidCallback? onTap;

  final AlignmentGeometry? alignment = Alignment.center;
  final EdgeInsetsGeometry? padding = mediumPadding;

  PlantCard({
    required this.title,
    required this.image,
    this.imageSize = bigCardImageHeight,
    this.onTap,
  }) : super(
          child: InkWell(
            child: Column(
              children: [
                //Image
                Container(
                  width: imageSize,
                  height: imageSize,
                  decoration: BoxDecoration(
                    image: DecorationImage(image: image),
                    borderRadius: BorderRadius.all(
                        Radius.circular(imageSize / bigCardImageHeight * d8)),
                  ),
                ),
                SizedBox(height: normalSpacing),
                //Title
                Text(
                  title,
                  style: BTypography.bodyText2,
                ),
              ],
            ),
            //On Tap
            onTap: onTap,
          ),
        );
}
