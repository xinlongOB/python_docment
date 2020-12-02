var myEnergeType = ["线下支付", "行走", "共享单车", "地铁购票", "网络购票", "网购火车票", "生活缴费", "ETC缴费", "电子发票", "绿色办公", "咸鱼交易", "预约挂号"];
var morningTime = "07:20";//自己运动能量生成时间

auto.waitFor()
unlock();
sleep(1000);
mainEntrence();

//解锁
function unlock() {
    if (!device.isScreenOn()) {
        //点亮屏幕
        device.wakeUp();
        sleep(500);
        //滑动屏幕到输入密码界面
        swipe(500, 1900, 500, 1000, 1000);
        sleep(500);

        //输入四次 1 （密码为1111） 数字键1的像素坐标为（200,1000）
        click(200, 1000);
        sleep(500);

        click(200, 1000);
        sleep(500);

        click(200, 1000);
        sleep(500);

        click(200, 1000);
        sleep(500);

    }
}

function tLog(msg) {
    toast(msg);
    console.log(msg)
}

/**
 * 获取权限和设置参数
 */
function prepareThings() {
    setScreenMetrics(1080, 2340);
    //请求截图
    if (!requestScreenCapture()) {
        tLog("请求截图失败");
        exit();
    }

}

/**
 * 设置按键监听 当脚本执行时候按音量减 退出脚本
 */
function registEvent() {
    //启用按键监听
    events.observeKey();
    //监听音量上键按下
    events.onKeyDown("volume_down", function (event) {
        tLog("脚本手动退出");
        exit();
    });
}

/**
 * 获取截图
 */
function getCaptureImg() {
    var img0 = null;
    img0 = captureScreen();
    // tLog("获取截图完成");
    if (!img0) {
        tLog("截图失败,退出脚本");
        exit();
    } else {
        return img0;
    }
}

/**
 * 默认程序出错提示操作
 */
function defaultException() {
    tLog("程序当前所处状态不合预期,脚本退出");
    exit();
}

/**
 * 等待加载收集能量页面,采用未找到指定组件阻塞的方式,等待页面加载完成
 */
function waitPage(type) {
    // 等待进入自己的能量主页
    if (type == 0) {
        tLog("等待进入自己的能量主页");
        // desc("消息").findOne();
    }
    // 等待进入他人的能量主页
    else if (type == 1) {
        desc("浇水").findOne();
        tLog("已进入他人的能量主页");
    }
    // tLog("容错处理 等待3毫秒");
    //再次容错处理
    sleep(3000);
}

/**
 * 从支付宝主页进入蚂蚁森林我的主页
 */
function enterMyMainPage() {
    launchApp("支付宝");
    tLog("等待支付宝启动");
    sleep(3000);
    click("蚂蚁森");
    //等待进入自己的主页
    waitPage(0);
}

/**
 * 进入排行榜
 */
function enterRank() {
    tLog("进入排行榜");
    try {
        //滑动到最低端
        swipe(520, 1860, 520, 100, 1000);
        swipe(520, 1860, 520, 100, 1000);
        swipe(520, 1860, 520, 100, 1000);
        clickByDesc("查看更多好友", 0, true, "程序未找到排行榜入口,脚本退出");
        //等待排行榜主页出现
        sleep(5000);
    } catch (e) {
        tLog("error[%j]" + e);
    }
}

/**
 * 从排行榜获取可收集好有的点击位置
 * @returns {*}
 */
function getHasEnergyfriend(type) {
    tLog("从排行榜获取可收集好有的点击位置");
    var img = getCaptureImg();
    var p = null;
    if (1 == type) {
        //img 是图片
        //"#1DA06E" 第一个颜色
        //[0, 33, "#1D9F6E"] 第二颜色和它的相对坐标
        //[34,45, "#FFFFFF"] 第三个颜色和他的相对坐标
        //region: [1030, 100, 1, 1700] 第一个颜色的检测区域1030，100为起始坐标，1，1700为区域宽度！！！
        p = images.findMultiColors(img, "#1da06e", [[60, 0, "#1d9f6e"], [46, 45, "#ffffff"]], {
            region: [1017, 100, 10, 1700]
        });
    }
    if (!!p) {
        tLog("检测到可收取好友");
        return p;
    } else {
        tLog("p = " + p);
        return null;
    }
}

/**
 * 判断是否好有排行榜已经结束
 * @returns {boolean}
 */
function isRankEnd() {
    if (descContains("没有更多").exists()) {
        var b = descContains("没有更多").findOne();
        var bs = b.bounds();
        if (bs.centerY() < 1920) {
            return true;
        }
    }
    return false;
}

/**
 * 在排行榜页面,循环查找可收集好友
 * @returns {boolean}
 */
