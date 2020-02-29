#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jd_assistant import Assistant

if __name__ == '__main__':
    """
    重要提示：此处为示例代码之一，请移步下面的链接查看使用教程👇
    https://github.com/tychxn/jd-assistant/wiki/1.-%E4%BA%AC%E4%B8%9C%E6%8A%A2%E8%B4%AD%E5%8A%A9%E6%89%8B%E7%94%A8%E6%B3%95

    定时预约功能
    https://github.com/tychxn/jd-assistant/pull/109
    """

    # sku_ids 商品id
    # sku_ids = '100011521400'  # 振德 （ZHENDE) 口罩一次性医用口罩 预约21点 抢购10点 数量3000
    # sku_ids = '100011551632'  # 3Q医用口罩  预约15点 抢购20点 数量10000
    # sku_ids = '65708238590'  # 袋鼠医生  预约15点 抢购20点 数量？？

    sku_ids = '100011521400'
    area = '12_904_905_50601'  # 区域id
    reserve_time = '2020-02-29 21:00:02.500'  # 预约时间
    buy_time = '2020-02-29 10:00:00.800'  # 抢购时间

    asst = Assistant()  # 初始化
    asst.login_by_QRcode()  # 扫码登陆

    # 1.预约商品
    # asst.make_reserve(sku_id=sku_ids, buy_time=reserve_time)
    # 2个参数
    # sku_id: 商品id
    # buy_time: 预约时间，例如：'2019-11-10 22:41:30.000'

    # 2.定时抢购商品(可以加入购物车)
    asst.exec_reserve_seckill_by_time(sku_id=sku_ids, buy_time=buy_time, retry=2, interval=2, num=1)
    # 5个参数
    # sku_id: 商品id
    # buy_time: 抢购时间，例如：'2019-11-10 22:41:30.000'
    # retry: 抢购重复执行次数，可选参数，默认4次
    # interval: 抢购执行间隔，可选参数，默认4秒
    # num: 购买数量，可选参数，默认1个

    # 3.定时抢购商品(不可加入购物车)
    # asst.exec_seckill_by_time(sku_ids=sku_ids, buy_time=buy_time, retry=2, interval=2, num=1)
    # 5个参数
    # sku_ids: 商品id，多个商品id用逗号进行分割，如"123,456,789"
    # buy_time: 下单时间，例如：'2018-09-28 22:45:50.000'
    # retry: 抢购重复执行次数，可选参数，默认4次
    # interval: 抢购执行间隔，可选参数，默认4秒
    # num: 购买数量，可选参数，默认1个
