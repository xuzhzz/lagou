import requests
from config import keyword, city

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Referer':'https://www.lagou.com/jobs/list_{kd}?px=new&city={ct}'.format(kd=keyword.encode('utf-8'), ct=city.encode('utf-8')),
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'user_trace_token=20170309145408-4dbe240c1f8449939f858f2f4a2d5420; LGUID=20170309145411-333eaefc-0495-11e7-922e-5254005c3644; X_HTTP_TOKEN=5e923c157572273b9588e2ddb27787a9; TG-TRACK-CODE=search_code; login=true; unick=%E8%AE%B8%E5%AD%90%E6%B6%B5; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=35; index_location_city=%E5%B9%BF%E5%B7%9E; JSESSIONID=ABAAABAACBHABBI99225C04C25581BB1FA752224A1DB04A; _gat=1; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E7%2588%25AC%25E8%2599%25AB%3Fpx%3Ddefault%26city%3D%25E5%25B9%25BF%25E5%25B7%259E; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E7%2588%25AC%25E8%2599%25AB%3Fpx%3Dnew%26city%3D%25E5%25B9%25BF%25E5%25B7%259E; _ga=GA1.2.1241989892.1489042452; _gid=GA1.2.1205416879.1500799100; LGSID=20170724225325-d8626a68-707f-11e7-b13f-525400f775ce; LGRID=20170724225330-db90185f-707f-11e7-b5d2-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1500626107,1500799100; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1500908011; _putrc=4BFD1BD87E3A6460; SEARCH_ID=42b31a11d6c841ec9e685c72f2122c26',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest',
}

headers2 = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Referer':'https://www.lagou.com',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'user_trace_token=20170309145408-4dbe240c1f8449939f858f2f4a2d5420; LGUID=20170309145411-333eaefc-0495-11e7-922e-5254005c3644; X_HTTP_TOKEN=5e923c157572273b9588e2ddb27787a9; TG-TRACK-CODE=search_code; login=true; unick=%E8%AE%B8%E5%AD%90%E6%B6%B5; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=35; index_location_city=%E5%B9%BF%E5%B7%9E; JSESSIONID=ABAAABAACBHABBI99225C04C25581BB1FA752224A1DB04A; _gat=1; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E7%2588%25AC%25E8%2599%25AB%3Fpx%3Ddefault%26city%3D%25E5%25B9%25BF%25E5%25B7%259E; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E7%2588%25AC%25E8%2599%25AB%3Fpx%3Dnew%26city%3D%25E5%25B9%25BF%25E5%25B7%259E; _ga=GA1.2.1241989892.1489042452; _gid=GA1.2.1205416879.1500799100; LGSID=20170724225325-d8626a68-707f-11e7-b13f-525400f775ce; LGRID=20170724225330-db90185f-707f-11e7-b5d2-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1500626107,1500799100; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1500908011; _putrc=4BFD1BD87E3A6460; SEARCH_ID=42b31a11d6c841ec9e685c72f2122c26',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest',
}

params = {
    'px': 'new',
    'city': city,
    'needAddtionalResult': 'false'
}


def get_index_data(url, page=1):
    data = {
        'first': 'true',
        'pn': str(page),
        'kd': keyword,
    }
    try:
        response = requests.post(url=url, params=params, headers=headers, data=data)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        print('connection error!')


def get_job_data(id):
    try:
        response = requests.post('https://www.lagou.com/jobs/{id}.html'.format(id=id), headers=headers2)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        print('connection error!')

def get_company_data(id):
    try:
        response = requests.post('https://www.lagou.com/gongsi/{id}.html'.format(id=id), headers=headers2)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        print('connection error!')
