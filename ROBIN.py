Black="\033[1;30m"       # Black
Red="\033[1;31m"         # Red
Green="\033[1;32m"       # 'هGreen
Yellow="\033[1;33m"      # Yellow
Blue="\033[1;34m"        # Blue
Purple="\033[1;35m"      # Purple
Cyan="\033[1;36m"        # Cyan
White="\033[1;37m"       # White
_=f'{White}[{Yellow}+{White}]{White} - '
def hasanat():
	global error , good , bad , id ,  csrftoken , si  ,s ,k ,text
	print(f'''
{Red}====================== 
{Cyan}Done {Green} >>> {good} 
{Cyan}bad {Purple} >>> {bad}  
{Cyan}Block {Red} >>> {error} 
{Cyan}link {White} >>> {link}
{Cyan}seconse {White} >>> {s}
{Cyan}text {White} >>> text
{Red}======================     ''')
	while True:
		
		k+=1
		if k == 11:
			k=0
			
		data={
			'is_prefetch': 'false',
			'omit_cover_media': 'false',
			'module': 'explore_popular',
			'use_sectional_payload': 'true',
			'include_fixed_destinations': 'true'
		}
		url='https://i.instagram.com/api/v1/discover/web/explore_grid/?is_prefetch=false&omit_cover_media=false&module=explore_popular&use_sectional_payload=true&include_fixed_destinations=true'
		headers={
			'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'content-length': '16',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; shbid="6501\{id}\0541689888481:01f73c5c447b81316667f3fef03e854ec17819127a3a7cfc708b6d6e3b1375631101f397"; shbts="1658352481\{id}\0541689888481:01f71e2280fe2389aebca035d43296bda632ccf8386b2b0d3dbc3285dce2018e676c77fc"; ds_user_id={id}; csrftoken={csrftoken}; sessionid={si}; rur="NAO/{id}\0541690144166:01f716870c4d087f0dc86549dd21ad03c1b4a998a97bce93ceda73f7ddfef603bcf6b03a"',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/',
		'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
		'x-asbd-id': '198387',
		'x-csrftoken': csrftoken,
		'x-frame-options': 'SAMEORIGIN',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': 'hmac.AR0CTssDFfvaLymrF2w77U_v94Xm9xDN1zVkcHJhaK2vaDs3',
		'x-instagram-ajax': '1006179778'
		}
		req=rs.get(url,headers=headers,data=data).json()['sectional_items'][0]['layout_content']['fill_items']
		try:
			q=req[k]['media']['pk']
		except :
			
			k=1
			req=rs.get(url,headers=headers,data=data).json()['sectional_items'][0]['layout_content']['fill_items']
			q=req[k]['media']['pk']
		for i in req:
			nex=next(text , 'إنّ اللهَ وملائكتَهُ يُصَـلُّونَ على النبي يا أيها الذين آمنوا صَلُّوا عليه وسلِّمُوا تسليما')
			if nex == 'إنّ اللهَ وملائكتَهُ يُصَـلُّونَ على النبي يا أيها الذين آمنوا صَلُّوا عليه وسلِّمُوا تسليما':
				text = iter(['استغفروا' , 'صلوا على الرسول' , 'اذكرا الله' ,'اكتب شيء يشفع لك' ,'اكتب شيء تؤجر عليه'  , 'مَنْ عَمِلَ صَالِحًا مِّن ذَكَرٍ أَوْ أُنثَى وَهُوَ مُؤْمِنٌ فَلَنُحْيِيَنَّهُ حَيَاةً طَيِّبَةً وَلَنَجْزِيَنَّهُمْ أَجْرَهُم بِأَحْسَنِ مَا كَانُواْ يَعْمَلُونَ' ])
			text1=nex
			
			link='https://www.instagram.com/reel/'+i['media']['code']
			
			
			comment=rs.post(f'https://i.instagram.com/api/v1/web/comments/{q}/add/',data={
		'comment_text': text1
		},headers={
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'content-length': '16',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; shbid="6501\{id}\0541689888481:01f73c5c447b81316667f3fef03e854ec17819127a3a7cfc708b6d6e3b1375631101f397"; shbts="1658352481\{id}\0541689888481:01f71e2280fe2389aebca035d43296bda632ccf8386b2b0d3dbc3285dce2018e676c77fc"; ds_user_id={id}; csrftoken={csrftoken}; sessionid={si}; rur="NAO/{id}\0541690144166:01f716870c4d087f0dc86549dd21ad03c1b4a998a97bce93ceda73f7ddfef603bcf6b03a"',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/',
		'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
		'x-asbd-id': '198387',
		'x-csrftoken': csrftoken,
		'x-frame-options': 'SAMEORIGIN',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': 'hmac.AR0CTssDFfvaLymrF2w77U_v94Xm9xDN1zVkcHJhaK2vaDs3',
		'x-instagram-ajax': '1006179778'
		}).json()
			
			try:
			  if comment["feedback_title"]=="Try Again Later":
			    error+=1
			    s=1000
			
			except :
				pass
			try:
				if comment['message']=='Unable to post comment.':
				  bad+=1
				  s=j
			except :
				pass
			if comment["status"]=="ok":
			    good+=1
			    s=j
			print(f'''
{Red}====================== 
{Cyan}Done {Green} >>> {good} 
{Cyan}bad {Purple} >>> {bad}  
{Cyan}Block {Red} >>> {error} 
{Cyan}link {White} >>> {link}
{Cyan}seconse {White} >>> {s}
{Cyan}text {White} >>> {text1}
{Red}======================     ''')
			sleep(s)














