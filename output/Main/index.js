"use strict";
var $foreign = require("./foreign.js");
var getFoo = function (v) {
    return v.foo;
};
var main = $foreign.discard($foreign.println(getFoo({
    foo: 1,
    bar: "2"
})))(function () {
    return $foreign.discard($foreign.println(getFoo({
        foo: "3",
        bar: 4
    })))(function () {
        return $foreign.discard($foreign.println(getFoo({
            foo: {}
        })))(function () {
            return $foreign.println(getFoo({
                foo: {
                    foo_nested: 5,
                    bar_nested: 6
                },
                bar: 7
            }));
        });
    });
});
module.exports = {
    getFoo: getFoo,
    main: main,
    println: $foreign.println,
    discard: $foreign.discard
};
