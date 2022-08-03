import requests
url="https://ec.kamanautomation.com/category/Connectors/?N=j3f6le"

headers={
    'authority':'ec.kamanautomation.com',
    'method':'GET',
    'path':'/category/Connectors/?N=j3f6le',
    'scheme':'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control':'no-cache',
    'cookie':'deviceMode=desktop; userPrefLanguage=en_GB; JSESSIONID=5bUAj1nDoLu1PacNWFEJsDEPHIE1a4Zrr2ncjzV0.03; anonSiteHitCounter_ec=1; _gcl_au=1.1.636721838.1656067462; _ga=GA1.2.570676142.1656067475; _gid=GA1.2.1727867847.1656067479; _gat_UA-15350234-27=1; cebs=1; _ce.s=v~284b11b911c9b5b3859f6cc5b40100c058b11621~vpv~0; __qca=P0-475070655-1656067482564; utag_main=v_id:018195505e960016e7418b36fec50506f003c067009dc$_sn:1$_se:1$_ss:1$_st:1656069281239$ses_id:1656067481239%3Bexp-session$_pn:1%3Bexp-session$dc_visit:1$dc_event:1%3Bexp-session$dc_region:eu-west-1%3Bexp-session; lhnStorageType=cookie; lhnRefresh=3be43db8-9721-4f64-8b79-e8a089e02675; lhnJWT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ2aXNpdG9yIiwiZG9tYWluIjoiIiwiZXhwIjoxNjU2MTUzODg4LCJpYXQiOjE2NTYwNjc0ODgsImlzcyI6eyJhcHAiOiJqc19zZGsiLCJjbGllbnQiOjM2NjkwLCJjbGllbnRfbGV2ZWwiOiJlbnRlcnByaXNlIiwibGhueF9mZWF0dXJlcyI6W10sInZpc2l0b3JfdHJhY2tpbmciOnRydWV9LCJqdGkiOiIzYjdhMjZjNi02M2E3LTRjNTgtOTZiZi03NDI2OTExOTZhMWQiLCJyZXNvdXJjZSI6eyJpZCI6IjNiN2EyNmM2LTYzYTctNGM1OC05NmJmLTc0MjY5MTE5NmExZC0zNjY5MC1KSDJEamY1IiwidHlwZSI6IkVsaXhpci5MaG5EYi5Nb2RlbC5Db3JlLlZpc2l0b3IifX0.3Go_5OIzlYS6-fGBFWy6pDbAV9BqnZIzHO1X4SJi5iQ; lhnContact=3b7a26c6-63a7-4c58-96bf-742691196a1d-36690-JH2Djf5; KP_UIDz-ssn=0fOx0Q1M62133gjgdSYGLR2RNfjYxk9NAxrb1rNHj0CLGOyPidj5dRU77KbBxR0D7aj7N7PgG3P9BL9F3PqnOFmRlNqYwn8a94aInTfW9l3rdYlhwI1vFPTPKso7mi2LW8JxCYc8HdA5NuAs4DRAAxiuE7wC; KP_UIDz=0fOx0Q1M62133gjgdSYGLR2RNfjYxk9NAxrb1rNHj0CLGOyPidj5dRU77KbBxR0D7aj7N7PgG3P9BL9F3PqnOFmRlNqYwn8a94aInTfW9l3rdYlhwI1vFPTPKso7mi2LW8JxCYc8HdA5NuAs4DRAAxiuE7wC; _ga_ZSCJY95Y1B=GS1.1.1656067475.1.0.1656067510.0',
    'pragma':'no-cache',
    'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'document',
    'sec-fetch-mode':'navigate',
    'sec-fetch-site':'none',
    'sec-fetch-user':'?1',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
}

re=requests.get(url=url,headers=headers)
print(re.status_code)