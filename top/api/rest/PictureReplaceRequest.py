'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class PictureReplaceRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.image_data = None
		self.picture_id = None

	def getapiname(self):
		return 'taobao.picture.replace'

	def getMultipartParas(self):
		return ['image_data']
