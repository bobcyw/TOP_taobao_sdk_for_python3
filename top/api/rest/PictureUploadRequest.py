'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class PictureUploadRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.image_input_title = None
		self.img = None
		self.picture_category_id = None
		self.title = None

	def getapiname(self):
		return 'taobao.picture.upload'

	def getMultipartParas(self):
		return ['img']