def comment():
	global error , good , bad , id ,  csrftoken , si  ,s ,k ,text
	print(f'''
{Red}====================== 
{Cyan}Done {Green} >>> {good} 
{Cyan}bad {Purple} >>> {bad}  
{Cyan}Block {Red} >>> {error} 
{Cyan}link {White} >>> {link}
{Cyan}seconse {White} >>> {s}
{Cyan}text {White} >>> text
{Red}======================     ''')
	while True:
		
		k+=1
		if k == 11:
			k=0
			
		data={
			'is_prefetch': 'false',
			'omit_cover_media': 'false',
			'module': 'explore_popular',
			'use_sectional_payload': 'true',
			'include_fixed_destinations': 'true'
		}
		url='https://i.instagram.com/api/v1/discover/web/explore_grid/?is_prefetch=false&omit_cover_media=false&module=explore_popular&use_sectional_payload=true&include_fixed_destinations=true'
		headers={
			'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'content-length': '16',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; shbid="6501\{id}\0541689888481:01f73c5c447b81316667f3fef03e854ec17819127a3a7cfc708b6d6e3b1375631101f397"; shbts="1658352481\{id}\0541689888481:01f71e2280fe2389aebca035d43296bda632ccf8386b2b0d3dbc3285dce2018e676c77fc"; ds_user_id={id}; csrftoken={csrftoken}; sessionid={si}; rur="NAO/{id}\0541690144166:01f716870c4d087f0dc86549dd21ad03c1b4a998a97bce93ceda73f7ddfef603bcf6b03a"',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/',
		'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
		'x-asbd-id': '198387',
		'x-csrftoken': csrftoken,
		'x-frame-options': 'SAMEORIGIN',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': 'hmac.AR0CTssDFfvaLymrF2w77U_v94Xm9xDN1zVkcHJhaK2vaDs3',
		'x-instagram-ajax': '1006179778'
		}
		req=rs.get(url,headers=headers,data=data).json()['sectional_items'][0]['layout_content']['fill_items']
		try:
			q=req[k]['media']['pk']
		except :
			pass
			
			k=1
			req=rs.get(url,headers=headers,data=data).json()['sectional_items'][0]['layout_content']['fill_items']
			q=req[k]['media']['pk']
		for i in req:
			
			
			
			link='https://www.instagram.com/reel/'+i['media']['code']
			
			
			comment=rs.post(f'https://i.instagram.com/api/v1/web/comments/{q}/add/',data={
		'comment_text': text 
		},headers={
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'content-length': '16',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; shbid="6501\{id}\0541689888481:01f73c5c447b81316667f3fef03e854ec17819127a3a7cfc708b6d6e3b1375631101f397"; shbts="1658352481\{id}\0541689888481:01f71e2280fe2389aebca035d43296bda632ccf8386b2b0d3dbc3285dce2018e676c77fc"; ds_user_id={id}; csrftoken={csrftoken}; sessionid={si}; rur="NAO/{id}\0541690144166:01f716870c4d087f0dc86549dd21ad03c1b4a998a97bce93ceda73f7ddfef603bcf6b03a"',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/',
		'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
		'x-asbd-id': '198387',
		'x-csrftoken': csrftoken,
		'x-frame-options': 'SAMEORIGIN',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': 'hmac.AR0CTssDFfvaLymrF2w77U_v94Xm9xDN1zVkcHJhaK2vaDs3',
		'x-instagram-ajax': '1006179778'
		}).json()
			
			try:
			  if comment["feedback_title"]=="Try Again Later":
			    error+=1
			    s=1000
			
			except :
				pass
			try:
				if comment['message']=='Unable to post comment.':
				  bad+=1
				  s=j
			except :
				pass
			if comment["status"]=="ok":
			    good+=1
			    s=j
			print(f'''
{Red}====================== 
{Cyan}Done {Green} >>> {good} 
{Cyan}bad {Purple} >>> {bad}  
{Cyan}Block {Red} >>> {error} 
{Cyan}link {White} >>> {link}
{Cyan}seconse {White} >>> {s}
{Cyan}text {White} >>> {text}
{Red}======================     ''')
			sleep(s)
		


















