import hashlib
import html
import math
import re
import requests
from scrapy.selector import Selector
from mymodules._common_ import c_replace
import json
import scrapy
from ugam_cdiscount.config import *
from ugam_cdiscount.items import *
from ugam_cdiscount.pipelines import *
import time
from ugam_cdiscount.config import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


he_html={
    'authority': 'www.cdiscount.com',
    'method': 'GET',
    # 'path': '/search/10/276e8vjsb.html',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'cookie': 'tcId=a0ca3b3c-b4af-4dd4-bacb-976b77736962; s_ecid=MCMID%7C23306473208207058996697567794876773304; app_vi=34214400%7C; AMCV_6A63EE6A54FA13E60A4C98A7%40AdobeOrg=1585540135%7CMCIDTS%7C19180%7CMCMID%7C23306473208207058996697567794876773304%7CMCAID%7CNONE%7CMCOPTOUT-1657090964s%7CNONE%7CvVersion%7C4.4.0; CookieId=CookieId=220706070255IVXQCPFV&IsA=0; TC_AB=B; TCPID=1227310325810632012344; UniqueVisitContext=UniqueVisitId__220706070259XCOBKNDS__; SitePersoCookie=PersoCountryKey____PersoLatitudeKey____PersoLongitudeKey____PersoTownKey____GeolocPriorityKey__0__PersoPostalCodeKey____PersoUrlGeoSCKey____ExpressSellerId____ExpressShopName____ExpressGlobalSellerId____ShowroomVendorId____RetailStoreName____VehicleId__0__AddressId____; _cs_c=3; TC_PRIVACY=0@016%7C2%7C2%7C150@4%2C1%2C5%2C3%2C2%2C6%2C10001%2C10003%2C10005%2C10007%2C10013%2C10015%2C10017%2C10019%2C10009%2C10011%2C13002%2C13001%2C10004%2C10014%2C10016%2C10018%2C10020%2C10010%2C10008%2C10012%2C10006@@1657083812374%2C1657083812374%2C1672635812374@_u_PvZ8a-F4BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACe-Pn_ge_v-Zvnmf-fB75_6v-D79hm6D-en4FvaOCZ8b-b_z_mmn_m5ocAHh7gB5h6gHkOvucfgOhgYPj_mOf_Ye4BiP_RmwMYfh6KgPn5fmaGZuYDYGJ4GPgHhmE-np-nABgGGACewhiooGH4iYGhmWF4HpBnYGAYmTlmGBro44AmgqAp4GCGDgKeYQKGeh6GgWEYgnseeBh_moeKOQAogO-b4H_o_wiIATp7KABmePin--mH76-uq4-_X_gpEO579-jv9_j__-fh_9nhnr_77pH9vfvpvxqebr373qHq7_c75n9gAQ%3D%3D; TC_PRIVACY_CENTER=4%2C1%2C5%2C3%2C2%2C6%2C10001%2C10003%2C10005%2C10007%2C10013%2C10015%2C10017%2C10019%2C10009%2C10011%2C13002%2C13001%2C10004%2C10014%2C10016%2C10018%2C10020%2C10010%2C10008%2C10012%2C10006; tc_sample_335_562=0; _$1okcook=1; tcIdNe=2963384a-9a2e-486c-b7f4-76f95887f946; _gcl_au=1.1.237251301.1657083817; _scid=82290a26-4297-4c90-992d-5d334ab5d4ae; __gsas=ID=b26d08d7095b14c4:T=1657083819:S=ALNI_MZmeAYcP96kTDER5gvsUrDLwH6Dbg; mics_lts=1657083822073; mics_vid=27918825074; _sctr=1|1657045800000; SiteVersionCookieNoChanges=1370.1|1418.1|1423.1|1426.1|1433.1|1441.1|1458.1|1464.0|1466.1|1467.1|1469.1|1475.1|1482.1|1484.1|1488.1|1491.1|5005.1|5008.0|5015.1|5016.1|5019.1|5021.0|5023.1; __gads=ID=4e72e106a83131d3:T=1657092313:S=ALNI_MbKgIOzfgZSKaXP_3yZLYLHzZq_7w; _fbp=fb.1.1657092318265.415251108; prio7j=prio3; chcook7=ref; prio30j=prio3; mssctse=W2dNXeEyrPIjeOJ6paI359XUqdFmwLX0IPTditUolnOjwxi_H1d5XgWp8rmqKfagu3WEvbk5H-3zOZXcawRbqw; _$dtype=t:d; cache_cdn=; svisit=1; _$3custinf=AUT=0; _$3ci=; rxVisitor=1657166866291I44T95VBNROBAQOH4KN1BBTFB8BQRUSO; cs_heure_session=9; s_sq=%5B%5BB%5D%5D; s_cc=true; _$cst=1; dtCookie=v_4_srv_12_sn_4638E4503635D00AFED12278981E63CD_app-3Ac93cbedcccfc6fbb_0_ol_0_perc_100000_mul_1; _clck=1c51u66|1|f2y|0; _cs_cvars=%7B%228%22%3A%5B%22h_deb_session%22%2C%229%22%5D%7D; msswt=; __gpi=UID=00000769af5b6517:T=1657092313:RT=1657166923:S=ALNI_Masg1rkBEtAEtAQYXbybUcp6wYL5w; SiteVersionCookie=1547.1|1548.0|2038.1|2041.1|2524.1|3027.0|3032.1|3033.1|3040.0|4012.1|4018.1|4019.1|4026.1|4028.1|4033.0|4037.0|4302.1|4305.1|4308.1|4513.0|4514.0|4515.1|4516.1|4517.1|4521.0|4525.1|5010.1|5011.1|5012.0|5013.1; s_pv=Recherche; ABTasty=uid=ym5hezxj23t22apt&fst=1657083816562&pst=1657097934503&cst=1657166870837&ns=4&pvt=113&pvis=17&th=695989.863466.87.86.2.1.1657083817639.1657113844124.1_710841.882596.1.1.1.1.1657098356687.1657098356687.1_723627.899155.1.1.1.1.1657166871614.1657166871614.1_851040.0.112.17.4.1.1657083817641.1657167807461.1_856343.1065502.7.7.1.1.1657095520642.1657107624046.1_856622.1065855.112.17.4.1.1657083817642.1657167807464.1_863731.1075056.108.91.3.1.1657083816753.1657167807690.1_864039.1075410.108.91.3.1.1657083816763.1657167807700.1; _uetsid=fe4aab00fce811ec98887fd0eac75d36; _uetvid=fe4b0c50fce811ec87f46fec61c45c13; challenge=JmNaL4p84LHEfek6eFD6LfB3VuoA6C26wqU0quhENwTehv8YuBbrOWGhuAmyPgq8zDCQDIez1AcJoa5ySEyQyoVZmtTrRSUMmkzSIU4DeOY8IzRMQ2UrfQTSDkGizK_NhwvTjoB5z0EYIGbRZoY-2v5hDmq-LMYWvDTWPERaC_RQ1ICteHS9ABS7vJU7SD6D5A2QZm44gK9VEiOYXaCSYk3to-yTuLa5rUJyQ6rQg34; _cs_id=9ec0b146-e3c5-af43-9c03-77cf5f58a0b1.1657083781.6.1657167812.1657166885.1590586488.1691247781204; _cs_s=14.0.0.1657169612294; _clsk=15z6j55|1657167812338|17|0|b.clarity.ms/collect; _MFB_=fHwxNHx8fFtdfHx8NTIuNDI5MTAwOTgyNDIyNzV8; cto_bundle=aMGSkF9reVdyZWhnZVdVV2h3RFY2bCUyQjdEa2FqbUVsdEFyRjR3Z0tSVkdOeUI5QWFVSlFud1NDcmM2R3BUNzYwek5XQnRIelBGdktIZk9Nc2VFUzBaazQwQ1JRZm5GTzU5UDFDT0trTkl4dFU0VENjdXklMkIyRVlhMFBsckg0YUR2Vm16aHZ5TSUyQkxJdThweVowdXc1aURlOU9YZGclM0QlM0Q; VisitContextCookie=ipxOG--c2fPP9V5AJ5yoCM7p62T_d2P3xzHCC6lwlMiAZfJZln2HRA; dtLatC=1; el2=0; tp=4180; s_ppv=Recherche%2C21%2C19%2C889; ABTastySession=mrasn=&sen=113&lp=https%253A%252F%252Fwww.cdiscount.com%252F; s_nr=1657168012339-Repeat; rxvt=1657169812609|1657166866295; dtPC=12$567803237_662h73vPOHPKRHKQCRRPLAHETFARIPJJFKEKCKO-0',
    'pragma': 'no-cache',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

headers={
    'authority': 'www.cdiscount.com',
    'method': 'POST',
    'path': '/ProductListUC.mvc/UpdateJsonPage?page=2',
    'scheme': 'https',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-length': '474',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'tcId=a0ca3b3c-b4af-4dd4-bacb-976b77736962; s_ecid=MCMID%7C23306473208207058996697567794876773304; app_vi=34214400%7C; AMCV_6A63EE6A54FA13E60A4C98A7%40AdobeOrg=1585540135%7CMCIDTS%7C19180%7CMCMID%7C23306473208207058996697567794876773304%7CMCAID%7CNONE%7CMCOPTOUT-1657090964s%7CNONE%7CvVersion%7C4.4.0; CookieId=CookieId=220706070255IVXQCPFV&IsA=0; TC_AB=B; TCPID=1227310325810632012344; UniqueVisitContext=UniqueVisitId__220706070259XCOBKNDS__; SitePersoCookie=PersoCountryKey____PersoLatitudeKey____PersoLongitudeKey____PersoTownKey____GeolocPriorityKey__0__PersoPostalCodeKey____PersoUrlGeoSCKey____ExpressSellerId____ExpressShopName____ExpressGlobalSellerId____ShowroomVendorId____RetailStoreName____VehicleId__0__AddressId____; _cs_c=3; TC_PRIVACY=0@016%7C2%7C2%7C150@4%2C1%2C5%2C3%2C2%2C6%2C10001%2C10003%2C10005%2C10007%2C10013%2C10015%2C10017%2C10019%2C10009%2C10011%2C13002%2C13001%2C10004%2C10014%2C10016%2C10018%2C10020%2C10010%2C10008%2C10012%2C10006@@1657083812374%2C1657083812374%2C1672635812374@_u_PvZ8a-F4BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACe-Pn_ge_v-Zvnmf-fB75_6v-D79hm6D-en4FvaOCZ8b-b_z_mmn_m5ocAHh7gB5h6gHkOvucfgOhgYPj_mOf_Ye4BiP_RmwMYfh6KgPn5fmaGZuYDYGJ4GPgHhmE-np-nABgGGACewhiooGH4iYGhmWF4HpBnYGAYmTlmGBro44AmgqAp4GCGDgKeYQKGeh6GgWEYgnseeBh_moeKOQAogO-b4H_o_wiIATp7KABmePin--mH76-uq4-_X_gpEO579-jv9_j__-fh_9nhnr_77pH9vfvpvxqebr373qHq7_c75n9gAQ%3D%3D; TC_PRIVACY_CENTER=4%2C1%2C5%2C3%2C2%2C6%2C10001%2C10003%2C10005%2C10007%2C10013%2C10015%2C10017%2C10019%2C10009%2C10011%2C13002%2C13001%2C10004%2C10014%2C10016%2C10018%2C10020%2C10010%2C10008%2C10012%2C10006; tc_sample_335_562=0; _$1okcook=1; tcIdNe=2963384a-9a2e-486c-b7f4-76f95887f946; _gcl_au=1.1.237251301.1657083817; _scid=82290a26-4297-4c90-992d-5d334ab5d4ae; __gsas=ID=b26d08d7095b14c4:T=1657083819:S=ALNI_MZmeAYcP96kTDER5gvsUrDLwH6Dbg; mics_lts=1657083822073; mics_vid=27918825074; _sctr=1|1657045800000; SiteVersionCookieNoChanges=1370.1|1418.1|1423.1|1426.1|1433.1|1441.1|1458.1|1464.0|1466.1|1467.1|1469.1|1475.1|1482.1|1484.1|1488.1|1491.1|5005.1|5008.0|5015.1|5016.1|5019.1|5021.0|5023.1; __gads=ID=4e72e106a83131d3:T=1657092313:S=ALNI_MbKgIOzfgZSKaXP_3yZLYLHzZq_7w; _fbp=fb.1.1657092318265.415251108; chcook7=ref; prio7j=prio3; prio30j=prio3; mssctse=W2dNXeEyrPIjeOJ6paI359XUqdFmwLX0IPTditUolnOjwxi_H1d5XgWp8rmqKfagu3WEvbk5H-3zOZXcawRbqw; _$dtype=t:d; cache_cdn=; svisit=1; _$3custinf=AUT=0; _$3ci=; rxVisitor=1657166866291I44T95VBNROBAQOH4KN1BBTFB8BQRUSO; cs_heure_session=9; s_sq=%5B%5BB%5D%5D; s_cc=true; _$cst=1; dtCookie=v_4_srv_12_sn_4638E4503635D00AFED12278981E63CD_app-3Ac93cbedcccfc6fbb_0_ol_0_perc_100000_mul_1; _clck=1c51u66|1|f2y|0; _cs_cvars=%7B%228%22%3A%5B%22h_deb_session%22%2C%229%22%5D%7D; msswt=; __gpi=UID=00000769af5b6517:T=1657092313:RT=1657166923:S=ALNI_Masg1rkBEtAEtAQYXbybUcp6wYL5w; SiteVersionCookie=1547.1|1548.0|2038.1|2041.1|2524.1|3027.0|3032.1|3033.1|3040.0|4012.1|4018.1|4019.1|4026.1|4028.1|4033.0|4037.0|4302.1|4305.1|4308.1|4513.0|4514.0|4515.1|4516.1|4517.1|4521.0|4525.1|5010.1|5011.1|5012.0|5013.1; s_pv=Recherche; ABTasty=uid=ym5hezxj23t22apt&fst=1657083816562&pst=1657097934503&cst=1657166870837&ns=4&pvt=113&pvis=17&th=695989.863466.87.86.2.1.1657083817639.1657113844124.1_710841.882596.1.1.1.1.1657098356687.1657098356687.1_723627.899155.1.1.1.1.1657166871614.1657166871614.1_851040.0.112.17.4.1.1657083817641.1657167807461.1_856343.1065502.7.7.1.1.1657095520642.1657107624046.1_856622.1065855.112.17.4.1.1657083817642.1657167807464.1_863731.1075056.108.91.3.1.1657083816753.1657167807690.1_864039.1075410.108.91.3.1.1657083816763.1657167807700.1; _uetsid=fe4aab00fce811ec98887fd0eac75d36; _uetvid=fe4b0c50fce811ec87f46fec61c45c13; challenge=JmNaL4p84LHEfek6eFD6LfB3VuoA6C26wqU0quhENwTehv8YuBbrOWGhuAmyPgq8zDCQDIez1AcJoa5ySEyQyoVZmtTrRSUMmkzSIU4DeOY8IzRMQ2UrfQTSDkGizK_NhwvTjoB5z0EYIGbRZoY-2v5hDmq-LMYWvDTWPERaC_RQ1ICteHS9ABS7vJU7SD6D5A2QZm44gK9VEiOYXaCSYk3to-yTuLa5rUJyQ6rQg34; _cs_id=9ec0b146-e3c5-af43-9c03-77cf5f58a0b1.1657083781.6.1657167812.1657166885.1590586488.1691247781204; _cs_s=14.0.0.1657169612294; _clsk=15z6j55|1657167812338|17|0|b.clarity.ms/collect; _MFB_=fHwxNHx8fFtdfHx8NTIuNDI5MTAwOTgyNDIyNzV8; cto_bundle=aMGSkF9reVdyZWhnZVdVV2h3RFY2bCUyQjdEa2FqbUVsdEFyRjR3Z0tSVkdOeUI5QWFVSlFud1NDcmM2R3BUNzYwek5XQnRIelBGdktIZk9Nc2VFUzBaazQwQ1JRZm5GTzU5UDFDT0trTkl4dFU0VENjdXklMkIyRVlhMFBsckg0YUR2Vm16aHZ5TSUyQkxJdThweVowdXc1aURlOU9YZGclM0QlM0Q; dtLatC=1; el2=0; tp=4180; s_ppv=Recherche%2C21%2C19%2C889; ABTastySession=mrasn=&sen=113&lp=https%253A%252F%252Fwww.cdiscount.com%252F; s_nr=1657168012339-Repeat; rxvt=1657169812609|1657166866295; dtPC=12$567803237_662h-vPOHPKRHKQCRRPLAHETFARIPJJFKEKCKO-0; VisitContextCookie=ipxOG--c2fP4W7-k-NKBy1B7b2cMbKImuoZUDgxB6exKhHTuDtpFXA',
    'origin': 'https://www.cdiscount.com',
    'pragma': 'no-cache',
    'referer': 'https://www.cdiscount.com/search/10/24m.html',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

class CategorySpider(scrapy.Spider):

    name = 'ugam_cdiscount'
    handle_httpstatus_list = [404]
    F_PATH = HTML

    def __init__(self, start='', end=''):
        try:
            self.cursor = UgamCdiscountPipeline.cursor
            self.con = UgamCdiscountPipeline.con
            self.start = start
            self.end = end
        except Exception as e:
            print('exception in _init_ method main:{}'.format(e))

    def start_requests(self):
        try:
            brand_select = f"select Id,Model_No from {db_category_table} where Status = 'Pending' AND ID BETWEEN {self.start} AND {self.end}"

            self.cursor.execute(brand_select)
            category_list = [column for column in self.cursor.fetchall()]

            for cat_item in category_list:

                cat_row_id = cat_item[0]
                cat_mpn = cat_item[1]

                """ -----delete duplicate data in link data table with brand id----- """
                delete_duplicate_row = f"delete from {db_data_table} where cat_id like {cat_row_id}"
                self.cursor.execute(delete_duplicate_row)
                self.con.commit()

                page_no = 1
                meta_dict = {
                    'row_id': cat_row_id,
                    'page_no': page_no,
                    'counter': 0,
                    'cat_mpn':cat_mpn
                }

                category_url=f"https://www.cdiscount.com/search/10/{cat_mpn}.html"
                print(category_url)

                filename = f'/cat_{cat_row_id}_page_{page_no}.html'
                path = self.F_PATH + filename
                path = path.replace("\\", "/")
                url3="https://www.cdiscount.com/ProductListUC.mvc/UpdateJsonPage?page=2"


                he_html = {
                    'authority': 'www.cdiscount.com',
                    'method': 'GET',
                    'path': f'/search/10/{cat_mpn}.html',
                    'scheme': 'https',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                    'cache-control': 'no-cache',
                    'cookie': 'cs_heure_session=13; dtCookie=v_4_srv_11_sn_33E797486C76147740C98B2E8684ADE6_perc_100000_ol_0_mul_1_app-3Ac93cbedcccfc6fbb_0; mssctse=W2dNXeEyrPLuCKbPRebXBQpBlG-57sfpH-HftLdJqJKcq6ztE-T1KPIFZp16HK-xaCLVRzgo0QDPMf2oUnntzA; CookieId=CookieId=220707085448CHDHXOIS&IsA=0; _$dtype=t:d; TC_AB=B; TCPID=122741224481373121395; _$3custinf=AUT=0; s_ecid=MCMID%7C90142719171348737430810711503318569131; app_vi=34214400%7C; s_cc=true; AMCV_6A63EE6A54FA13E60A4C98A7%40AdobeOrg=1585540135%7CMCIDTS%7C19181%7CMCMID%7C90142719171348737430810711503318569131%7CMCAID%7CNONE%7CMCOPTOUT-1657184089s%7CNONE%7CvVersion%7C4.4.0; AMCVS_6A63EE6A54FA13E60A4C98A7%40AdobeOrg=1; UniqueVisitContext=UniqueVisitId__220707085450QDGVXVDW__; _cs_c=3; tcId=8973823e-1aa7-404e-9f7a-5a91a3f36229; msswt=; svisit=1; cache_cdn=; rxVisitor=16571822475382TJ5JGGNFPMSR0N3P3445VLD9F4HSLO1; dtLatC=11; rxvt=1657184051279|1657182247545; dtPC=11$582247532_665h-vLJAPRKLDLBFCUQGUCVRIPCWKOVEDRWAC-0; TC_CPT=4; el2=0; _cs_cvars=%7B%228%22%3A%5B%22h_deb_session%22%2C%2213%22%5D%7D; TC_PRIVACY=0@016%7C2%7C2%7C150@4%2C1%2C5%2C3%2C2%2C6%2C10001%2C10003%2C10005%2C10007%2C10013%2C10015%2C10017%2C10019%2C10009%2C10011%2C13002%2C13001%2C10004%2C10014%2C10016%2C10018%2C10020%2C10010%2C10008%2C10012%2C10006@@1657182266264%2C1657182266264%2C1672734266264@_u_PvZ8a-F4BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACe-Pn_ge_v-Zvnmf-fB75_6v-D79hm6D-en4FvaOCZ8b-b_z_mmn_m5ocAHh7gB5h6gHkOvucfgOhgYPj_mOf_Ye4BiP_RmwMYfh6KgPn5fmaGZuYDYGJ4GPgHhmE-np-nABgGGACewhiooGH4iYGhmWF4HpBnYGAYmTlmGBro44AmgqAp4GCGDgKeYQKGeh6GgWEYgnseeBh_moeKOQAogO-b4H_o_wiIATp7KABmePin--mH76-uq4-_X_gpEO579-jv9_j__-fh_9nhnr_77pH9vfvpvxqebr373qHq7_c75n9gAQ%3D%3D; TC_PRIVACY_CENTER=4%2C1%2C5%2C3%2C2%2C6%2C10001%2C10003%2C10005%2C10007%2C10013%2C10015%2C10017%2C10019%2C10009%2C10011%2C13002%2C13001%2C10004%2C10014%2C10016%2C10018%2C10020%2C10010%2C10008%2C10012%2C10006; tcIdNe=832960a8-4d64-43dc-8d7d-87dcb47da622; tc_sample_335_562=0; _$1okcook=1; _$cst=1; _gcl_au=1.1.2015130301.1657182267; fpg=1; _scid=6f4558de-5c08-4823-84dc-68f108a1768c; __gsas=ID=181e30c16b87da52:T=1657182270:S=ALNI_MY5ycmgpgXiE9WOPjILqWxaZZMIwQ; _sctr=1|1657132200000; _clck=h21xay|1|f2y|0; mics_vid=27956300211; mics_lts=1657182271990; SiteVersionCookie=1547.1|1548.0|2038.1|2041.1|2524.1|3027.0|3032.1|3033.1|3040.0|4012.1|4018.1|4019.1|4026.1|4028.1|4033.0|4037.1|4302.1|4305.1|4308.1|4513.0|4514.0|4515.1|4516.1|4517.1|4521.0|4525.1|5010.1|5011.1|5012.1|5013.0; SiteVersionCookieNoChanges=1370.1|1418.1|1423.1|1426.1|1433.1|1441.1|1458.1|1464.0|1466.1|1467.1|1469.1|1475.1|1482.1|1484.1|1488.1|1491.1|5005.0|5008.0|5015.1|5016.1|5019.1|5021.1|5023.1; _$3ci=; _fbp=fb.1.1657182296967.1474215795; captcha=XjY0d3Fm9hKJVhNn81NfqHDWLQTVIYSV6NkXWrDblO2acbo3w6ShhoL39QueLRagfYwMURbhoFcrLIQzUdtoIojgO19dRLX3bocIuuIlKmDTQAeGBmZBAYnf1AGXxtaTTkZU4g3SFWebe4yi74t_tROegvYtfNxGXQK8nYvOKKVqQt7IWqPV3pny7HT4Z1hTTmS1Cz04n2qFW9gm_38mWK9e9LlaXzfpjzLcjgL3GSfiUdtKikddNiWA4kUZ5qdo; _uetsid=37d3e420fdce11eca30aab7ed2cad26b; _uetvid=37d42a70fdce11ecb57643e7d5ba6d1e; challenge=JmNaL4p84LHEfek6eFD6LSZpCPILaFhPLZfmikj40ly29zDbJKeERnyBE-63xh1mfpOus02jC1Ib4F43uUaBN6NHcmPDmZFmoQRzXjvbKquaJhJTNWZYOkFar17-bObkWVVuI2FqljQYDTI7HlYsAVq6e3z6YTWSb4GxFisdP1eEyNE_ENIAxFuG-cnXi8Et75SoE-jW8xN6xAJuqV6Y4lB_Eagy81I2RnVwqQZmP_tky3lu_n4MJqC-tUrAa7MD; ABTasty=uid=cb50vz0brsa246w7&fst=1657182267628&pst=-1&cst=1657182267628&ns=1&pvt=3&pvis=3&th=851040.0.3.3.1.1.1657182267673.1657182468090.1_856622.0.3.3.1.1.1657182267676.1657182468094.1_863731.1075056.3.3.1.1.1657182268648.1657182468313.1_864039.1075410.3.3.1.1.1657182268669.1657182468326.1; ABTastySession=mrasn=&sen=17&lp=https%253A%252F%252Fwww.cdiscount.com%252Fsearch%252F10%252Fgb2770hsu.html%2523_his_; s_pv=Recherche; s_nr=1657182469228-Repeat; tp=5894; s_ppv=Recherche%2C13%2C13%2C789; __gads=ID=9605383d50484335:T=1657182472:S=ALNI_Maan39F-BSWjkv0Ke7y-nh24o2IvQ; __gpi=UID=00000770d087f261:T=1657182472:RT=1657182472:S=ALNI_MYftXHIM4ILLpJdQ5v-BDuv8xYJ5w; _clsk=1ur212v|1657182476083|3|0|h.clarity.ms/collect; VisitContextCookie=gbLaCtTCGPcTyhlOYool4Btc0krOSvaoeP9ws1vVILt6dESI6MxOwg; _cs_id=0a5ecf51-e3c5-ac92-deb5-efff07e145f0.1657176890.2.1657182480.1657182230.1590586488.1691340890350; _cs_s=4.5.0.1657184280468; cto_bundle=j0Ys7F9zRDJvWm4wTGQ3JTJCUDV1SFAzJTJGNlJFMXhYeU8lMkZlYnpwNEhueSUyQkJCQzgwVDBHVjZTJTJGNlE1dHFKTEtkNVpKQ0lWdSUyRldnb1N6N0RhU3hLUG51RFpCNjdwdzU5WUVwYUxOUUtLMkl5cng4dXB4ZW1SWENQandhUXJra3dCWVRVdHN1VG9VJTJGQXdOSEpuSmxVZ2k0NTFSZ29WQSUzRCUzRA; _MFB_=fHwzfHx8W118fHwzOS40MTE5NjUyNTc3OTgxMXw=',
                    'pragma': 'no-cache',
                    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
                }

                if os.path.exists(path):
                    pass
                else:
                    re = requests.get(url=category_url, headers=he_html)
                    print(re.text)
                    if re.status_code != 200 or re.status_code == 200 and "Achat sur Internet a prix discount de DVD et de produits culturels" in re.text:
                        from lxml import html
                        dd = webdriver.ChromeOptions()
                        dd = webdriver.Chrome(ChromeDriverManager().install())
                        dd.get(category_url)
                        dd.maximize_window()
                        time.sleep(2)
                        try:
                            dd.find_element_by_xpath('//button[@id="footer_tc_privacy_button_2"]').click()
                        except Exception as e:
                            print("Aceept Not IN page")

                        time.sleep(2)
                        cookie = ''
                        try:
                            d = dd.get_cookies()
                            for c in d:
                                cookie += '{name}={value}; '.format(
                                    name=c['name'],
                                    value=c['value']
                                )

                            he_html = {
                                'authority': 'www.cdiscount.com',
                                'method': 'GET',
                                'path': f'/search/10/{cat_mpn}.html',
                                'scheme': 'https',
                                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                                'cache-control': 'no-cache',
                                'cookie': cookie,
                                'pragma': 'no-cache',
                                'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"',
                                'sec-fetch-dest': 'document',
                                'sec-fetch-mode': 'navigate',
                                'sec-fetch-site': 'none',
                                'sec-fetch-user': '?1',
                                'upgrade-insecure-requests': '1',
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
                            }
                            re = requests.get(url=category_url, headers=he_html)
                            print(re.text)

                            if re.status_code==200 and "Achat sur Internet a prix discount de DVD et de produits culturels" not in re.text:
                                with open(path, 'w', encoding='utf-8')as f:
                                    f.write(re.text)
                            else:
                                print("AGAIN WROMG RESPONSE")

                        except Exception as e:
                            print(e)

                    if "Achat sur Internet a prix discount de DVD et de produits culturels" in re.text:
                        print("--- Wrong Response Please Re Try -----")
                    else:
                        if os.path.exists(path):
                            pass
                        else:
                            with open(path,'w',encoding='utf-8')as f:
                                f.write(re.text)

                if os.path.exists(path):
                    yield scrapy.FormRequest(url=f'file:///{path}', callback=self.parse,dont_filter=True,
                                             meta={'meta_dict': meta_dict})
        except Exception as e:
            print('exception in start requests method main: {}'.format(e))

    def parse(self, response, **kwargs):
        pass
        print("response",response.status)

        # print(response.text)
        #
        # meta_dict = response.meta.get('meta_dict')
        # row_id=meta_dict.get('row_id')
        # page_no=meta_dict.get('page_no')
        # counter=meta_dict.get('counter')
        #
        # try:
        #     if "</html>" in response.text:
        #         filename = f'/cat_url{row_id}_Page_{page_no}.html'
        #         path = self.F_PATH + filename.replace("\\", "/")
        #
        #         if not os.path.exists(path):
        #             with open(path, 'wb') as f:
        #                 f.write(response.body)
        #
        #         catpdp.Htmlpath=c_replace(path)
        #         catpdp.id1=c_replace(row_id)
        #
        #         for li in response.xpath('//div[@class="jsPrdBlocContainer"]'):
        #             counter += 1
        #             product_url=li.xpath('').get()
        #
        # except Exception as e:
        #     print("Error in parse main try :{}".format(e))
        #     import sys
        #
        #     print("parse method main error: {}".format(e))
        #     exception_type, exception_object, exception_traceback = sys.exc_info()
        #     filename = exception_traceback.tb_frame.f_code.co_filename
        #     line_number = exception_traceback.tb_lineno
        #     print('line---:{}'.format(sys.exc_info()))
        #     print("Exception type: {}".format(exception_type))
        #     print("File name: {}".format(filename))
        #     print("Error is:{} ".format(e))
        #     print("Line number: {}".format(line_number))

if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute('scrapy crawl ugam_cdiscount -a start=1 -a end=250'.split())