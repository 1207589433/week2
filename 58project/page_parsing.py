from bs4 import BeautifulSoup
import requests
import time
import pymysql
db=pymysql.connect('localhost','root','Luhang574','list',charset="utf8")
cursor=db.cursor()
sql="""CREATE TABLE IF NOT EXISTS `iteminfo` ( 
      id int unsigned key auto_increment,
      `name` text
      
    ) charset=utf8"""
cursor.execute(sql)
def get_links_from(channel,pages,who_sells=0):
    #http://bj.58.com/sanxing/1/pn4/

    list_view = '{}{}/pn{}/'.format(channel, str(who_sells), str(pages))
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if soup.find('a', 't'):
        for link in soup.select('table.tbimg tbody tr.zzinfo td.t a.t'):
            item_link = link.get('href')
            if item_link.find('jump') >= 0:
                ##存在jump出来
                pass
            else:
                cursor.execute("insert iteminfo(name) values(%s)",item_link)
                db.commit()

                print(list_view)





    else:
        pass
        #nothing!!!
def get_item_info(url):
    wb_data=requests.get(url)
    soup=BeautifulSoup(wb_data.text,'lxml')
    title = soup.select('div.box_left_top > h1')
    price = soup.select('span.price_now')

    #sql = """CREATE TABLE IF NOT EXISTS `iteminfo` (

     #     `title` text,
    #       price  text

     #   ) charset=utf8"""
    #cursor.execute(sql)
    #cursor.execute("insert iteminfo values(%s%s)",title,price )
    #db.commit()

#get_item_info('http://bj.58.com/shouji/26055261754434x.shtml')