def comment_ch():
	global error , good , bad , id ,  csrftoken , si  ,s ,k ,text
	print(f'''
{Red}====================== 
{Cyan}Done {Green} >>> {good} 
{Cyan}bad {Purple} >>> {bad}  
{Cyan}Block {Red} >>> {error} 
{Cyan}link {White} >>> link
{Cyan}seconse {White} >>> {s}
{Cyan}text {White} >>> {text}
{Red}======================     ''')
	while True:
		
		k+=1
		if k == 11:
			k=0
			
		data={
			'username': 'fx_py3'}
		url=f'https://i.instagram.com/api/v1/users/web_profile_info/?username={use}'
		headers={
			'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'content-length': '16',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; shbid="6501\{id}\0541689888481:01f73c5c447b81316667f3fef03e854ec17819127a3a7cfc708b6d6e3b1375631101f397"; shbts="1658352481\{id}\0541689888481:01f71e2280fe2389aebca035d43296bda632ccf8386b2b0d3dbc3285dce2018e676c77fc"; ds_user_id={id}; csrftoken={csrftoken}; sessionid={si}; rur="NAO/{id}\0541690144166:01f716870c4d087f0dc86549dd21ad03c1b4a998a97bce93ceda73f7ddfef603bcf6b03a"',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/',
		'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
		'x-asbd-id': '198387',
		'x-csrftoken': csrftoken,
		'x-frame-options': 'SAMEORIGIN',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': 'hmac.AR0CTssDFfvaLymrF2w77U_v94Xm9xDN1zVkcHJhaK2vaDs3',
		'x-instagram-ajax': '1006179778'
		}
		try:
			req=rs.get(url,headers=headers,data=data).json()['data']['user']['edge_owner_to_timeline_media']['edges']
		except :
			print('Api bolcked you !')
			exit()
		for i in req:
				q=i['node']['id']
				link='https://www.instagram.com/reel/'+i['node']['shortcode']
				
				comment=rs.post(f'https://i.instagram.com/api/v1/web/comments/{q}/add/',data={
			'comment_text': text 
			},headers={
			'accept': '*/*',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
			'content-length': '16',
			'content-type': 'application/x-www-form-urlencoded',
			'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; shbid="6501\{id}\0541689888481:01f73c5c447b81316667f3fef03e854ec17819127a3a7cfc708b6d6e3b1375631101f397"; shbts="1658352481\{id}\0541689888481:01f71e2280fe2389aebca035d43296bda632ccf8386b2b0d3dbc3285dce2018e676c77fc"; ds_user_id={id}; csrftoken={csrftoken}; sessionid={si}; rur="NAO/{id}\0541690144166:01f716870c4d087f0dc86549dd21ad03c1b4a998a97bce93ceda73f7ddfef603bcf6b03a"',
			'origin': 'https://www.instagram.com',
			'referer': 'https://www.instagram.com/',
			'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-site',
			'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
			'x-asbd-id': '198387',
			'x-csrftoken': csrftoken,
			'x-frame-options': 'SAMEORIGIN',
			'x-ig-app-id': '936619743392459',
			'x-ig-www-claim': 'hmac.AR0CTssDFfvaLymrF2w77U_v94Xm9xDN1zVkcHJhaK2vaDs3',
			'x-instagram-ajax': '1006179778'
			}).json()
				
				try:
				  if comment["feedback_title"]=="Try Again Later":
				    error+=1
				    s=1000
				
				except :
					pass
				try:
					if comment['message']=='Unable to post comment.':
					  bad+=1
					  s=j
				except :
					pass
				if comment["status"]=="ok":
				    good+=1
				    s=j
				print(f'''
{Red}====================== 
{Cyan}Done {Green} >>> {good} 
{Cyan}bad {Purple} >>> {bad}  
{Cyan}Block {Red} >>> {error} 
{Cyan}link {White} >>> {link}
{Cyan}seconse {White} >>> {s}
{Cyan}text {White} >>> {text}
{Red}======================     ''')
				sleep(s)
		





















