from bs4 import BeautifulSoup
import requests

start_url='http://bj.58.com/sale.shtml'

def get_channel_urls(url):
    wb_data=requests.get(url)
    soup=BeautifulSoup(wb_data.text,'lxml')
    links=soup.select('li.btno > span > a')
    for link in links:
        page_url='http://bj.58.com'+link.get('href')
        print(page_url)


#get_channel_urls(start_url)

channel_list='''

http://bj.58.com/pbdnipad/
http://bj.58.com/pbdnsanxing/
http://bj.58.com/pbdnlianxiang/
http://bj.58.com/pbdnaiguozhe/
http://bj.58.com/biguakt/
http://bj.58.com/guishikt/
http://bj.58.com/zhongyangkt/
http://bj.58.com/quanzidongxiyiji/
http://bj.58.com/guntongxiyiji/
http://bj.58.com/shuanggangxiyiji/
http://bj.58.com/minixiyiji/
http://bj.58.com/shuangkaimenbx/
http://bj.58.com/duikaimenbx/
http://bj.58.com/minibx/
http://bj.58.com/lishibg/
http://bj.58.com/wohibg/
http://bj.58.com/zhanshibg/
http://bj.58.com/danrenchuang/
http://bj.58.com/shuanrenchuang/
http://bj.58.com/chuangcengchuang/
http://bj.58.com/zhediechuang/
http://bj.58.com/tongchuang/
http://bj.58.com/chuangdian/
http://bj.58.com/guizi/
http://bj.58.com/zhuolei/
http://bj.58.com/zuoju/
http://bj.58.com/jiajushafa/
http://bj.58.com/chaji/
http://bj.58.com/jujia/
http://bj.58.com/naifen/
http://bj.58.com/weiyangfushi/
http://bj.58.com/weiyangyingyangpin/
http://bj.58.com/weiyangnaiping/
http://bj.58.com/weiyangnaizui/
http://bj.58.com/weiyangxinaiqi/
http://bj.58.com/weiyangnuannaiqi/
http://bj.58.com/yingerchuang/
http://bj.58.com/yingerche/
http://bj.58.com/tongchexuebu/
http://bj.58.com/tongcheyaoyi/
http://bj.58.com/tongzuoyi/
http://bj.58.com/tongcanyi/
http://bj.58.com/tongniuche/
http://bj.58.com/tongzixingche/
http://bj.58.com/tongsanlunche/
http://bj.58.com/yongpintaixin/
http://bj.58.com/fangfusefu/
http://bj.58.com/mmfuzhuang/
http://bj.58.com/yongpinshoufu/
http://bj.58.com/yongpinyunfuzhen/
http://bj.58.com/fushipeijian/
http://bj.58.com/fuzhuangshoushi/
http://bj.58.com/fuzhuangshoubiao/
http://bj.58.com/fuzhuangtxue/
http://bj.58.com/fuzhuangchenshan/
http://bj.58.com/fuzhuangwaitao/
http://bj.58.com/fuzhuangkuzi/
http://bj.58.com/qunzifs/
http://bj.58.com/fuzhuangxizhuang/
http://bj.58.com/tongzhuang/
http://bj.58.com/xiuxianxie/
http://bj.58.com/yundongxie/
http://bj.58.com/fanbuxie/
http://bj.58.com/gaogenxie/
http://bj.58.com/xiebanxi/
http://bj.58.com/pixie/
http://bj.58.com/xiangbaodanjian/
http://bj.58.com/xiangbaoshuangjian/
http://bj.58.com/xiangbaoshubao/
http://bj.58.com/xiangbaoqianbao/
http://bj.58.com/xiangbaolagan/
http://bj.58.com/xiangbaodiannao/
http://bj.58.com/youpiaoyoupin/
http://bj.58.com/fanggujiaju/
http://bj.58.com/aoyunjinianbi/
http://bj.58.com/sbjinianpin/
http://bj.58.com/youyongwt/
http://bj.58.com/yujiawt/
http://bj.58.com/diaoyuyongju/
http://bj.58.com/qipai/
'''


