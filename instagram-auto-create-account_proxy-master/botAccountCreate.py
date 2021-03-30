from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import accountInfoGenerator as account
import getVerifCode as verifiCode
from selenium import webdriver
import fakeMail as email
import time
import argparse
import pandas as pd
from selenium.webdriver.common.proxy import Proxy, ProxyType
from numpy import random
from time import sleep
import random
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
import requests
import json

# from pandas import ExcelWriter
# from pandas import ExcelFile
# from pandas import DataFrame
# from openpyxl import Workbook


api_key = 'fe5e06bc8ba3b0d4d5c7222b8b8e7a71'
site_key = '6Lc9qjcUAAAAADTnJq5kJMjN9aD1lxpRLMnCS2TR'  # grab from site
captcha_url = 'https://www.fbsbx.com/captcha/recaptcha/iframe/?compact=0&referer=https%3A%2F%2Fwww.instagram.com&locale=en_US&__cci=ig_captcha_iframe'


def create_proxyauth_extension(proxy_host, proxy_port, proxy_username, proxy_password, scheme='http', plugin_path=None):
    import string
    import zipfile

    if plugin_path is None:
        plugin_path = 'proxy.zip'

    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = string.Template("""
    var config = {
            mode: "fixed_servers",
            rules: {
              singleProxy: {
                scheme: "${scheme}",
                host: "${host}",
                port: parseInt(${port})
              },
              bypassList: ["foobar.com"]
            }
          };
    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
    function callbackFn(details) {
        return {
            authCredentials: {
                username: "${username}",
                password: "${password}"
            }
        };
    }
    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """
                                    ).substitute(
        host=proxy_host,
        port=proxy_port,
        username=proxy_username,
        password=proxy_password,
        scheme=scheme,
    )
    with zipfile.ZipFile(plugin_path, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)

    return plugin_path


list_user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0']
i = 1

for i in range(1, 5):
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--firefox", action="store_true", help="Use Firefox - geckodriver")
    group.add_argument("--chrome", action="store_true", help = "Use Chrome - chromedriver")

    args = parser.parse_args()

    ua = UserAgent()
    userAgent = ua.random
    userAgent = random.choice(list_user_agents)
    print(userAgent)

    if args.firefox:
        with open('proxy.txt','r') as file:
            countriesStr = file.read()
        PROXY_HOST = countriesStr.split(":")[0]
        PROXY_PORT = countriesStr.split(":")[1]
        profile = webdriver.FirefoxProfile()
        profile.set_preference("intl.accept_languages", "en-US")
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http",PROXY_HOST)
        print(PROXY_HOST)
        profile.set_preference("network.proxy.http_port",int(PROXY_PORT))
        print(int(PROXY_PORT))
        profile.set_preference("general.useragent.ovrride", userAgent)
        profile.update_preferences()
        try:
            driver = webdriver.Firefox(firefox_profile=profile, executable_path=r"/Users/sbeuran/Desktop/Desktop/web/geckodriver.exe")
        except:
            driver = webdriver.Firefox(firefox_profile=profile, executable_path=r"geckodriver.exe")


    if args.chrome:
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_argument("--lang=en")
        options.add_argument(f'user-agent={userAgent}')
        proxyauth_plugin_path = create_proxyauth_extension(
            proxy_host='gw.proxy.rainproxy.io',
            proxy_port=5959,
            proxy_username="getrixone-cc-us",
            proxy_password="790IdcnU"
        )
        options.add_extension(proxyauth_plugin_path)
        try:
            driver = webdriver.Chrome(options=options, executable_path=r"/Users/sbeuran/Desktop/Desktop/web/chromedriver")
        except:
            driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")

    driver.get("https://www.instagram.com/accounts/emailsignup/")
    time.sleep(8)
    name = account.username()
    #//button[text()='Accept']
    try:
        driver.find_element_by_xpath("//button[text()='Accept']").click()
    except:
        pass

    #Fill the email value
    email_field = driver.find_element_by_name('emailOrPhone')
    fake_email = email.getFakeMail()
    email_field.send_keys(fake_email)
    print(fake_email)

    # Fill the fullname value
    fullname_field = driver.find_element_by_name('fullName')
    fullname_field.send_keys(account.generatingName())
    print(account.generatingName())
    # Fill username value
    username_field = driver.find_element_by_name('username')
    username_field.send_keys(name)
    print(name)
    # Fill password value
    password_field = driver.find_element_by_name('password')
    password_field.send_keys(account.generatePassword())  # You can determine another password here.
    paw = account.generatePassword()
    print(account.generatePassword())
    time.sleep(8)

    driver.find_elements_by_class_name('L3NKy')[1].click()
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']"))).click()

    time.sleep(8)

    #Birthday verification
    driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select").click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[4]"))).click()

    driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select").click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[10]"))).click()

    driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select").click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[27]"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[6]/button"))).click()
    time.sleep(3)
    #
    fMail = fake_email[0].split("@")
    mailName = fMail[0]
    domain = fMail[1]
    instCode = verifiCode.getInstVeriCode(mailName, domain, driver)
    old_url = driver.current_url
    driver.find_element_by_name('email_confirmation_code').send_keys(instCode, Keys.ENTER)
    time.sleep(8)
    curr = driver.current_url
    while curr == old_url:
        time.sleep(2)
        curr = driver.current_url
    if 'challenge' in curr:
        cookies_list = driver.get_cookies()
        cookies_dict = {}
        for cookie in cookies_list:
            cookies_dict[cookie['name']] = cookie['value']
        url_now = driver.current_url
        client = AnticaptchaClient(api_key)
        task = NoCaptchaTaskProxylessTask(captcha_url, site_key)
        job = client.createTask(task)
        job.join()
        g_token = job.get_solution_response()
        headers = {
            'authority': 'www.instagram.com',
            'x-ig-www-claim': '0',
            'x-instagram-ajax': '753ce878cd6d',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
            'x-requested-with': 'XMLHttpRequest',
            'x-csrftoken': cookies_dict['csrftoken'],
            'x-ig-app-id': '936619743392459',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': url_now,
            'accept-language': 'en-US,en;q=0.9',
            'cookie': 'csrftoken={}; mid={}; ig_did={}; ig_nrcb={}'.format(cookies_dict['csrftoken'], cookies_dict['mid'], cookies_dict['ig_did'], cookies_dict['ig_nrcb']),
        }
        data = {
          'g-recaptcha-response': g_token
        }
        requests.post(url_now, headers=headers, data=data)
        time.sleep(2)
        driver.get(url_now)
    driver.get("https://www.instagram.com/growthfxtrading/")
    sleeptime = random.uniform(2, 4)
    print("sleeping for:", sleeptime, "seconds")
    sleep(sleeptime)
    print("sleeping is over")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Follow']"))).click()
    


    with open("test.txt", "a") as myfile:
        myfile.write(str(fake_email)+"\n")
        myfile.write(str(name)+"\n")
        myfile.write(str(name)+"\n")
        myfile.write("--------------------------------------------------  \n")