def like_ch():
	global error , good , bad , id ,  csrftoken , si  ,s ,k ,text ,use
	print(f'''
{Red}====================== 
{Cyan}Done {Green} >>> {good} 
{Cyan}bad {Purple} >>> {bad}  
{Cyan}Block {Red} >>> {error} 
{Cyan}link {White} >>> link
{Cyan}seconse {White} >>> {s}
{Red}======================     ''')
	while True:
		
		k+=1
		if k == 11:
			k=0
			
		data={
			'username': 'fx_py3'}
		url=f'https://i.instagram.com/api/v1/users/web_profile_info/?username={use}'
		headers={
			'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'content-length': '16',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; shbid="6501\{id}\0541689888481:01f73c5c447b81316667f3fef03e854ec17819127a3a7cfc708b6d6e3b1375631101f397"; shbts="1658352481\{id}\0541689888481:01f71e2280fe2389aebca035d43296bda632ccf8386b2b0d3dbc3285dce2018e676c77fc"; ds_user_id={id}; csrftoken={csrftoken}; sessionid={si}; rur="NAO/{id}\0541690144166:01f716870c4d087f0dc86549dd21ad03c1b4a998a97bce93ceda73f7ddfef603bcf6b03a"',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/',
		'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
		'x-asbd-id': '198387',
		'x-csrftoken': csrftoken,
		'x-frame-options': 'SAMEORIGIN',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': 'hmac.AR0CTssDFfvaLymrF2w77U_v94Xm9xDN1zVkcHJhaK2vaDs3',
		'x-instagram-ajax': '1006179778'
		}
		try:
			req=rs.get(url,headers=headers,data=data).json()['data']['user']['edge_owner_to_timeline_media']['edges']
		except :
			print('Api bolcked you !')
			exit()
		for i in req:
				q=i['node']['id']
				link='https://www.instagram.com/reel/'+i['node']['shortcode']
				
				like=rs.post(f'https://www.instagram.com/web/likes/{q}/like/',headers={
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'content-length': '0',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; shbid="6501\{id}\0541689888481:01f73c5c447b81316667f3fef03e854ec17819127a3a7cfc708b6d6e3b1375631101f397"; shbts="1658352481\{id}\0541689888481:01f71e2280fe2389aebca035d43296bda632ccf8386b2b0d3dbc3285dce2018e676c77fc"; ds_user_id={id}; csrftoken={csrftoken}; sessionid={si}; rur="NAO/{id}\0541690144166:01f716870c4d087f0dc86549dd21ad03c1b4a998a97bce93ceda73f7ddfef603bcf6b03a"',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/',
		'sec-ch-prefers-color-scheme': 'light',
		'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
		'x-asbd-id': '198387',
		'x-csrftoken': csrftoken,
		'x-frame-options': 'SAMEORIGIN',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': 'hmac.AR0CTssDFfvaLymrF2w77U_v94Xm9xDN1zVkcHJhaK2vaDs3',
		'x-instagram-ajax': '1006179778'
		}).json()
		try:
			  if like["feedback_title"]=="Try Again Later":
			    error+=1
			    s=1000
			
		except :
				pass
		try:
				if like['message']=='Unable to post like.':
				  bad+=1
				  s=j
		except :
				pass
		if like["status"]=="ok":
			    good+=1
			    s=j
		print(f'''
{Red}====================== 
{Cyan}Done {Green} >>> {good} 
{Cyan}bad {Purple} >>> {bad}  
{Cyan}Block {Red} >>> {error} 
{Cyan}link {White} >>> {link}
{Cyan}seconse {White} >>> {s}
{Red}======================     ''')
		sleep(s)































