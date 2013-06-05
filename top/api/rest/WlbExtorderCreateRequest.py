'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class WlbExtorderCreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.buyer_nick = None
		self.expect_end_time = None
		self.expect_start_time = None
		self.ext_flag = None
		self.ext_order_code = None
		self.ext_order_source = None
		self.ext_prev_order_id = None
		self.invoince_info = None
		self.op_main_type = None
		self.operate_code = None
		self.operate_type = None
		self.order_item_list = None
		self.order_type = None
		self.package_count = None
		self.postage = None
		self.receiver_info = None
		self.remark = None
		self.retailer = None
		self.return_tms_code = None
		self.schedule_end = None
		self.schedule_start = None
		self.schedule_type = None
		self.sender_info = None
		self.service_fee = None
		self.shipping_type = None
		self.sub_ext_order_code = None
		self.tms_code = None
		self.tms_tp_code = None
		self.total_price = None
		self.trade_order_type = None
		self.wms_code = None
		self.wms_code_destination = None

	def getapiname(self):
		return 'taobao.wlb.extorder.create'
