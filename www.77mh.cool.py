# 漫画url:https://www.77mh.cool/201805/387251.html
import requests
from lxml import etree
import js2py

# js解密得到的数据
"""
    var atsvr = "gn";
    var msg = '202009/26/1027252090.jpg|202009/26/1027256471.jpg|202009/26/1027256362.jpg|202009/26/1027252743.jpg|202009/26/1027257894.jpg|202009/26/1027257665.jpg|202009/26/1027256546.jpg|202009/26/1027257727.jpg|202009/26/1027253448.jpg|202009/26/1027252929.jpg|202009/26/10272559310.jpg|202009/26/10272586411.jpg|202009/26/10272587312.jpg|202009/26/10272589313.jpg|202009/26/10272520114.jpg|202009/26/10272569515.jpg|202009/26/10272598516.jpg|202009/26/10272588417.jpg|202009/26/10272515318.jpg|202009/26/10272525519.jpg|202009/26/10272533420.jpg|202009/26/10272533521.jpg|202009/26/10272571422.jpg';
    var maxPage = 23;
    var img_s = 61;
    var preLink_b = '/202009/465933.html';
    var preName_b = '第01话';
    var nextLink_b = '/202009/465935.html';
    var nextName_b = '第03话';
    var linkname = '第02话';
    var link_z = '/colist_245770.html';
    var linkn_z = '不知我的死亡Flag将于何处停止';
"""


def get_data(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }
    html = requests.get(url, headers=header).text
    print(html)
    ee = etree.HTML(html)
    # 注意这个页面有多个text/javascript 使用下面的xpath可能匹配不到数据
    js = ee.xpath('//script[@type="text/javascript"]/text()')[0] if len(
        ee.xpath('//script[@type="text/javascript"]/text()')) > 0 else None
    return js


def parse_js(js):

    context = js2py.EvalJs()
    result = context.execute(js)  # 这时候打印result为None，不代表没有执行成功
    # print(context.msg)  # 201805/05/1941346030.jpg|201805/05/1941346141.jpg|201805/05/1941344172.jpg|201805/05/1941346823.jpg|201805/05/1941347744.jpg|201805/05/1941342585.jpg|201805/05/1941342086.jpg|201805/05/1941346067.jpg|201805/05/1941347748.jpg|201805/05/1941344309.jpg|201805/05/19413449010.jpg|201805/05/19413480911.jpg|201805/05/19413445612.jpg|201805/05/19413449713.jpg|201805/05/19413445814.jpg|201805/05/19413468515.jpg|201805/05/19413457816.jpg|201805/05/19413415617.jpg|201805/05/19413440018.jpg|201805/05/19413445419.jpg|201805/05/19413484120.jpg|201805/05/19413432621.jpg|201805/05/194134100022.jpg|201805/05/19413425023.jpg|201805/05/19413470724.jpg|201805/05/19413428525.jpg|201805/05/19413423326.jpg|201805/05/19413474327.jpg|201805/05/19413421428.jpg|201805/05/19413420329.jpg|201805/05/19413474430.jpg|201805/05/19413471831.jpg|201805/05/19413471732.jpg|201805/05/19413416133.jpg|201805/05/19413440034.jpg|201805/05/19413449135.jpg|201805/05/19413431936.jpg|201805/05/19413450937.jpg|201805/05/19413499738.jpg|201805/05/19413499439.jpg|201805/05/19413483940.jpg|201805/05/19413448741.jpg|201805/05/19413480242.jpg|201805/05/19413429443.jpg|201805/05/19413488544.jpg|201805/05/19413426045.jpg|201805/05/19413488046.jpg|201805/05/19413446347.jpg
    list_url = context.msg.split("|")
    img_s = context.img_s  # 这个拼接图片url要用
    print(list_url)
    return list_url, img_s

# 注意这个img_s,是拼接url所需要的参数
def SplicingURL(list_url, img_s):
    new_list = []
    for l in list_url:
        url = "https://a16d.gdbyhtl.net:64443/" + "h" + str(img_s) + "/" + l
        new_list.append(url)
    print(new_list)

def run():
    # 1.获取到要执行的js代码
    js = get_data("https://www.77mh.cool/201805/387251.html")
    # 2.把代码放到js2py去执行
    list_url, img_s = parse_js(js)
    # 3.拼接链接
    SplicingURL(list_url, img_s)


if __name__ == "__main__":
    run()
