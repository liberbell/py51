import requests
from httpx import get
from selectolax.parser import HTMLParser

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
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

def image_filter_out(url: str, keywords: list) -> bool:
    return not any(x in url for x in keywords)

def get_high_res_img_url(img_node):
    secret = img_node.attrs=["secret"]

if __name__ == "__main__":
    image_nodes = get_img_tags_for('galaxy')

    # image_urls = []
    # for image_node in image_nodes:
    #     image_urls.append(image_node.attrs["src"])

    #     # for image_url in image_urls:
    #     #     print(image_url)

    # relevent_urls = [i for i in image_urls if image_filter_out(i, ['plus', 'premium', 'profile'])]
    # for relevent_url in relevent_urls:
    #     print(relevent_url)