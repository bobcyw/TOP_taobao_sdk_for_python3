'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class PromotionCoupondetailGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.buyer_nick = None
		self.coupon_id = None
		self.end_time = None
		self.extend_params = None
		self.page_no = None
		self.page_size = None
		self.state = None

	def getapiname(self):
		return 'taobao.promotion.coupondetail.get'