def like_ex():
	global error , good , bad , id ,  csrftoken , si  ,s ,k ,text
	print(f'''
====================== 
Done >>> {good} 
bad >>> {bad}  
Block >>> {error} 
link >>> link
seconse >>> {s}
======================     ''')
	while True:
		k+=1
		if k == 11:
			k=0
		data={
			'is_prefetch': 'false',
			'omit_cover_media': 'false',
			'module': 'explore_popular',
			'use_sectional_payload': 'true',
			'include_fixed_destinations': 'true'
		}
		url='https://i.instagram.com/api/v1/discover/web/explore_grid/?is_prefetch=false&omit_cover_media=false&module=explore_popular&use_sectional_payload=true&include_fixed_destinations=true'
		headers={
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'content-length': '16',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; shbid="6501\{id}\0541689888481:01f73c5c447b81316667f3fef03e854ec17819127a3a7cfc708b6d6e3b1375631101f397"; shbts="1658352481\{id}\0541689888481:01f71e2280fe2389aebca035d43296bda632ccf8386b2b0d3dbc3285dce2018e676c77fc"; ds_user_id={id}; csrftoken={csrftoken}; sessionid={si}; rur="NAO/{id}\0541690144166:01f716870c4d087f0dc86549dd21ad03c1b4a998a97bce93ceda73f7ddfef603bcf6b03a"',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/',
		'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
		'x-asbd-id': '198387',
		'x-csrftoken': csrftoken,
		'x-frame-options': 'SAMEORIGIN',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': 'hmac.AR0CTssDFfvaLymrF2w77U_v94Xm9xDN1zVkcHJhaK2vaDs3',
		'x-instagram-ajax': '1006179778'
		}
		req=rs.get(url,headers=headers,data=data).json()['sectional_items'][0]['layout_content']['fill_items']
		try:
			q=req[k]['media']['pk']
		except :
			
			k=1
			req=rs.get(url,headers=headers,data=data).json()['sectional_items'][0]['layout_content']['fill_items']
			q=req[k]['media']['pk']
		for i in req:
			
			
			
			link='https://www.instagram.com/reel/'+i['media']['code']
			
			
			
			like=rs.post(f'https://www.instagram.com/web/likes/{q}/like/',headers={
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'content-length': '0',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; shbid="6501\{id}\0541689888481:01f73c5c447b81316667f3fef03e854ec17819127a3a7cfc708b6d6e3b1375631101f397"; shbts="1658352481\{id}\0541689888481:01f71e2280fe2389aebca035d43296bda632ccf8386b2b0d3dbc3285dce2018e676c77fc"; ds_user_id={id}; csrftoken={csrftoken}; sessionid={si}; rur="NAO/{id}\0541690144166:01f716870c4d087f0dc86549dd21ad03c1b4a998a97bce93ceda73f7ddfef603bcf6b03a"',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/',
		'sec-ch-prefers-color-scheme': 'light',
		'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
		'x-asbd-id': '198387',
		'x-csrftoken': csrftoken,
		'x-frame-options': 'SAMEORIGIN',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': 'hmac.AR0CTssDFfvaLymrF2w77U_v94Xm9xDN1zVkcHJhaK2vaDs3',
		'x-instagram-ajax': '1006179778'
		}).json()
			
			try:
			  if like["feedback_title"]=="Try Again Later":
			    error+=1
			    s=1000
			
			except :
				pass
			try:
				if like['message']=='Unable to post like.':
				  bad+=1
				  s=j
			except :
				pass
			if like["status"]=="ok":
			    good+=1
			    s=j
			print(f'''
{Red}====================== 
{Cyan}Done {Green} >>> {good} 
{Cyan}bad {Purple} >>> {bad}  
{Cyan}Block {Red} >>> {error} 
{Cyan}link {White} >>> {link}
{Cyan}seconse {White} >>> {s}
{Red}======================     ''')
			sleep(s)










