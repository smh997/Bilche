import 'package:bilche/utilities/app_constants.dart';
import 'package:bilche/utilities/themes/text_styles.dart';
import 'package:bilche/widgets/card.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class SiteCard extends BCard {
  final String title;
  final String lightFactor;
  final String tempFactor;
  final String humidityFactor;
  final String placeType;
  // final List pics;

  final AlignmentGeometry? alignment = Alignment.center;
  final EdgeInsetsGeometry? padding = mediumPadding;

  SiteCard({
    required this.title,
    required this.lightFactor,
    required this.tempFactor,
    required this.humidityFactor,
    required this.placeType,
  }) : super(
            height: 100,
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    //Title
                    Text(
                      title,
                      style: BTypography.bodyText2,
                    ),
                    SizedBox(height: normalSpacing),
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          children: [
                            //Light
                            Row(
                              children: [
                                Icon(CupertinoIcons.bubble_left),
                                SizedBox(width: captionSpacing),
                                Text(
                                  lightFactor,
                                  style: BTypography.overline,
                                ),
                              ],
                            ),
                            SizedBox(width: mediumSpacing),
                            //Temperature
                            Row(
                              children: [
                                Icon(CupertinoIcons.bubble_left),
                                SizedBox(width: captionSpacing),
                                Text(
                                  tempFactor,
                                  style: BTypography.overline,
                                ),
                              ],
                            ),
                            SizedBox(width: mediumSpacing),
                            //Humidity
                            Row(
                              children: [
                                Icon(CupertinoIcons.bubble_left),
                                SizedBox(width: captionSpacing),
                                Text(
                                  humidityFactor,
                                  style: BTypography.overline,
                                ),
                              ],
                            ),
                          ],
                        ),
                        SizedBox(height: captionSpacing),
                        //Place Type
                        Row(
                          children: [
                            Text(
                              'نوع محل:',
                              style: BTypography.overline,
                            ),
                            SizedBox(width: captionSpacing),
                            Text(
                              placeType,
                              style: BTypography.overline,
                            ),
                          ],
                        ),
                      ],
                    ),
                  ],
                ),
                Text('Pictures')
              ],
            ));
}
