import tweepy
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from datetime import  datetime
from webdriver_manager.chrome import ChromeDriverManager
import schedule
import time

def job():
    api_key = '*************************'
    api_key_secret = '****************************'
    access_token = '***************************'
    access_token_secret = '************************'

    auth = tweepy.OAuthHandler(api_key,api_key_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)
    me = api.me()

    url = 'https://www.amazon.co.jp/%E3%82%B7%E3%83%A3%E3%83%BC%E3%83%97-SHARP-SJ-AF50G-R-%E3%83%97%E3%83%A9%E3%82%BA%E3%83%9E%E3%82%AF%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC-%E3%82%B0%E3%83%A9%E3%83%87%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%AC%E3%83%83%E3%83%89/dp/B08KJ85RJ5?ref_=fspcr_pl_dp_2_2272928051'

    driver = Chrome(ChromeDriverManager().install())
    driver.get(url)
    time.sleep(2)

    now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    if len(driver.find_elements_by_id('add-to-cart-button')) > 0:
        api.update_status(f'{now}現在、在庫があります。')
    else:
        api.update_status(f'{now}現在、在庫がありません。')

    driver.quit()

def main():
    schedule.every(3).hour.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()