def users(k):
	url=f'https://i.instagram.com/api/v1/friendships/{id}/following/?count=1000'
	headers={
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	    'accept-encoding': 'gzip, deflate, br',
	    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
	    'cache-control': 'max-age=0',
	    'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; ds_user_id={id}; shbid="6501\{id}\0541690153954:01f73336d2f16eae237610a06f5bcd1f504113d2f3f5a8272e7a3632b1c49a2b38d996b8"; shbts="1658617954\{id}\0541690153954:01f7daef559297f48fade12c799d37d559c1714e6d5f1c748d113e3afe054482d99ce705"; csrftoken={csrftoken}; sessionid={si}; rur="NAO\{id}\0541690220317:01f7a8da6b0e6b43e92dfc93007569e40f9e2e1b878df993fcb2864254ddd65cdb5e7daf"',
	    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'none',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
	    'x-frame-options': 'SAMEORIGIN'
	    }
	req=requests.get(url,headers=headers)
	r=req.json()['users']
	use=r[k]['username']
	yield use


def like_following():
	global error , good , bad , id ,  csrftoken , si  ,s ,k ,text ,use
	
	print(f'''
====================== 
Done >>> {good} 
bad >>> {bad}  
Block >>> {error} 
link >>> link
seconse >>> 0
======================     ''')
	while True:
		use=next(users(k))
		k+=1
		if k == 11:
			k=0
			
		data={
			'username': 'fx_py3'}
		url=f'https://i.instagram.com/api/v1/users/web_profile_info/?username={use}'
		headers={
			'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'content-length': '16',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; shbid="6501\{id}\0541689888481:01f73c5c447b81316667f3fef03e854ec17819127a3a7cfc708b6d6e3b1375631101f397"; shbts="1658352481\{id}\0541689888481:01f71e2280fe2389aebca035d43296bda632ccf8386b2b0d3dbc3285dce2018e676c77fc"; ds_user_id={id}; csrftoken={csrftoken}; sessionid={si}; rur="NAO/{id}\0541690144166:01f716870c4d087f0dc86549dd21ad03c1b4a998a97bce93ceda73f7ddfef603bcf6b03a"',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/',
		'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
		'x-asbd-id': '198387',
		'x-csrftoken': csrftoken,
		'x-frame-options': 'SAMEORIGIN',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': 'hmac.AR0CTssDFfvaLymrF2w77U_v94Xm9xDN1zVkcHJhaK2vaDs3',
		'x-instagram-ajax': '1006179778'
		}
		try:
			req=rs.get(url,headers=headers,data=data).json()['data']['user']['edge_owner_to_timeline_media']['edges']
		except :
			print('Api bolcked you !')
			exit()
		for i in req:
				q=i['node']['id']
				link='https://www.instagram.com/reel/'+i['node']['shortcode']
				
				like=rs.post(f'https://www.instagram.com/web/likes/{q}/like/',headers={
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'content-length': '0',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; shbid="6501\{id}\0541689888481:01f73c5c447b81316667f3fef03e854ec17819127a3a7cfc708b6d6e3b1375631101f397"; shbts="1658352481\{id}\0541689888481:01f71e2280fe2389aebca035d43296bda632ccf8386b2b0d3dbc3285dce2018e676c77fc"; ds_user_id={id}; csrftoken={csrftoken}; sessionid={si}; rur="NAO/{id}\0541690144166:01f716870c4d087f0dc86549dd21ad03c1b4a998a97bce93ceda73f7ddfef603bcf6b03a"',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/',
		'sec-ch-prefers-color-scheme': 'light',
		'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
		'x-asbd-id': '198387',
		'x-csrftoken': csrftoken,
		'x-frame-options': 'SAMEORIGIN',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': 'hmac.AR0CTssDFfvaLymrF2w77U_v94Xm9xDN1zVkcHJhaK2vaDs3',
		'x-instagram-ajax': '1006179778'
		}).json()
				try:
					  if like["feedback_title"]=="Try Again Later":
					    error+=1
					    s=1000
					
				except :
						pass
				try:
						if like['message']=='Unable to post comment.':
						  bad+=1
						  s=j
				except :
						pass
				if like["status"]=="ok":
					    good+=1
					    s=j
				print(f'''
====================== 
Done >>> {good} 
bad >>> {bad}  
Block >>> {error} 
link >>> {link}
seconse >>> {s}
======================     ''')
				sleep(s)




















