import 'package:bilche/models/enums.dart';
import 'package:flutter/material.dart';

class BaseProvider extends ChangeNotifier {
  ViewState _state = ViewState.Idle;

  ViewState get state => _state;

  setState(ViewState newState) {
    _state = newState;
    notifyListeners();
  }
}
