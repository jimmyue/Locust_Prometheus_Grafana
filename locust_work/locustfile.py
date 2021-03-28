#!/usr/bin/python3
# -*- coding:utf-8 -*-
import requests
import json
import queue
from locust import HttpUser,TaskSet,task,between

class HondaLogin(TaskSet):
	@task(1)
	def work_user_top(self):
		headers={"content-type":"application/json; charset=UTF-8"}
		data={"data":{"userName":"QIUZHANFENG","password":"abc.123"}}
		with self.client.post("/api/services-admin/login",name="login",headers=headers,data=json.dumps(data),catch_response=True) as response:
			if response.status_code==200 and response.json()['status']['status']==0:
				response.success()
			else:
				response.failure("登录 接口异常！")
				print(response.text)

class WebsiteUser(HttpUser):
	tasks = [HondaLogin]
	host='http://10.10.22.23:3000'
	wait_time = between(1,3)
