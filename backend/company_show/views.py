from django.shortcuts import render
from django.shortcuts import HttpResponse
import json
import pymysql
from django.shortcuts import redirect

# Create your views here.

host = '127.0.0.1'
port = 3306
user = 'root'
password = 'root'
database = 'ncbi'
one_page = 50


def index_page(request):
    return redirect('/AlpacaCapital-fe/index.html')


def get_company_list(request):
    page_num = request.GET.get('page', 1)
    page_num = int(page_num)

    conn = pymysql.connections.Connection(host=host, port=port, user=user, passwd=password,
                                          database=database, connect_timeout=5, charset='utf8')
    cur = conn.cursor()
    query = '''SELECT * FROM ncbi.company ORDER BY id limit {0},{1};'''.format(page_num * one_page, one_page)

    result = cur.execute(query)
    rows = cur.fetchall()
    company_raw = []
    for row in rows:
        temp_dict = dict()
        temp_dict['company_name'] = row[1]
        temp_dict['company_description'] = row[2]
        temp_dict['company_location'] = row[3]
        temp_dict['phone'] = row[4]
        temp_dict['fax'] = row[5]
        temp_dict['county'] = row[6]
        temp_dict['region'] = row[7]
        temp_dict['company_type'] = row[8]
        temp_dict['year_founded'] = row[9]
        temp_dict['employment_in_nc'] = row[10]
        temp_dict['us_headquarters'] = row[11]
        temp_dict['global_headquarters'] = row[12]
        company_raw.append(temp_dict)
    json_raw = dict()
    json_raw["data"] = company_raw

    query = '''SELECT count(*) FROM ncbi.company;'''
    cur.execute(query)
    company_num = cur.fetchall()
    json_raw["amount"] = company_num[0][0]

    json_res = json.dumps(company_raw)
    print(json_res)
    conn.commit()
    cur.close()
    return HttpResponse(json_res)