def comment_following():
	global error , good , bad , id ,  csrftoken , si  ,s ,k ,text ,use
	
	print(f'''
{Red}====================== 
{Cyan}Done {Green} >>> {good} 
{Cyan}bad {Purple} >>> {bad}  
{Cyan}Block {Red} >>> {error} 
{Cyan}link {White} >>> link
{Cyan}seconse {White} >>> {s}
{Cyan}text {White} >>> {text}
{Red}======================     ''')
	while True:
		use=next(users(k))
		k+=1
		if k == 11:
			k=0
			
		data={
			'username': 'fx_py3'}
		url=f'https://i.instagram.com/api/v1/users/web_profile_info/?username={use}'
		headers={
			'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'content-length': '16',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; shbid="6501\{id}\0541689888481:01f73c5c447b81316667f3fef03e854ec17819127a3a7cfc708b6d6e3b1375631101f397"; shbts="1658352481\{id}\0541689888481:01f71e2280fe2389aebca035d43296bda632ccf8386b2b0d3dbc3285dce2018e676c77fc"; ds_user_id={id}; csrftoken={csrftoken}; sessionid={si}; rur="NAO/{id}\0541690144166:01f716870c4d087f0dc86549dd21ad03c1b4a998a97bce93ceda73f7ddfef603bcf6b03a"',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/',
		'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
		'x-asbd-id': '198387',
		'x-csrftoken': csrftoken,
		'x-frame-options': 'SAMEORIGIN',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': 'hmac.AR0CTssDFfvaLymrF2w77U_v94Xm9xDN1zVkcHJhaK2vaDs3',
		'x-instagram-ajax': '1006179778'
		}
		try:
			req=rs.get(url,headers=headers,data=data).json()['data']['user']['edge_owner_to_timeline_media']['edges']
		except :
			print('Api bolcked you !')
			exit()
		for i in req:
				q=i['node']['id']
				link='https://www.instagram.com/reel/'+i['node']['shortcode']
				
				comment=rs.post(f'https://i.instagram.com/api/v1/web/comments/{q}/add/',data={
			'comment_text': text },headers={
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		'content-length': '0',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': f'ig_did=37396E22-2BAA-45B4-BE12-2C138F2EE907; ig_nrcb=1; mid=Yoo2NAALAAF_bSUg9E76T9FjnyOg; datr=1w6bYk9s5Fe7mNlwoBvLzX_d; shbid="6501\{id}\0541689888481:01f73c5c447b81316667f3fef03e854ec17819127a3a7cfc708b6d6e3b1375631101f397"; shbts="1658352481\{id}\0541689888481:01f71e2280fe2389aebca035d43296bda632ccf8386b2b0d3dbc3285dce2018e676c77fc"; ds_user_id={id}; csrftoken={csrftoken}; sessionid={si}; rur="NAO/{id}\0541690144166:01f716870c4d087f0dc86549dd21ad03c1b4a998a97bce93ceda73f7ddfef603bcf6b03a"',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/',
		'sec-ch-prefers-color-scheme': 'light',
		'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
		'x-asbd-id': '198387',
		'x-csrftoken': csrftoken,
		'x-frame-options': 'SAMEORIGIN',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': 'hmac.AR0CTssDFfvaLymrF2w77U_v94Xm9xDN1zVkcHJhaK2vaDs3',
		'x-instagram-ajax': '1006179778'
		}).json()
				try:
					  if comment["feedback_title"]=="Try Again Later":
					    error+=1
					    s=1000
					
				except :
						pass
				try:
						if comment['message']=='Unable to post comment.':
						  bad+=1
						  s=j
				except :
						pass
				if comment["status"]=="ok":
					    good+=1
					    s=j
				print(f'''
{Red}====================== 
{Cyan}Done {Green} >>> {good} 
{Cyan}bad {Purple} >>> {bad}  
{Cyan}Block {Red} >>> {error} 
{Cyan}link {White} >>> {link}
{Cyan}seconse {White} >>> {s}
{Cyan}text {White} >>> {text}
{Red}======================     ''')
				sleep(s)






















