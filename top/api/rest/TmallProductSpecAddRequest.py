'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class TmallProductSpecAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.barcode = None
		self.certified_pic_str = None
		self.certified_txt_str = None
		self.change_prop = None
		self.image = None
		self.market_time = None
		self.product_code = None
		self.product_id = None
		self.spec_props = None
		self.spec_props_alias = None

	def getapiname(self):
		return 'tmall.product.spec.add'

	def getMultipartParas(self):
		return ['image']
