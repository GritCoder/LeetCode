#!/usr/bin/python
# -*- coding: UTF-8 -*-
# # 142
#
# # encoding:utf-8
# import requests
# import base64
#
# # 获取 access_token
# # client_id 为官网获取的AK， client_secret 为官网获取的SK
# # host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=Y9CKqIw4ZXVsMArkEyba1ITp&client_secret=yUMoczQzY9ks63AVNhr7Nr1cftKfS4tc'
# # response = requests.get(host)
# # if response:
# #     print(response.json())
#
# # 'access_token': '24.c636eb3fa471f2da6c1ccc44c427f9fe.2592000.1605420568.282335-22830808'
#
# # # 高精度版
# # request_url = "http://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# # f = open('C:/Users/shishengli5/Desktop/res/output/0.jpg', 'rb')
# # img = base64.b64encode(f.read())
# # params = {"image":img}
# # access_token = '24.c636eb3fa471f2da6c1ccc44c427f9fe.2592000.1605420568.282335-22830808'
# # request_url = request_url + "?access_token=" + access_token
# # headers = {'content-type': 'application/x-www-form-urlencoded'}
# # response = requests.post(request_url, data=params, headers=headers)
# # if response:
# #     print (response.json())
#
# # request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general"
# # # 二进制方式打开图片文件
# # f = open('test.jpg', 'rb')
# # img = base64.b64encode(f.read())
# # params = {"image":img}
# # access_token = response.json()['access_token']# '24.c636eb3fa471f2da6c1ccc44c427f9fe.2592000.1605420568.282335-22830808'
# # print(access_token)
# # request_url = request_url + "?access_token=" + access_token
# # headers = {'content-type': 'application/x-www-form-urlencoded'}
# # response = requests.post(request_url, data=params, headers=headers)
# # if response:
# #     print (response.json())
# # f = open('./tmp.txt', encoding='utf-8')
# # for item in f.readlines():
# #     print(item)
# import cv2
# res = {'words_result': [{'words': '4头', 'location': {'top': 24, 'left': 53, 'width': 288, 'height': 41}}, {'words': '状75%□9:38', 'location': {'top': 23, 'left': 720, 'width': 310, 'height': 43}}, {'words': '<保险', 'location': {'top': 141, 'left': 36, 'width': 215, 'height': 63}}, {'words': '健康保障金', 'location': {'top': 378, 'left': 410, 'width': 313, 'height': 57}}, {'words': '最高15,000免费保障', 'location': {'top': 462, 'left': 258, 'width': 562, 'height': 71}}, {'words': '恶性肿瘤确诊可获赔免费保障天天领', 'location': {'top': 557, 'left': 190, 'width': 698, 'height': 54}}, {'words': '免费领', 'location': {'top': 646, 'left': 749, 'width': 82, 'height': 31}}, {'words': '领500元保额', 'location': {'top': 704, 'left': 395, 'width': 287, 'height': 52}}, {'words': '收益稳', 'location': {'top': 930, 'left': 323, 'width': 89, 'height': 31}}, {'words': '免息', 'location': {'top': 930, 'left': 544, 'width': 60, 'height': 30}}, {'words': '出行必备来攒钱', 'location': {'top': 1060, 'left': 48, 'width': 341, 'height': 42}}, {'words': '车险', 'location': {'top': 1062, 'left': 498, 'width': 81, 'height': 40}}, {'words': '重疾险超医保', 'location': {'top': 1059, 'left': 686, 'width': 327, 'height': 44}}, {'words': '1', 'location': {'top': 1145, 'left': 74, 'width': 711, 'height': 81}}, {'words': '1元购免费赠险在线专家健康课堂更多', 'location': {'top': 1245, 'left': 71, 'width': 924, 'height': 46}}, {'words': '医疗险超医保百万医疗险', 'location': {'top': 1371, 'left': 92, 'width': 454, 'height': 43}}, {'words': '防癌险丨安享一生', 'location': {'top': 1370, 'left': 764, 'width': 299, 'height': 41}}, {'words': '报销住院医疗费,大病小病和', 'location': {'top': 1438, 'left': 87, 'width': 562, 'height': 54}}, {'words': '报销癌症医疗费', 'location': {'top': 1440, 'left': 761, 'width': 306, 'height': 51}}, {'words': '意外', 'location': {'top': 1498, 'left': 87, 'width': 101, 'height': 51}}, {'words': '能报', 'location': {'top': 1498, 'left': 761, 'width': 96, 'height': 51}}, {'words': '￥11.84起立即购买', 'location': {'top': 1602, 'left': 136, 'width': 312, 'height': 41}}, {'words': '￥4起立即购买', 'location': {'top': 1600, 'left': 810, 'width': 242, 'height': 42}}, {'words': '本人配偶子女父母', 'location': {'top': 1803, 'left': 38, 'width': 685, 'height': 65}}, {'words': '成人保障如何配置更合理?', 'location': {'top': 1962, 'left': 80, 'width': 479, 'height': 52}}, {'words': '去了解', 'location': {'top': 1995, 'left': 832, 'width': 114, 'height': 38}}, {'words': '替上有老下有小的家庭支柱分担压力', 'location': {'top': 2027, 'left': 81, 'width': 558, 'height': 41}}, {'words': '口', 'location': {'top': 2183, 'left': 508, 'width': 59, 'height': 28}}, {'words': '首页', 'location': {'top': 2228, 'left': 143, 'width': 72, 'height': 34}}, {'words': '产品', 'location': {'top': 2226, 'left': 502, 'width': 73, 'height': 37}}, {'words': '我的', 'location': {'top': 2225, 'left': 861, 'width': 73, 'height': 38}}], 'log_id': 1316999774649450496, 'words_result_num': 31}
# words_result = res["words_result"]
#
# from cnstd import CnStd
# from cnocr import CnOcr
# import cv2
# std = CnStd()
# cn_ocr = CnOcr()
# box_info_list = std.detect('../tabbar.jpg')
# img = cv2.imread("../test.jpg")
# cv2.namedWindow('image',cv2.WINDOW_NORMAL)
# # print(box_info_list)
# for box_info in box_info_list:
#     cropped_img = box_info['cropped_img']  # 检测出的文本框
#     box = box_info["box"]
#     print(box[0], box[2])
#     cv2.rectangle(img, (box[0][0], box[0][1]), (box[2][0], box[2][1]), (255, 0, 0), 20)
#     cv2.imshow('image', cropped_img)
#     cv2.imshow('image', img)
#     cv2.waitKey(0)
#     ocr_res = cn_ocr.ocr_for_single_line(cropped_img)
#     print('ocr result: %s' % ''.join(ocr_res))