import 'package:bilche/utilities/app_constants.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class BTable extends StatelessWidget {
  const BTable({
    Key? key,
    required this.crossAxisCount,
    required this.children,
  }) : super(key: key);
  final int crossAxisCount;
  final List<Widget> children;

  @override
  Widget build(BuildContext context) {
    return GridView.count(
      shrinkWrap: true,
      padding: EdgeInsets.only(bottom: d16),
      crossAxisCount: crossAxisCount,
      childAspectRatio: 1,
      mainAxisSpacing: normalSpacing,
      crossAxisSpacing: normalSpacing,
      children: children,
    );
  }
}
