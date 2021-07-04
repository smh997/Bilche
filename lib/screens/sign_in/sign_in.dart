import 'package:bilche/utilities/app_constants.dart';
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
    return Scaffold(
      body: Center(
        child: Padding(
          padding: scaffoldPadding,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              BTextField(
                hintText: 'لورم ایپسوم متن آزمایشی است!',
                label: 'نام کاربری',
                onChanged: (value) => input1 = value,
              ),
              BTextField(
                onChanged: (value) => input2 = value,
                hintText: 'لورم ایپسوم متن آزمایشی است!',
              ),
            ],
          ),
        ),
      ),
    );
  }
}
