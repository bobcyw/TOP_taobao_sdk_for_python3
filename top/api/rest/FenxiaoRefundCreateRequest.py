'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class FenxiaoRefundCreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.is_return_goods = None
		self.is_return_post_fee = None
		self.refund_desc = None
		self.refund_reason_id = None
		self.return_fee = None
		self.sub_order_id = None

	def getapiname(self):
		return 'taobao.fenxiao.refund.create'
