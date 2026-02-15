require("D:/PY1/课/测3点点副");

const crypto = require('crypto');

n = window.load;


var d = n(24)
, c = n.n(d)
, m = n(318)
, _ = n.n(m)
, f = n(2039)
, h = n.n(f);


function yb(e, n, o) {
    var d = "";
    n = Buffer.from(n, "utf8"),
    o = Buffer.from(o, "utf8");
    var c = Object(crypto.createDecipheriv)("aes-128-cbc", n, o);
    return d += c.update(e, "hex", "utf8"),
    d += c.final("utf8")
}


function v(e, path, n, r) {
    var s = n.s
        , d = n.k
        , m = n.l
        , f = n.d
        , v = n.sort
        , l = n.num
        , k = function(content, t, e) {
        for (var a = Array.from(content), n = Array.from(t), r = a.length, o = n.length, d = String.fromCodePoint, i = 0; i < r; i++)
            a[i] = d(a[i].codePointAt(0) ^ n[(i + e) % o].codePointAt(0));
        return a.join("")
    }(function(s, t, path, e) {
        return [s, t, e, path].join("(&&)")
    }(function(t, e) {
        var n = c()(t);
        if (!h()(n)) {
            var r = [];
            for (var d in n)
                _()(n[d]) && "get" === e && (n[d] = n[d].join("")),
                "post" === e && (_()(n[d]) || o()(n[d])) && (n[d] = JSON.stringify(n[d])),
                r.push(n[d]);
            return r.sort(),
            r.join("")
        }
    }(e, r), parseInt((new Date).getTime() / 1e3) - 655876800 - f, path, v), Object(yb)(s, d, m), l);
    return Buffer.from(k).toString("base64")
}


function data_en(s, k, l, d){
    var r = {
        "market_id": "",
        "sub_type": 1,
        "is_detail": 0,
        "is_go_sea": 0,
        "country_id": ""
    }


    var o = Object(v)(r, "/v2/user/favorite", {
                            s: s,
                            k: k,
                            l: l,
                            d: d,
                            sort: "dd",
                            num: 10
                        }, "get");
    return o;
}


// console.log(data_en("ab68b062bd7456251edd3d1d9d1e9af9", "7696e4674352f94b", "9143f91daff56df2"))
