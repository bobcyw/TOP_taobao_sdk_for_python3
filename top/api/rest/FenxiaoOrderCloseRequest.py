'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class FenxiaoOrderCloseRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.message = None
		self.purchase_order_id = None
		self.sub_order_ids = None

	def getapiname(self):
		return 'taobao.fenxiao.order.close'
