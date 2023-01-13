import time
import requests

Download_Num = int(input("下几张:"))
Path = input("下载路径:")
for i in range(Download_Num):
    Get_Req = requests.get("https://xiaobapi.top/api/xb/api/pixiv_r18.php")
    Get_URL = Get_Req.json()['data'][0]['urls']['original']

    Format = Get_Req.json()['data'][0]['ext']
    get_File = requests.get(Get_URL)
    Now = str(int(time.time()))
    FileName = Path + Now + "." + Format
    with open(FileName, "wb") as f:
        f.write(get_File.content)
        f.close()
print("下好啦")