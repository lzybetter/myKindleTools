#代码取自https://www.jianshu.com/p/8f66fadaf844


header_str='''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
Cache-Control: max-age=0
Connection: keep-alive
Cookie: _vwo_uuid_v2=DA3DAF51A5873D18F413EC953A60D0B14|59cda40608aeb3e971f3aa8b6a32b521; douban-fav-remind=1; __gads=ID=62693d2c96c0daf9:T=1563749125:S=ALNI_MboPyvJD85MTWzvptvHUURTuC_wvg; gr_user_id=4ce14567-f0e1-4294-82f0-5998169f95fc; UM_distinctid=17081cf0c591bc-0c48c5bfc380ef-317e0a5e-1fa400-17081cf0c5ae37; bid=05yE4xkoHx0; ll="108296"; __utmz=30149280.1598225837.30.29.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); viewed="3729518_4915989_4199363_4141733_27093745_27125397_26912214_26825082_1031551_3715623"; __utmz=81379588.1598226120.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); CNZZDATA1256793290=2034367399-1598220679-https%253A%252F%252Fwww.douban.com%252F%7C1598226079; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=1e6723e7-b3f8-4f85-a0bb-928cd3947ca8; gr_cs1_1e6723e7-b3f8-4f85-a0bb-928cd3947ca8=user_id%3A0; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1598441590%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fcat%3D1001%26q%3D%25E4%25B9%259D%25E4%25BA%25BA%25E9%25A3%258E%25E4%25BA%2591%22%5D; _pk_id.100001.3ac3=00245973aff85684.1598225891.2.1598441590.1598226120.; _pk_ses.100001.3ac3=*; __utma=30149280.1020757966.1558712092.1598225837.1598441590.31; __utmc=30149280; __utmt_douban=1; __utma=81379588.1899842199.1598225891.1598226120.1598441590.3; __utmc=81379588; __utmt=1; __utmb=81379588.1.10.1598441590; __utmt_t1=1; __utmb=30149280.4.8.1598441590; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_1e6723e7-b3f8-4f85-a0bb-928cd3947ca8=true; RT=s=1598441593170&r=https%3A%2F%2Fbook.douban.com%2F
DNT: 1
Host: book.douban.com
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36
'''

#字符串转dict
def str2dict(s,s1=';',s2='='):
    li=s.split(s1)
    res={}
    for kv in li:
        li2=kv.split(s2)
        if len(li2)>1:
            li2[0]=li2[0].replace(':','')
            res[li2[0]]=li2[1]
    return res

def getHeader():
    headers=str2dict(header_str,'\n',': ')
    if 'Content-Length' in headers:del headers['Content-Length']
    return headers