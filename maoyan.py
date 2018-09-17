# _*_ encoding=utf8 _*_
import requests,re,json
headers = {

            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'

        }
response = requests.get("http://maoyan.com/board/4",headers=headers)




def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?title=.*?"(.*?)"'+'.*?star">(.*?)</p>.*?releasetime">(.*?)</p>' + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',
                         re.S)

    items =re.findall(pattern,html)

    print(items)

    for item in items:
        yield {
            "index":item[0],
            "image":item[1],
            "title":item[2].strip(),
            "actor":item[3].strip(),
            "time":item[4].strip(),
            "score":item[5].strip()
        }

def write_to_file(content):
    with open("maoyan.txt","a",encoding="utf-8") as f:
        f.write(json.dumps(content,ensure_ascii=False)+"\n")


def main(offset):
    url = "http://maoyan.com/board/4?offset=" + str(offset)
    html = response.text
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__=="__main__":
    for i in range(10):
        main(offset=i*10)