function enterOthers() {
    tLog("开始检查排行榜");
    sleep(3000);
    var i = 1;
    var ePoint = getHasEnergyfriend(1);
    //确保当前操作是在排行榜界面
    while (ePoint == null && textEndsWith("排行榜").exists()) {
        sleep(2000);
        swipe(520, 1800, 520, 300, 1000);
        sleep(5000);
        ePoint = getHasEnergyfriend(1);
        i++;
        //检测是否排行榜结束了
        if (isRankEnd()) {
            return false;
        }
        //如果连续32次都未检测到可收集好友,无论如何停止查找(由于程序控制了在排行榜界面,且判断了结束标记,基本已经不存在这种情况了)
        else if (i > 32) {
            tLog("程序可能出错,连续" + i + "次未检测到可收集好友");
            exit();
        }
    }
    // if (!ePoint && textContains("排行榜").exists()) {
    //     for (var i = 1; i < 50; i++) {
    //         if (!ePoint && textContains("排行榜").exists()) {
    //             sleep(2000);
    //             swipe(520, 1800, 520, 300, 500);
    //             sleep(5000);
    //             ePoint = getHasEnergyfriend(1);
    //             if (!!ePoint) {
    //                 break;
    //             }
    //             //检测是否排行榜结束了
    //             if (isRankEnd()) {
    //                 return false;
    //             } else if (i = 49) {
    //                 tLog("程序可能出错,连续" + i + "次未检测到可收集好友");
    //                 exit();
    //             }
    //         }
    //     }
    // }

    if (!!ePoint) {
        // tLog("检测到可收取好友");
        //点击位置相对找图后的修正
        // tLog(ePoint.x + "," + ePoint.y);
        click(ePoint.x, ePoint.y + 20);
        waitPage(1);
        // var falgs = clickByDesc("收", 80);
        //进去收集完后,递归调用enterOthers
        var falgs = collect();
        // tLog("falg " + falgs);
        if (falgs) {
            back();
            sleep(3000);
        } else {
            whenComplete();
        }
        enterOthers();
    } else {
        defaultException();
    }
}

/**
 * 根据描述值 点击
 * @param energyType
 * @param noFindExit
 */
function clickByDesc(energyType, paddingY, noFindExit, exceptionMsg) {
    if (descContains(energyType).exists()) {
        var energyList = descContains(energyType).find();
        // tLog("发现" + energyType + " : " + energyList.length);
        energyList.forEach(function (pos) {
            var posb = pos.bounds();
            click(posb.centerX(), posb.centerY() - paddingY);
        });
        return true;
    } else {
        if (noFindExit != null && noFindExit) {
            if (exceptionMsg != null) {
                tLog(exceptionMsg);
            } else {
                defaultException();
            }
        }
        return false;
    }
}

/**
 * 根据text值 点击 * @param energyType * @param noFindExit
 */
function clickByText(energyType, noFindExit, exceptionMsg) {
    if (textContains(energyType).exists()) {
        textContains(energyType).find().forEach(function (pos) {
            var posb = pos.bounds();
            click(posb.centerX(), posb.centerY() - 60);
        });
    } else {
        if (noFindExit != null && noFindExit) {
            if (exceptionMsg != null) {
                tLog(exceptionMsg);
                exit();
            } else {
                defaultException();
            }
        }
    }
}

/**
 * 遍历能量类型,收集自己的能量
 */
function collectionMyEnergy() {
    // tLog("遍历能量类型,收集自己的能量");
    // var energyRegex = generateCollectionType();
    // var checkInMorning = false;
    // //如果是早上7点20分左右的话.等待主页能量出现 每隔一秒检测一次
    // while (isMorningTime() && descContains("行走").exists()) {
    //     if (!checkInMorning) {
    //         tLog("等待运动能量生成中...");
    //         checkInMorning = true;
    //     }
    //     descContains("行走").find().forEach(function (pos) {
    //         var posb = pos.bounds();
    //         click(posb.centerX(), posb.centerY() - 80);
    //         sleep(1000);
    //     });
    // }
    // if (checkInMorning) {
    //     tLog("运动能量收集完成");
    // }
    // if (descMatches(energyRegex).exists()) {
    //     if (!checkInMorning) {
    //         tLog("防止小树的提示遮挡,等待中");
    //         sleep(1000);
    //     }
    //     //这里存在一定的问题：如果sleep时间短的话，就会出现循环代码在运行，循环之后的代码也在运行，感觉出现了异步，具体原因不明
    //     descMatches(energyRegex).find().forEach(function (pos) {
    //         var posb = pos.bounds();
    //         //tLog( posb.centerX());
    //         click(posb.centerX(), posb.centerY() - 100);
    //         sleep(1000);
    //     });
    // }
    collect();
    tLog("自己能量收集完成");
    sleep(5000);
}

/**
 * 结束后返回主页面
 */
function whenComplete() {
    tLog("结束");
    back();
    sleep(1500);
    back();
    exit();
}

/**
 * 遍历收取点击收取能量
 */
function collect() {
    for (var y = 460; y <= 860; y += 100) {
        for (var x = 185; x <= 890; x += 100) {
            click(x, y);
        }
    }
    return true;
}

/**
 * 根据能量类型数组生成我的能量类型正则查找字符串
 * @returns {string}
 */
function generateCollectionType() {
    tLog("根据能量类型数组生成我的能量类型正则查找字符串");
    var regex = "/";
    myEnergeType.forEach(function (t, num) {
        if (num == 0) {
            regex += "(\\s*" + t + "$)";
        } else {
            regex += "|(\\s*" + t + "$)";
        }
    });
    regex += "/";
    return regex;
}

function isMorningTime() {
    var now = new Date();
    var hour = now.getHours();
    var minu = now.getMinutes();
    var targetTime = morningTime.split(":");
    if (Number(targetTime[0]) == hour && Math.abs(Number(targetTime[1]) - minu) <= 2) {
        return true;
    } else {
        return false;
    }
}

//程序主入口
function mainEntrence() {
    //前置操作
    prepareThings();
    //注册音量下按下退出脚本监听
    registEvent();
    //从主页进入蚂蚁森林主页
    enterMyMainPage();
    //收集自己的能量
    collectionMyEnergy();
    //进入排行榜
    enterRank();
    //在排行榜检测是否有好有的能量可以收集
    enterOthers();
    //结束后返回主页面
    // whenComplete();
}

