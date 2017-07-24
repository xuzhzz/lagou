from getPage import get_index_data, get_job_data, get_company_data
from parsePage import parse_index_data, parse_job_data, parse_company_data


if __name__ == '__main__':
    desurl = 'https://www.lagou.com/jobs/positionAjax.json?'
    data = get_index_data(desurl)
    for item in parse_index_data(data):
        job_data = get_job_data(item['positionId'])
        item['job'] = parse_job_data(job_data)
        print(item)