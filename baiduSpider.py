import requests


# 获取百度搜索结果
def getBaiduMessage(keyWord,pageNumber):
    # 请求头，模拟浏览器请求
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',}
    # get  .text获取网页源代码
    res = requests.get('https://www.baidu.com/s?wd={}&pn={}'.format(keyWord,pageNumber),headers = headers).text
    # 替换百度图标
    return res.replace('//www.baidu.com/img/baidu_jgylogo3.gif','static/images/search.png')

# if __name__ == '__main__':
#     print(getBaiduMessage('python',0))