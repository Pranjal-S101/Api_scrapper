import requests
import xlwt
from xlwt import Workbook
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

BASE_URL='https://remoteok.com/api'
USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.2903.86'
REQUEST_HEADER={
    'User-Agent':USER_AGENT,
    'Accept-Language':'en-US, en;q=0.5'
}

def get_job_posting():
    res=requests.get(url=BASE_URL,headers=REQUEST_HEADER)
    return res.json()

def output_jobs_to_xls(data):
    wb=Workbook()
    job_sheet=wb.add_sheet('Jobs')
    headers=list(data[1].keys())
    for i in range(0, len(headers)):
        job_sheet.write(0,i,headers[i])
    for i in range(0, len(data)):
        job=data[i]
        values=list(job.values())
        for x in range(0,len(values)):
            job_sheet.write(i+1,x,values[x])
    wb.save('remote_jobs.xls')
    
    

if __name__=="__main__":
    json=get_job_posting()[1:]
    output_jobs_to_xls(json)
    