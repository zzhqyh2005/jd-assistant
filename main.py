#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jd_assistant import Assistant

if __name__ == '__main__':
    """
    重要提示：此处为示例代码之一，请移步下面的链接查看使用教程👇
    https://github.com/tychxn/jd-assistant/wiki/1.-%E4%BA%AC%E4%B8%9C%E6%8A%A2%E8%B4%AD%E5%8A%A9%E6%89%8B%E7%94%A8%E6%B3%95
    """
    # sku_ids 商品id
    # sku_ids = '100011521400'  # 振德 （ZHENDE) 口罩一次性医用口罩 预约21点 抢购10点 数量3000
    # sku_ids = '100011551632'  # 3Q医用口罩  预约15点 抢购20点 数量10000
    # sku_ids = '65708238590'  # 袋鼠医生  预约15点 抢购20点 数量？？

    sku_ids = '100011551632'
    area = '12_904_905_50601'  # 区域id
    buy_time = '2020-02-16 01:17:59.500'  # 下单时间

    asst = Assistant()  # 初始化
    asst.login_by_QRcode()  # 扫码登陆

    # 1.根据商品id添加购物车,下单
    asst.add_item_to_cart(sku_ids=sku_ids)
    # 提交订单
    asst.submit_order()

    # 2.清空购物车,下单
    # asst.clear_cart()
    # asst.submit_order() # 提交订单

    # 4.定时提交订单示例（常用）
    # asst.submit_order_by_time(buy_time=buy_time, retry=4, interval=5)  # 定时提交订单
    # 3个参数：
    # buy_time: 下单时间，例如：'2019-02-16 01:17:59.500'
    # retry: 下单重复执行次数，可选参数，默认4次
    # interval: 下单执行间隔，可选参数，默认5秒

    # 5.根据商品是否有货自动下单
    # asst.buy_item_in_stock(sku_ids=sku_ids, area=area, wait_all=False, stock_interval=5)
    # 6个参数：
    # sku_ids: 商品id。可以设置多个商品，也可以带数量，如：'1234' 或 '1234,5678' 或 '1234:2' 或 '1234:2,5678:3'
    # area: 地区id
    # wait_all: 是否等所有商品都有货才一起下单，可选参数，默认False
    # stock_interval: 查询库存时间间隔，可选参数，默认3秒
    # submit_retry: 提交订单失败后重试次数，可选参数，默认3次
    # submit_interval: 提交订单失败后重试时间间隔，可选参数，默认5秒
