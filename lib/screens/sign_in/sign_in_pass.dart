import 'package:bilche/providers/sign_in_provider.dart';
import 'package:bilche/screens/assistant_page/assistant_page.dart';
import 'package:bilche/screens/sign_in/sign_up.dart';
import 'package:bilche/utilities/app_constants.dart';
import 'package:bilche/utilities/themes/colors.dart';
import 'package:bilche/utilities/themes/text_styles.dart';
import 'package:bilche/utilities/validations.dart';
import 'package:bilche/widgets/push_button.dart';
import 'package:bilche/widgets/textfield.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:overlay_support/overlay_support.dart';
import 'package:provider/provider.dart';

class SignInPasswordPage extends StatelessWidget {
  SignInPasswordPage({Key? key}) : super(key: key);
  final _formKey1 = GlobalKey<FormState>();
  final _formKey2 = GlobalKey<FormState>();

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
                              text: 'بعداً وارد می‌شوم',
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
                            Text('ورود به بیلچه', style: BTypography.subtitle1),
                            SizedBox(height: hugeSpacing),
                            Form(
                              key: _formKey1,
                              child: BTextField(
                                hintText: 'example@bilche.com',
                                label: 'ایمیل',
                                textInputAction: TextInputAction.next,
                                textInputType: TextInputType.emailAddress,
                                textDirection: TextDirection.ltr,
                                validator: (email) => validateEmail(email),
                                onChanged: (value) => model.setEmail(value),
                                onFieldSubmitted: (value) =>
                                    _formKey1.currentState!.validate(),
                              ),
                            ),
                            SizedBox(height: normalSpacing),
                            Form(
                              key: _formKey2,
                              child: BTextField(
                                hintText: '••••••••••••••••',
                                label: 'رمز عبور',
                                textInputAction: TextInputAction.done,
                                textInputType: TextInputType.visiblePassword,
                                textDirection: TextDirection.ltr,
                                isPassword: true,
                                validator: (pass) => validatePassword(pass),
                                onChanged: (value) => model.setPassword(value),
                                onFieldSubmitted: (value) =>
                                    _formKey2.currentState!.validate(),
                              ),
                            ),
                          ],
                        ),
                        BPushButton(
                          text: 'ورود به بیلچه',
                          isPrimaryButton: true,
                          onTap: () async {
                            var isValid =
                                (_formKey1.currentState!.validate()) &&
                                    (_formKey2.currentState!.validate());
                            if (isValid) {
                              var res = await model.login() ?? false;
                              if (res!) {
                                Navigator.of(context)
                                    .pushReplacement(MaterialPageRoute(
                                  builder: (context) => AssistantPage(),
                                ));
                                showSimpleNotification(
                                    Directionality(
                                      textDirection: TextDirection.rtl,
                                      child: Text(
                                        'با موفقیت وارد شدید',
                                        style: BTypography.bodyText1
                                            .copyWith(color: GrayColor.white),
                                      ),
                                    ),
                                    background: successColor);
                              } else
                                showSimpleNotification(
                                    Directionality(
                                      textDirection: TextDirection.rtl,
                                      child: Text(
                                        model.errorMessage!,
                                        style: BTypography.bodyText1
                                            .copyWith(color: GrayColor.white),
                                      ),
                                    ),
                                    background: errorColor);
                              // print('Request failed');
                            }
                          },
                        ),
                      ],
                    ),
                    Wrap(
                      direction: Axis.vertical,
                      crossAxisAlignment: WrapCrossAlignment.start,
                      runSpacing: normalSpacing,
                      children: [
                        SizedBox(height: buttonHeight),
                        BPushButton(
                          text: 'حساب کاربری ندارید؟ ثبت‌نام',
                          type: ButtonType.TextOnly,
                          onTap: () => Navigator.of(context).pushReplacement(
                              MaterialPageRoute(
                                  builder: (context) => SignUpPage())),
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
