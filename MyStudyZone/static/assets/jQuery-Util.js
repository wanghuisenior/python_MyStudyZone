/**
 * 名称：jQuery 工具箱
 * 创建日期：2018-01-20
 * 更新日期：2018-07-10
 * 开发者：helang.love@qq.com
 * 联系QQ:1846492969
 */

$.extend({
    Util: {
        /* 获取浏览器类型 */
        getBrowser: function () {
            if (!!document.all) {
                return 'IE'
            } else if (!!document.all && !window.XMLHttpRequest) {
                return 'IE6'
            } else if (!!document.all && /msie 7.0/gi.test(window.navigator.appVersion)) {
                return 'IE7'
            } else if (!!document.all && /msie 8.0/gi.test(window.navigator.appVersion)) {
                return 'IE8'
            } else if (/firefox/gi.test(window.navigator.userAgent)) {
                return 'Firefox'
            } else if (/opera/gi.test(window.navigator.userAgent)) {
                return 'Opera'
            } else if (/Chrom/gi.test(window.navigator.userAgent)) {
                return 'Chrome'
            }
        },
        /* 获取终端类型 */
        getTerminal: function () {
            var regs = {
                /* 安卓 */
                "android": /android/i,
                /* 苹果平板电脑 */
                "iPad": /ipad/i,
                /* 苹果手机 */
                "iphone": /iphone/i,
                /* 苹果操作系统 */
                "mac": /macintosh/i,
                /* 微软操作系统 */
                "windows": /windows/i,
                /* 移动端设备 */
                "mobileEnd": /(nokia|iphone|android|ipad|motorola|^mot\-|softbank|foma|docomo|kddi|up\.browser|up\.link|htc|dopod|blazer|netfront|helio|hosin|huawei|novarra|CoolPad|webos|techfaith|palmsource|blackberry|alcatel|amoi|ktouch|nexian|samsung|^sam\-|s[cg]h|^lge|ericsson|philips|sagem|wellcom|bunjalloo|maui|symbian|smartphone|midp|wap|phone|windows ce|iemobile|^spice|^bird|^zte\-|longcos|pantech|gionee|^sie\-|portalmmm|jig\s browser|hiptop|^ucweb|^benq|haier|^lct|opera\s*mobi|opera\*mini|320x320|240x320|176x220)/i
            };
            for (var k in regs) {
                if (regs[k].test(window.navigator.userAgent)) {
                    return k
                }
            }
            return '未知设备';
        },
        /*获取随机数*/
        getRandomNumber: function (min, max) {
            return Math.floor(Math.random() * (max - min)) + min + 1;
        },
        /*字符串截取*/
        substring: function (str, length) {
            if (str.length > length) {
                return str.substring(0, length) + "...";
            } else {
                return str;
            }
        },
        /* 操作cookie*/
        cookie: {
            /* 设置 */
            set: function (key, val, len, unit) {
                if (!key || typeof val == 'undefined') {
                    return false;
                }
                var cookieVal = val;
                if (typeof cookieVal == 'object') {
                    var valArr = [];
                    $.each(cookieVal, function (val_k, val_v) {
                        valArr.push(val_k + "=" + val_v);
                    });
                    cookieVal = valArr.join("&");
                }
                var len = len || 1;
                var unit = unit || "d";
                var units = {
                    "d": len * 24 * 60 * 60 * 1000,
                    "h": len * 60 * 60 * 1000,
                    "m": len * 60 * 1000,
                    "s": len * 1000
                };
                var dt = new Date();
                dt.setTime(dt.getTime() + (units[unit]));
                var expires = ";expires=" + dt.toGMTString();
                var path = ';path=/', domain = '', secure = '';
                document.cookie = [key, '=', cookieVal, expires, path, domain, secure].join('');
            },
            /* 获取
            * key:cookie的名称，必传参数
            * name:cookie中的指定值，缺省默认返回cookie下所有值
            * */
            get: function (key, name) {
                var cookieStr = document.cookie;
                var start = cookieStr.indexOf(key + "=");
                if (!key || start < 0) {
                    return false;
                }
                cookieStr = cookieStr.substring(start);
                var end = cookieStr.indexOf(";");
                if (end >= 0) {
                    cookieStr = cookieStr.substring(0, end);
                }
                cookieStr = cookieStr.substring(key.length + 1);
                cookieStr = decodeURIComponent(cookieStr);
                var keyArr = cookieStr.split("&");
                if (keyArr.length < 2) {
                    return keyArr[0];
                }
                var keyJSON = {};
                for (var i = 0; i < keyArr.length; i++) {
                    var item = keyArr[i].split("=");
                    keyJSON[item[0]] = item[1];
                }
                if (!name) {
                    return keyJSON;
                } else {
                    if (keyJSON.hasOwnProperty(name)) {
                        return keyJSON[name];
                    } else {
                        return false;
                    }
                }
            },
            /* 删除 */
            del: function (key) {
                this.set(key, "", -365);
            }
        },
        /* 序列化表单数据为JSON格式 */
        serializeJSON: function (obj) {
            var formArr = obj.serializeArray();
            var formObj = new Object();
            $.each(formArr, function () {
                if (formObj[this.name]) {
                    if (!formObj[this.name].push) {
                        formObj[this.name] = [formObj[this.name]];
                    }
                    formObj[this.name].push(this.value || '');
                } else {
                    formObj[this.name] = this.value || '';
                }
            });
            return formObj;
        },
        /*window对象*/
        win: {
            /*窗口跳转地址，@time:再指定的毫秒数后调用函数*/
            href: function (url, time) {
                var time = time || 0;
                setTimeout(function () {
                    window.location.href = url;
                }, time);
            },
            /*打开新窗口*/
            open: function (url, time) {
                var time = time || 0;
                setTimeout(function () {
                    window.open(url);
                }, time);
            },
            /*回退历史记录*/
            back: function () {
                window.history.back();
            },
            /*刷新当前页面*/
            reload: function (time) {
                var time = time || 0;
                setTimeout(function () {
                    window.location.reload();
                }, time);
            }
        },
        /*校验*/
        verify: function (key, val) {
            var regs = {
                /* 邮箱 */
                "email": /^[0-9a-zA-Z_]+@[0-9a-zA-Z_]+[\.]{1}[0-9a-zA-Z]+[\.]?[0-9a-zA-Z]+$/,
                /* 手机 */
                "mobile": /^(0|86|17951)?(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$/,
                /* 超链接 */
                "url": /^https?:\/\/(([a-zA-Z0-9_-])+(\.)?)*(:\d+)?(\/((\.)?(\?)?=?&?[a-zA-Z0-9_-](\?)?)*)*$/i,
                /* 身份证 */
                "idCard": /^(^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$)|(^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])((\d{4})|\d{3}[Xx])$)$/,
                /* 邮政编码 */
                "postal": /^[1-9]\d{5}(?!\d)$/,
                /* YY-MM-dd 格式日期 */
                "date": /^[1-2][0-9][0-9][0-9]-[0-1]{0,1}[0-9]-[0-3]{0,1}[0-9]$/,
                /* QQ */
                "qq": /^[1-9][0-9]{4,9}$/,
                /* 全部为数字 */
                "numAll": /"^\d+$/,
                /* 适合的帐号 英文/数字 */
                "legalUserName": /^[a-z0-9A-Z]+$/i,
                /* 适合的密码 英文/数字/下划线 */
                "legalPassword": /^[0-9a-zA-Z_]+$/,
                /* 是否包含中文 */
                "isContainChinese": /[\u4e00-\u9fa5]/
            };
            return regs[key].test(val);
        },
        /**
         *
         * 必须引入bootstrap3 css及js
         *说明：基于bootstrap对模态框进行封装；
         *界面构造(必须给予modal控件ID),将以下div放在html页面任意位置(默认隐藏不占空间)
         <div id="bs_modal_alert" class="modal" style="z-index:9999;display: none;">
         <div class="modal-dialog modal-sm">
         <div class="modal-content">
         <div class="modal-header">
         <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span>
         </button>
         <h5 class="modal-title"><i class="fa fa-exclamation-circle"></i> [Title]</h5>
         </div>
         <div class="modal-body small">
         <p>[Message]</p>
         </div>
         <div class="modal-footer">
         <button type="button" class="btn btn-primary ok" data-dismiss="modal">[BtnOk]</button>
         <button type="button" class="btn btn-default cancel" data-dismiss="modal">[BtnCancel]</button>
         </div>
         </div>
         </div>
         </div>
         *显示提示消息（自动关闭）
         * @param msg
         * @param msec 显示时间（毫秒）,可选参数
         * @param callback 回调函数,可选参数
         $.Util.bootstrapTip('成功!', 5000, function () {
            console.log('提示框消失了自动')
         })
         **/
        bootstrapTip: function (msg, msec, callback) {
            if (!msec) {
                msec = 500;
            }
            Modal.tip({
                title: '提示',
                msg: msg
            }, msec);
            setTimeout(callback, msec);
        },
        /**
         * 显示提示消息（需点击确定关闭）
         * @param msg
         * @param callback 回调函数,可选参数
         * 调用：
         $.Util.bootstrapMsg('成功！', function () {
            console.log('点击确定按钮后执行')
         })
         */
        bootstrapMsg: function (msg, callback) {
            Modal.alert({
                title: '提示',
                msg: msg,
                btnok: '确定'
            }).on(function (e) {
                if (callback) {
                    callback();
                }
            });
        },
        /**
         * Confirm提示（点击确定按钮才会执行，否则不执行）
         * @param msg
         * @param callback 回调函数,必须定义
         * 调用：
         $.Util.bootstrapConfirm('确认执行该操作吗？', function () {
            console.log('我只有在点击了确认按钮后才会输出，点击取消按钮不输出')
         })
         */
        bootstrapConfirm: function (msg, callback) {
            Modal.confirm({
                title: '提示',
                msg: msg,
            }).on(function (e) {
                callback();
            });
        }

    }
});
/***
 * 模态框封装
 */
