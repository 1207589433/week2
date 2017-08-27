from bs4 import BeautifulSoup
import requests

def get_links_from(channel,pages,who_sells=0):
    #ttp://bj.58.com/sanxing/1/pn4/
    list_view='{}{}/pn{}/'.format(channel,str(who_sells),str(pages))
    wb_data=requests.get(list_view)
    soup=BeautifulSoup(wb_data.text,'lxml')
    if soup.find('a','t'):
        for link in soup.select('table.tbimg tbody tr.zzinfo td.t a.t'):
            item_link=link.get('href').split('?')[0]
            if item_link.find('jump')>=0:
                ##存在jump出来
                pass
            else:
                print(item_link)



    else:
        pass
#get_links_from('http://bj.58.com/pbdnipad/',2)


def get_item_info(url):

    wb_data=requests.get(url)
    soup=BeautifulSoup(wb_data.text,'lxml')
    if '商品已下架' in wb_data.text:  ##如果直接判断soup.find不能 因为是一个列表 可以使用wb_data.text
        pass
    else:
        title=soup.select('h1.info_titile')[0].text  #取出列表中第一个元素的文本内容
        price=soup.select('span.price_now')[0].text
        print(price)
        print(title)
get_item_info('http://zhuanzhuan.58.com/detail/900629263558848011z.shtml')
















'''http://zhuanzhuan.58.com/detail/900629263874048011z.shtml
http://zhuanzhuan.58.com/detail/900625212958916617z.shtml
http://zhuanzhuan.58.com/detail/900195128220254220z.shtml
http://zhuanzhuan.58.com/detail/900644475154120711z.shtml
http://zhuanzhuan.58.com/detail/900595629367132167z.shtml
http://zhuanzhuan.58.com/detail/900638743969660934z.shtml
http://zhuanzhuan.58.com/detail/900585893649285133z.shtml
http://zhuanzhuan.58.com/detail/900584568195694599z.shtml
http://zhuanzhuan.58.com/detail/900670642011832327z.shtml
http://zhuanzhuan.58.com/detail/900583374052294663z.shtml
http://zhuanzhuan.58.com/detail/900623232322420749z.shtml
http://zhuanzhuan.58.com/detail/900575318636658700z.shtml
http://zhuanzhuan.58.com/detail/900572279099883533z.shtml
http://zhuanzhuan.58.com/detail/900570907427274758z.shtml
http://zhuanzhuan.58.com/detail/900615367327694857z.shtml
http://zhuanzhuan.58.com/detail/900612588965118989z.shtml
http://zhuanzhuan.58.com/detail/900606794794991625z.shtml
http://zhuanzhuan.58.com/detail/900559695967568396z.shtml
http://zhuanzhuan.58.com/detail/900559288445845510z.shtml
http://zhuanzhuan.58.com/detail/900559052574965768z.shtml
http://zhuanzhuan.58.com/detail/900555013351702540z.shtml
http://zhuanzhuan.58.com/detail/900553696722714635z.shtml
http://zhuanzhuan.58.com/detail/900552932979048455z.shtml
http://zhuanzhuan.58.com/detail/900552265944203270z.shtml
http://zhuanzhuan.58.com/detail/900641676132745223z.shtml
http://zhuanzhuan.58.com/detail/900538332025208841z.shtml
http://zhuanzhuan.58.com/detail/900583141740249097z.shtml
http://zhuanzhuan.58.com/detail/900530357783789579z.shtml
http://zhuanzhuan.58.com/detail/900577740306808845z.shtml
http://zhuanzhuan.58.com/detail/900529506302328840z.shtml
http://zhuanzhuan.58.com/detail/900521944917704712z.shtml
http://zhuanzhuan.58.com/detail/900558105153143817z.shtml
http://zhuanzhuan.58.com/detail/900557796236787724z.shtml
http://zhuanzhuan.58.com/detail/776231511568416772z.shtml
http://zhuanzhuan.58.com/detail/900541295169060873z.shtml'''