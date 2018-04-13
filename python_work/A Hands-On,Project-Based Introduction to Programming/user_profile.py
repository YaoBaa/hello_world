#coding=utf-8
def build_profile(first_name,last_name,**user_info):
	#**让python创建一个名为user_info空字典
	profile = {}
	profile['first_name'] = first_name
	profile['last_name'] = last_name
	
	for key,value in user_info.items():
		profile[key] = value
	return profile
	
#user_profile = build_profile('yaoyao','li',location='jingzhou',ke='hb')
#print(user_profile)
