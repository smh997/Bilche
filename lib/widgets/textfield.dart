import 'package:bilche/utilities/app_constants.dart';
import 'package:bilche/utilities/themes/colors.dart';
import 'package:bilche/utilities/themes/text_styles.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class BTextField extends StatelessWidget {
  const BTextField(
      {Key? key,
      this.label,
      this.hintText,
      this.errorText,
      this.controller,
      this.textInputAction = TextInputAction.done,
      this.filled = false,
      this.isPassword = false,
      this.enabled = true,
      this.suffix,
      this.prefix,
      this.helperText,
      this.counterText,
      this.validator,
      required this.onChanged,
      this.onTap,
      this.minLines,
      this.maxLines})
      : super(key: key);

  final String? label;
  final String? hintText;
  final String? suffix;
  final String? prefix;
  final String? errorText;
  final String? helperText;
  final String? counterText;
  final bool enabled;
  final bool filled;
  final bool isPassword;
  final String? Function(String?)? validator;
  final Function(String value) onChanged;
  final VoidCallback? onTap;
  final TextEditingController? controller;
  final TextInputAction textInputAction;
  final int? minLines;
  final int? maxLines;

  static final border =
      OutlineInputBorder(borderRadius: BorderRadius.all(Radius.circular(d8)));
  InputDecoration? get decoration => InputDecoration(
        hintText: hintText,
        labelText: label,
        // labelStyle: BTypography.bodyText2,
        suffixText: suffix,
        prefixText: prefix,
        counterStyle: BTypography.overline,
        border: border.copyWith(
            borderSide: BorderSide(color: PrimaryColor.main, width: 1)),
        contentPadding: inputPadding,
        hintTextDirection: textDirection,
        hintStyle: BTypography.bodyText2.copyWith(color: GrayColor.g70),
        fillColor: GrayColor.white,
        filled: true,
        errorText: errorText,
      );
  TextDirection? get textDirection => TextDirection.rtl;

  @override
  Widget build(BuildContext context) {
    return Directionality(
      textDirection: TextDirection.rtl,
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Container(
            child: TextFormField(
              style: BTypography.bodyText2,
              obscureText: isPassword,
              textInputAction: textInputAction,
              decoration: decoration,
              textDirection: textDirection,
              onTap: onTap,
              onChanged: onChanged,
              controller: controller,
              minLines: minLines,
              maxLines: maxLines,
              enabled: enabled,
              validator: validator,
            ),
            decoration: BoxDecoration(boxShadow: [inputShadow]),
          ),
          SizedBox(height: d4),
          if (helperText != null || counterText != null)
            Padding(
              padding: const EdgeInsets.all(d4),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Text(helperText ?? '', style: BTypography.overline),
                  SizedBox(width: normalSpacing),
                  Text(counterText ?? '',
                      style:
                          BTypography.overline.copyWith(color: GrayColor.g10)),
                ],
              ),
            ),
        ],
      ),
    );
  }
}
