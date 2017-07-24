import json
from bs4 import BeautifulSoup
def parse_index_data(data):
    items = json.loads(data).get('content').get('positionResult').get('result')
    for item in items:
        yield {
            'positionId': item.get('positionId'),
            'positionName': item.get('positionName'),
            'companyId': item.get('companyId'),
            'companyFullName': item.get('companyFullName'),
            'companyLable': item.get('companyLabelList'),
            'positionLable': item.get('positionLables'),
            'time': item.get('createTime'),
            'education': item.get('education'),
            'industryField': item.get('industryField'),
            'salary': item.get('salary'),
            'workYear': item.get('workYear')
        }

def parse_job_data(data):
    d = BeautifulSoup(data, "lxml")
    desc = d.find('dd', {'class': 'job_bt'}).get_text()
    addr_ = d.find('div', {'class': 'work_addr'}).get_text()
    return (desc, addr_)

def parse_company_data(data):
    pass