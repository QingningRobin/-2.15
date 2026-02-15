require("D:/PY1/课/测2电子卖场副");


n = window.load;

var i = n("9816")
, o = "77,73,71,102,77,65,48,71,67,83,113,71,83,73,98,51,68,81,69,66,65,81,85,65,65,52,71,78,65,68,67,66,105,81,75,66,103,81,67,83,50,84,90,68,115,53,43,111,114,76,89,67,76,53,83,115,74,53,52,43,98,80,67,86,115,49,90,81,81,119,80,50,82,111,80,107,70,81,70,50,106,99,84,48,72,110,78,78,84,56,90,111,81,103,74,84,114,71,119,78,105,53,81,78,84,66,68,111,72,67,52,111,74,101,115,65,86,89,101,54,68,111,120,88,83,57,78,108,115,56,87,98,71,69,56,90,78,103,79,67,53,116,86,118,49,87,86,106,121,66,119,55,107,50,120,55,50,67,47,113,106,80,111,121,111,47,107,79,55,84,89,108,54,81,110,117,52,106,113,87,47,73,109,76,111,117,112,47,110,115,74,112,112,85,122,110,70,48,89,103,98,121,85,47,100,70,70,78,66,81,73,68,65,81,65,66";


function p_() {
    for (var e = "", t = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "").split(","), n = 0; n < t.length; n++)
        e += String.fromCharCode(Number(t[n]));
    return e
}

function ch(e) {
    var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : p_(o)
        , n = new i.a;
    return n.setPublicKey(t),
    n.encrypt(e)
}

function a() {
    var e = ["y29Uy2f0", "nZG4mJq2wLzJA1Pw", "mtHxEuLwyLK", "B3bXCNn0Dxz3Ea", "mdy4mtzHyMeZzq", "mZK5mte2mfLMu2vfDG", "ExOWmtiZndu2nW", "zwzNAgLQA2XTBG", "nZa3mJK3ng16rKHbua", "zNjVBunOyxjdBW", "nMm5y2qWzdG5za", "mte2ndqZmJv0rwDNEvy", "BgvUz3rO", "ytK5otnLmZy0nW", "odKRlW", "s0XntK9quvjtva", "qujdrevg", "ywjJzgvM", "mdeYmZq1nJC4oq", "qujdrevgr0HjsG", "mJq3nJGWnuzbAwDxsG", "mteYntK4mZjiuMXRzxq", "ywjJ", "mJu3mtC4ntbJmG", "mujTBgjmCW", "y2HHCKnVzgvbDa", "ngrmBurxsa", "y2HHCKf0", "vvzxwfLAywjJza", "mJC1mtaWm3PctNjxBG"];
    return (a = function() {
        return e
    }
    )()
}

function f(e, t) {
    var n = a();
    return f = function(t, i) {
        var r = n[t -= 154];
        void 0 === f.NsReJA && (f.WJgeSN = function(e) {
            for (var t, n, i = "", r = "", o = 0, a = 0; n = e.charAt(a++); ~n && (t = o % 4 ? 64 * t + n : n,
            o++ % 4) ? i += String.fromCharCode(255 & t >> (-2 * o & 6)) : 0)
                n = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=".indexOf(n);
            for (var s = 0, l = i.length; s < l; s++)
                r += "%" + ("00" + i.charCodeAt(s).toString(16)).slice(-2);
            return decodeURIComponent(r)
        }
        ,
        e = arguments,
        f.NsReJA = !0);
        var o = t + n[0]
            , a = e[o];
        return a ? r = a : (r = f.WJgeSN(r),
        e[o] = r),
        r
    }
    ,
    f(e, t)
}

function h(e) {
    for (var t = f, n = i ? t(173) + t(171) : t(173) + t(172), r = "", o = 0; o < 4 * e[t(167)]; o++)
        r += n[t(182)](e[o >> 2] >> 8 * (3 - o % 4) + 4 & 15) + n[t(182)](e[o >> 2] >> 8 * (3 - o % 4) & 15);
    return r
}