$(function () {
    window.Modal = function () {
        var reg = new RegExp("\\[([^\\[\\]]*?)\\]", 'igm');
        var alr = $("#bs_modal_alert"); //这里的id必须和页面上模态框id一致
        var ahtml = alr.html();

        var _tip = function (options, msec) {
            alr.html(ahtml);    // 复原
            alr.find('.ok').hide();
            alr.find('.cancel').hide();
            alr.find('.modal-content').width(200);
            _dialog(options, msec);

            return {
                on: function (callback) {
                }
            };
        };

        var _alert = function (options) {
            alr.html(ahtml);  // 复原
            alr.find('.ok').removeClass('btn-success').addClass('btn-primary');
            alr.find('.cancel').hide();
            _dialog(options);

            return {
                on: function (callback) {
                    if (callback && callback instanceof Function) {
                        alr.find('.ok').click(function () {
                            callback(true)
                        });
                    }
                }
            };
        };

        var _confirm = function (options) {
            alr.html(ahtml); // 复原
            alr.find('.ok').removeClass('btn-primary').addClass('btn-success');
            alr.find('.cancel').show();
            _dialog(options);

            return {
                on: function (callback) {
                    if (callback && callback instanceof Function) {
                        alr.find('.ok').click(function () {
                            callback(true)
                        });
                        alr.find('.cancel').click(function () {
                            return;
                        });
                    }
                }
            };
        };

        var _dialog = function (options, msec) {
            var ops = {
                msg: "提示内容",
                title: "操作提示",
                btnok: "确定",
                btncl: "取消"
            };

            $.extend(ops, options);

            var html = alr.html().replace(reg, function (node, key) {
                return {
                    Title: ops.title,
                    Message: ops.msg,
                    BtnOk: ops.btnok,
                    BtnCancel: ops.btncl
                }[key];
            });

            alr.html(html);
            alr.modal({
                width: 250,
                backdrop: 'static'
            });
            if (msec) {
                setTimeout(function () {
                    alr.modal('hide')
                }, msec)
            }
        }

        return {
            tip: _tip,
            alert: _alert,
            confirm: _confirm
        }

    }();
});


