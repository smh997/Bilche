import 'package:bilche/utilities/app_constants.dart';
import 'package:bilche/utilities/themes/text_styles.dart';
import 'package:bilche/widgets/push_button.dart';
import 'package:bilche/widgets/textfield.dart';
import 'package:flutter/material.dart';

class SignInPage extends StatelessWidget {
  const SignInPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    String? input1;
    String? input2;
    print('input1 is $input1');
    print('input2 is $input2');
    return MediaQuery(
      data: MediaQueryData(textScaleFactor: 1.0),
      child: Directionality(
        textDirection: TextDirection.rtl,
        child: Scaffold(
          body: Center(
            child: Padding(
              padding: scaffoldPadding,
              child: Column(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  SizedBox(),
                  Wrap(
                    alignment: WrapAlignment.center,
                    runSpacing: d36,
                    children: [
                      Image.asset('assets/bilche_logo/Logo.png'),
                      Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text('ورود', style: BTypography.subtitle1),
                          SizedBox(height: d24),
                          Text('شماره موبایل خود را وارد کنید.',
                              style: BTypography.bodyText2),
                          SizedBox(height: d16),
                          BTextField(
                            hintText: 'لورم ایپسوم متن آزمایشی است!',
                            label: 'نام کاربری',
                            onChanged: (value) => input1 = value,
                          ),
                        ],
                      ),
                      BPushButton(text: 'ورود به بیلچه', isPrimaryButton: true),
                    ],
                  ),
                  Wrap(
                    direction: Axis.vertical,
                    crossAxisAlignment: WrapCrossAlignment.start,
                    runSpacing: normalSpacing,
                    children: [
                      BPushButton(
                        text: 'ورود با رمز عبور',
                        type: ButtonType.TextOnly,
                      ),
                      BPushButton(
                        text: 'حساب کاربری ندارید؟ ثبت‌نام',
                        type: ButtonType.TextOnly,
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
