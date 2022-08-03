import requests
import browsercookie

header={
    'authority': 'www.amazon.com',
    'method': 'GET',
    'path': '/',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'cookie': 'aws-target-data=%7B%22support%22%3A%221%22%7D; aws-target-visitor-id=1653637237469-622692.31_0; AMCV_7742037254C95E840A4C98A6%40AdobeOrg=1585540135%7CMCIDTS%7C19140%7CMCMID%7C64178720641047390243744145601411548273%7CMCAAMLH-1654242037%7C12%7CMCAAMB-1654242037%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1653644437s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; aws-ubid-main=250-2620454-1356188; regStatus=registered; session-id=138-9049328-0959404; session-id-time=2082787201l; i18n-prefs=USD; skin=noskin; ubid-main=130-2328817-4720548; session-token=vPSECc6JY7Yov7bbjx1LwcmSeCoDgNuakUJeQzpQxUWF/QQUuLKcVGJEPODJTEY10oosZPRp2it/u1Q9iFe81+jtjOro8oIaIXjEOPyQa/pivf3PjItaSyXrBqaQ56iNdrIeBuXTFqUHihEfzBgwXsCDDEhsMDw4aIdnRH5jbccdWz3rMoC/tD87FK3M54SHYcyN+b3pkSLocV33qZg/zaoA7vikSdxZPrxaHHM49qsYLKNfAQe1wRWJTTyR1xgJ; csm-hit=tb:s-XJF2WHD8Q2FVHY4TEGP9|1655982448157&t:1655982449391&adb:adblk_yes',
    'device-memory': '8',
    'downlink': '10',
    'dpr': '1',
    'ect': '4g',
    'pragma': 'no-cache',
    'rtt': '50',
    'sec-ch-device-memory': '8',
    'sec-ch-dpr': '1',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-viewport-width': '1600',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'viewport-width':'1600',
}

cj = browsercookie.chrome()
print(cj)
url='https://www.amazon.com/'
r = requests.get(url=url, headers=header)

print(r.status_code)