function s(e, t) {
    var n = f;
    e[t >> 5] |= 128 << 24 - t % 32,
    e[15 + (t + 64 >> 9 << 4)] = t;
    for (var i, r = Array(80), o = 1732584193, a = -271733879, s = -1732584194, d = 271733878, h = -1009589776, p = 0; p < e[n(167)]; p += 16) {
        for (var m = o, v = a, g = s, y = d, b = h, _ = 0; _ < 80; _++) {
            r[_] = _ < 16 ? e[p + _] : u(r[_ - 3] ^ r[_ - 8] ^ r[_ - 14] ^ r[_ - 16], 1);
            var w = c(c(u(o, 5), l(_, a, s, d)), c(c(h, r[_]), (i = _) < 20 ? 1518500249 : i < 40 ? 1859775393 : i < 60 ? -1894007588 : -899497514));
            h = d,
            d = s,
            s = u(a, 30),
            a = o,
            o = w
        }
        o = c(o, m),
        a = c(a, v),
        s = c(s, g),
        d = c(d, y),
        h = c(h, b)
    }
    return Array(o, a, s, d, h)
}
var r = 8;
function d(e) {
    for (var t = f, n = Array(), i = (1 << r) - 1, o = 0; o < e[t(167)] * r; o += r)
        n[o >> 5] |= (e[t(180)](o / r) & i) << 24 - o % 32;
    return n
}



function o_(e) {
    var t = f;
    return h(s(d(e), e[t(167)] * r))
}

var p = o_
    , m = n("6821")
    , v = n.n(m)
    , g = n("f1dd")
    , y = n.n(g);
const b = b_;

const x = e => v()(y.a[b(166)](e));

function configTokenSign(e, t) {
    const n = b_
        , i = (new Date)[n(165)]()
        , r = x(p(i + "_" + String(e)[n(180)]("?")[0] + (n(171) + n(181) + n(182))))
        , o = {};
    if (o[n(161)] = i,
    o[n(177)] = String(e)[n(180)]("?")[0],
    o[n(173)] = r,
    null != t && "" !== t) {
        const r = x(p("" + t + String(e)[n(180)]("?")[0] + i));
        o[n(174)] = r
    }
    return o
}

function _() {
    const e = ["CgXHDgzVCM1Fma", "otuYodu", "DgLTzq", "mJaYndHWtLPUswC", "ntqWmJi4yNnywgD0", "mJeXmde0r3LduKnK", "z2v0vgLTzq", "zgvJB2rL", "nti5otCXvwDWwhLn", "mtvUt1vKt3a", "mZqZnZvLy2DhA0G", "mty2oeXWBerwsG", "x2jVC3nZB2z0xW", "mti2D3rrCLPl", "C2LNBG", "Dg9Rzw5ZAwDU", "mZCYuNn5yxLN", "mJuYmdLSt2n4rvu", "DxjS", "otbUwKfnCvm", "nJjgEKXtvKi", "C3bSAxq"];
    return (_ = function() {
        return e
    }
    )()
}

!function(e, t) {
    const n = b_
        , i = e();
    for (; ; )
        try {
            if (121507 === -parseInt(n(179)) / 1 * (parseInt(n(170)) / 2) + parseInt(n(167)) / 3 + -parseInt(n(163)) / 4 + parseInt(n(168)) / 5 * (parseInt(n(164)) / 6) + -parseInt(n(172)) / 7 * (parseInt(n(162)) / 8) + parseInt(n(176)) / 9 * (-parseInt(n(178)) / 10) + parseInt(n(169)) / 11 * (parseInt(n(175)) / 12))
                break;
            i.push(i.shift())
        } catch (e) {
            i.push(i.shift())
        }
}(_);

function b_(e, t) {
    const n = _();
    return w = function(t, i) {
        let r = n[t -= 161];
        void 0 === w.hEWvPs && (w.LvEbrJ = function(e) {
            let t = ""
                , n = "";
            for (let i, r, o = 0, a = 0; r = e.charAt(a++); ~r && (i = o % 4 ? 64 * i + r : r,
            o++ % 4) ? t += String.fromCharCode(255 & i >> (-2 * o & 6)) : 0)
                r = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=".indexOf(r);
            for (let i = 0, r = t.length; i < r; i++)
                n += "%" + ("00" + t.charCodeAt(i).toString(16)).slice(-2);
            return decodeURIComponent(n)
        }
        ,
        e = arguments,
        w.hEWvPs = !0);
        const o = t + n[0]
            , a = e[o];
        return a ? r = a : (r = w.LvEbrJ(r),
        e[o] = r),
        r
    }
    ,
    w(e, t)
}


function ans(){
    var Headers = {}
    var b = (new Date).getTime();
    var w = Object(ch)("".concat("/gateway/gpmall-bpoc/notice/v1/ignore/getNoticeList", "$$").concat(b)) || "";
    Headers["nsssjss"] = w;
    Headers["timestamp"] = b.toString();

    sign = configTokenSign("/gateway/gpmall-bpoc/notice/v1/ignore/getNoticeList" || "", undefined || "")

    var combined = { ...Headers, ...sign };
    return combined;
}


console.log(ans());


