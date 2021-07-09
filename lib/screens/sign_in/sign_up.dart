import 'package:bilche/providers/sign_in_provider.dart';
import 'package:bilche/providers/sign_up_provider.dart';
import 'package:bilche/screens/assistant_page/assistant_page.dart';
import 'package:bilche/screens/sign_in/sign_in_pass.dart';
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

class SignUpPage extends StatelessWidget {
  SignUpPage({Key? key}) : super(key: key);
  final _formKey1 = GlobalKey<FormState>();
  final _formKey2 = GlobalKey<FormState>();
  final _formKey3 = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Consumer<SignUpProvider>(
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
                              text: 'بعداً ثبت‌نام می‌کنم',
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
                            Text('ثبت‌نام در بیلچه',
                                style: BTypography.subtitle1),
                            SizedBox(height: hugeSpacing),
                            Wrap(
                              runSpacing: normalSpacing,
                              children: [
                                Form(
                                  key: _formKey1,
                                  child: BTextField(
                                    hintText: 'مثلاً علی غفرانی',
                                    label: 'نام و نام خانوادگی',
                                    textInputAction: TextInputAction.next,
                                    textInputType: TextInputType.text,
                                    validator: (value) =>
                                        validateNotnull(value),
                                    onChanged: (value) => model.setName(value),
                                    onFieldSubmitted: (value) =>
                                        _formKey1.currentState!.validate(),
                                  ),
                                ),
                                Form(
                                  key: _formKey2,
                                  child: BTextField(
                                    hintText: 'example@bilche.com',
                                    label: 'ایمیل',
                                    textInputAction: TextInputAction.next,
                                    textInputType: TextInputType.emailAddress,
                                    textDirection: TextDirection.ltr,
                                    validator: (email) => validateEmail(email),
                                    onChanged: (value) => model.setEmail(value),
                                    onFieldSubmitted: (value) =>
                                        _formKey2.currentState!.validate(),
                                  ),
                                ),
                                Form(
                                  key: _formKey3,
                                  child: BTextField(
                                    hintText: '••••••••••••••••',
                                    label: 'رمز عبور',
                                    textInputAction: TextInputAction.done,
                                    textInputType:
                                        TextInputType.visiblePassword,
                                    textDirection: TextDirection.ltr,
                                    isPassword: true,
                                    validator: (pass) => validatePassword(pass),
                                    onChanged: (value) =>
                                        model.setPassword(value),
                                    onFieldSubmitted: (value) =>
                                        _formKey3.currentState!.validate(),
                                  ),
                                ),
                              ],
                            ),
                          ],
                        ),
                        BPushButton(
                          text: 'ثبت‌نام',
                          isPrimaryButton: true,
                          onTap: () async {
                            var isValid =
                                (_formKey1.currentState!.validate()) &&
                                    (_formKey2.currentState!.validate());
                            if (isValid) {
                              var res = await model.register() ?? false;
                              if (res!) {
                                var signInProvider =
                                    Provider.of<SignInProvider>(context,
                                        listen: false);
                                signInProvider.setEmail(model.user!.email);
                                signInProvider
                                    .setPassword(model.user!.password!);
                                var res2 = await signInProvider.login();
                                if (res2) {
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
                                }
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
                          text: 'قبلاً ثبت‌نام کرده‌اید؟ ورود',
                          type: ButtonType.TextOnly,
                          onTap: () => Navigator.of(context).pushReplacement(
                              MaterialPageRoute(
                                  builder: (context) => SignInPasswordPage())),
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
