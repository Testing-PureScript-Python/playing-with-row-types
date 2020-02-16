
// | This module is to show the type checker,
//   and cannot run without giving proproriate implementations in Example.py
"use strict";
var $foreign = require("./foreign.js");
var opt2 = $foreign.mkPyNone;
var test3 = $foreign.linq.map($foreign.f)(opt2);
var opt1 = $foreign.mkPyOption(1);
var test2 = $foreign.linq.map($foreign.f)(opt1);
var list1 = $foreign.mkPyList([ 1, 2 ]);
var test1 = $foreign.linq.map($foreign.f)(list1);
module.exports = {
    list1: list1,
    opt1: opt1,
    opt2: opt2,
    test1: test1,
    test2: test2,
    test3: test3,
    mkPyList: $foreign.mkPyList,
    mkPyOption: $foreign.mkPyOption,
    mkPyNone: $foreign.mkPyNone,
    f: $foreign.f,
    linq: $foreign.linq
};