import requests
from time import sleep
print(f'''

{Yellow}TELEGRAM {White}: FX_PY3
{Yellow}INSTAGRAM {White}: FX_PY
{Red}

██████╗  ██████╗ ██████╗ ██╗███╗   ██╗
██╔══██╗██╔═══██╗██╔══██╗██║████╗  ██║
██████╔╝██║   ██║██████╔╝██║██╔██╗ ██║
██╔══██╗██║   ██║██╔══██╗██║██║╚██╗██║
██║  ██║╚██████╔╝██████╔╝██║██║ ╚████║
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝
                                      

{White}[{Red}1{White}]{Yellow} - AJR  
{White}[{Red}2{White}]{Yellow} - Comment explore
{White}[{Red}3{White}]{Yellow} - like explore
{White}[{Red}4{White}]{Yellow} - comment for select account
{White}[{Red}5{White}]{Yellow} - like for select account
{White}[{Red}6{White}]{Yellow} - comment following
{White}[{Red}7{White}]{Yellow} - like following
{White}[{Red}99{White}]{Yellow} - Exit
{White}======================================
''')
c=int(input(_+' choose : '))
if c == 99:
	exit()
error,bad,good=0,0,0


username = input(_+' Your Username : ')
password = input(_+' Your Password : ')
s=int(input(_+' Seconds : '))
j=s
url = 'https://www.instagram.com/accounts/login/ajax/'
headers = {
     'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '275',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'csrftoken=DqBQgbH1p7xEAaettRA0nmApvVJTi1mR; ig_did=C3F0FA00-E82D-41C4-99E9-19345C41EEF2; mid=X8DW0gALAAEmlgpqxmIc4sSTEXE3; ig_nrcb=1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
    'x-csrftoken': 'DqBQgbH1p7xEAaettRA0nmApvVJTi1mR',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': 'bc3d5af829ea',
    'x-requested-with': 'XMLHttpRequest'
  }
data = {
         'username': f'{username}',
         'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
         'queryParams': '{}',
         'optIntoOneTap': 'false'
    } 
rs=requests.session()
r = rs.post(url, headers=headers, data=data)


if  'authenticated":true' in r.text or 'userId' in r.text:
	csrftoken=r.cookies['csrftoken']
	si=r.cookies['sessionid']
	id=r.cookies['ds_user_id']
	
	
else:
	print('[-] bad login ')
	exit()

print(f'\n\n{_} Done login ~')


print('\n= = = = = Start = = = = =\n')
k=0

if  c == 1:
	text = text = text = iter(['استغفروا' , 'صلوا على الرسول' , 'اذكرا الله' ,'اكتب شيء يشفع لك' ,'اكتب شيء تؤجر عليه'  , 'مَنْ عَمِلَ صَالِحًا مِّن ذَكَرٍ أَوْ أُنثَى وَهُوَ مُؤْمِنٌ فَلَنُحْيِيَنَّهُ حَيَاةً طَيِّبَةً وَلَنَجْزِيَنَّهُمْ أَجْرَهُم بِأَحْسَنِ مَا كَانُواْ يَعْمَلُونَ' ])
	hasanat()
elif  c == 2:
	text = input(_+' Your Comment : ')
	comment()
elif  c == 3 :
	like_ex()
elif  c ==4:
	use=input(_+' username the account : ')
	text = input(_+' Your Comment : ')
	comment_ch()
elif  c == 5:
	use=input(_+' username the account : ')
	like_ch()
elif  c ==6:
	text = input(_+' Your Comment : ')
	comment_following()	
elif  c == 7 :
	like_following()



