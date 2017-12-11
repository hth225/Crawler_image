import Crawling

if __name__ == '__main__':
    url = "https://www.google.co.kr/search?q=galaxy+note+8&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjn18Dk7YHYAhWEi5QKHfQFAJAQ_AUICigB&biw=1440&bih=826#imgrc=OMI3cJHvIXa-KM:"
    Crawling.download_image(str(url))
