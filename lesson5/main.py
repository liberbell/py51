import requests
from httpx import get
from selectolax.parser import HTMLParser

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    # "accept-language": "ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
    # "accept-encoding": "gzip, deflate, br, zstd",
    "content-type": "application/json"
}

def get_img_tags_for(term=None):
    url = f"https://unsplash.com/s/photos/{term}"
    resp = get(url, headers=headers)
    
    if resp.status_code != 200:
        raise Exception("Error getting response")
    
    tree = HTMLParser(resp.text)
    # imgs = tree.css("figure a img + div img")
    imgs = tree.css("div div a img")
    # //*[@id="«R5iqp6m»"]/div/div/div[2]/figure[1]/div[1]/div/a/img
    return imgs

if __name__ == "__main__":
    image_nodes = get_img_tags_for('galaxy')
    print(len(image_nodes))
    print(image_nodes)