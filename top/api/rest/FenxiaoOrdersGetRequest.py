'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class FenxiaoOrdersGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_created = None
		self.fields = None
		self.page_no = None
		self.page_size = None
		self.purchase_order_id = None
		self.start_created = None
		self.status = None
		self.tc_order_id = None
		self.time_type = None

	def getapiname(self):
		return 'taobao.fenxiao.orders.get'
