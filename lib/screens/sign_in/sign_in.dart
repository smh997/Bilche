import 'package:bilche/providers/sign_in_provider.dart';
import 'package:bilche/screens/assistant_page/assistant_page.dart';
import 'package:bilche/screens/sign_in/sign_in_pass.dart';
import 'package:bilche/utilities/app_constants.dart';
import 'package:bilche/utilities/themes/text_styles.dart';
import 'package:bilche/widgets/push_button.dart';
import 'package:bilche/widgets/textfield.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

class SignInPage extends StatelessWidget {
  const SignInPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Consumer<SignInProvider>(
      builder: (context, model, child) => MediaQuery(
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
                    Padding(
                      padding: const EdgeInsets.only(top: normalSpacing),
                      child: Row(
                          mainAxisAlignment: MainAxisAlignment.end,
                          children: [
                            BPushButton(
                              text: 'بعداً',
                              type: ButtonType.TextOnly,
                              onTap: () => Navigator.of(context)
                                  .pushReplacement(MaterialPageRoute(
                                      builder: (context) => AssistantPage())),
                            ),
                          ]),
                    ),
                    Wrap(
                      alignment: WrapAlignment.center,
                      runSpacing: d36,
                      children: [
                        Image.asset('assets/bilche_logo/Logo.png'),
                        Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text('ورود', style: BTypography.subtitle1),
                            SizedBox(height: hugeSpacing),
                            Text('شماره موبایل خود را وارد کنید.',
                                style: BTypography.bodyText2),
                            SizedBox(height: extraSpacing),
                            BTextField(
                              hintText: 'مثلاً 09123456789',
                              textInputType: TextInputType.phone,
                              maxLength: 11,
                              counterText:
                                  (model.phone ?? '').length.toString() + '/11',
                              validator: (value) {},
                              // label: 'نام کاربری',
                              onChanged: (value) => model.setPhone(value),
                            ),
                          ],
                        ),
                        BPushButton(
                          text: 'ورود به بیلچه',
                          isPrimaryButton: true,
                          onTap: () {},
                        ),
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
                          onTap: () => Navigator.of(context).pushReplacement(
                              MaterialPageRoute(
                                  builder: (context) => SignInPasswordPage())),
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
      ),
    );
  }
}
