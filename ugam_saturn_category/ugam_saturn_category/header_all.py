import requests

# HEADER1

header1={
    'authority':'www.saturn.de',
    'method':'GET',
    'path':'/api/v1/graphql?operationName=CategoryV4&variables=%7B%22hasMarketplace%22%3Atrue%2C%22maxNumberOfAds%22%3A2%2C%22isRequestSponsoredSearch%22%3Atrue%2C%22isDemonstrationModelAvailabilityActive%22%3Afalse%2C%22withMarketingInfos%22%3Afalse%2C%22filters%22%3A%5B%5D%2C%22pimCode%22%3A%22CAT_DE_SAT_2582%22%2C%22page%22%3A1%2C%22experiment%22%3A%22mp%22%2C%22sessionId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22customerId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22pageType%22%3A%22Category%22%2C%22productFilters%22%3A%5B%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22e32ccad3bd5aa0781a4e27cf31af311d7936e6513719045adc070371710afa4c%22%7D%2C%22pwa%22%3A%7B%22salesLine%22%3A%22Saturn%22%2C%22country%22%3A%22DE%22%2C%22language%22%3A%22de%22%2C%22ccr%22%3Atrue%7D%7D',
    'scheme':'https',
    'accept':'*/*',
    'accept-language':'en-GB,en-US;q=0.9,en;q=0.8',
    'apollographql-client-name':'pwa-client',
    'apollographql-client-version':'1.79.0',
    'cache-control':'no-cache',
    'content-type':'application/json',
    'cookie':'optid=0e26086e-b797-4ce7-b30a-c51085ddc0a7; pwaconsent=v:1.0~required:1&clf:1,cli:1,gfb:1,gtm:1,jot:1,ocx:1|comfort:1&baz:1,cne:1,fix:1,gfa:1,gfc:1,goa:1,gom:1,grc:1,grv:1,lob:1,opt:1,orc:1,ore:1,prd:1,sen:1,sis:1,spe:1,sst:1,swo:1,twi:1,usw:1,usz:1,yte:1|marketing:1&asm:1,cad:1,cma:1,eam:1,fab:1,fbn:1,gad:1,gam:1,gcm:1,gdv:1,gos:1,gse:1,gst:1,kru:1,msb:1,omp:1,pin:1,ttd:1,twt:1|; _gcl_au=1.1.2080703172.1654864663; NoCookie=true; _pin_unauth=dWlkPU5ERXhaVE5pWTJZdFpEaGtPQzAwTURVM0xXRTFZemt0WWpSalpXTTNZVEUyTW1SbQ; cf_clearance=SA_u608X7uLRJs_vMu6xpDUPoner9KWCF01LAfoUiEY-1655299743-0-1-3b6693ae.23026482.6c67cc4e-150; _gid=GA1.2.1270608410.1655882585; a=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im8yc2lnbiJ9.eyJzdWIiOiJlZmYxNGY0NC1iZmYzLTRiMDMtOTY1Mi02YjUzMTMwYjA5YWEiLCJpc3MiOiJtbXNlIiwiaWF0IjoxNjU1OTY2OTYyLCJleHAiOjE2NTcxNzY1NjIsImF1ZCI6IndlYm1vYmlsZSIsInQiOiJ1IiwibyI6MTAxNX0.AL8qpjEkEiEuo20P67EsysB2oTrr_bOCNmw8hKz-I127-11AO3R4G2vcThwQsLjDmlI3HNW3dLuH1bcAxFGX_ybV2ZaTeUxd31HVgW89eKGXDkHEda8xU-lT8iADo6vrbErd6UN8RtyLDk3uhr_7KsWkVngyhbcLGFRtrs12dzuyH6Cdrl4oEbnql1-171nbKlJPexazt5Ea0j-XOnPYaTLfnpSufyb81zZMwKSNYxJPtPoFDz5YrWD84gV9ixfZIQ3lE4ICsn8CLY7_JlhjTOfnR5UbSFQ139EI7oH1APhWw1RY-U9l-VyoVUp3wS6CCiy-uh3neW2kB7jV0C3cTQ; r=SNNEXcEnxhvmK5iUOgWI73bkZ7RdPm6DnIEAxl9L66oRUN9l26wXWK0VWUQBAEam; BVBRANDID=d6ed1941-5d54-4cc5-b733-73b53a05572a; __cf_bm=JCwwYLe0KnUk6LKOXMYNJubKY3Ip3zjJ7HGCYjb.euk-1656047477-0-AcOWd+6O+b40dTIEfqfVJEAsZf8NMFKaLDhGLjR5F0Lr1jyiktDMsPt3tUS41+CMbqOb4ZoCaLSBtG6ZCSGNQfTP0kffe4pW0hvLh70ZHIJO; ts_id=3eae2cf6-d91d-4a19-a703-3d03c82578a1; t_fpd=true; s_id=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; MC_PS_SESSION_ID=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; p_id=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; MC_PS_USER_ID=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; __cfruid=5ce9277937f35b0509ea571d823a42e90d1feb4c-1656047481; lux_uid=165604748329125097; _ga=GA1.2.69ecb800-76e8-4ca4-864b-aaae21efda0b; _dc_gtm_UA-25101917-1=1; _uetsid=28915a40f1fc11eca7afb9eecc1c579a; _uetvid=24005d80e8ba11ec98bccb532996a8b6; _clck=1vw2yro|1|f2l|0; _clsk=11av6ee|1656047486683|1|1|h.clarity.ms/collect; _ga_9ZJL7DLSGD=GS1.1.1656047483.31.0.1656047513.30; _msbps=98',
    'pragma':'no-cache',
    'referer':'https://www.saturn.de/de/category/gaming-notebooks-2582.html',
    'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-cacheable':'true',
    'x-flow-id':'82bd3151-9517-4d84-8589-80941a0f7a6b',
    'x-mms-country':'DE',
    'x-mms-language':'de',
    'x-mms-salesline':'Saturn',
    'x-operation':'CategoryV4',
   }


# HEADER2

header2={
    'authority':'www.saturn.de',
    'method':'GET',
    'path':'/api/v1/graphql?operationName=CategoryV4&variables=%7B%22hasMarketplace%22%3Atrue%2C%22maxNumberOfAds%22%3A2%2C%22isRequestSponsoredSearch%22%3Atrue%2C%22isDemonstrationModelAvailabilityActive%22%3Afalse%2C%22withMarketingInfos%22%3Afalse%2C%22filters%22%3A%5B%5D%2C%22pimCode%22%3A%22CAT_DE_SAT_5197%22%2C%22page%22%3A1%2C%22experiment%22%3A%22mp%22%2C%22sessionId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22customerId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22pageType%22%3A%22Category%22%2C%22productFilters%22%3A%5B%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22e32ccad3bd5aa0781a4e27cf31af311d7936e6513719045adc070371710afa4c%22%7D%2C%22pwa%22%3A%7B%22salesLine%22%3A%22Saturn%22%2C%22country%22%3A%22DE%22%2C%22language%22%3A%22de%22%2C%22ccr%22%3Atrue%7D%7D',
    'scheme':'https',
    'accept':'*/*',
    'accept-language':'en-GB,en-US;q=0.9,en;q=0.8',
    'apollographql-client-name':'pwa-client',
    'apollographql-client-version':'1.79.0',
    'cache-control':'no-cache',
    'content-type':'application/json',
    'cookie':'optid=0e26086e-b797-4ce7-b30a-c51085ddc0a7; pwaconsent=v:1.0~required:1&clf:1,cli:1,gfb:1,gtm:1,jot:1,ocx:1|comfort:1&baz:1,cne:1,fix:1,gfa:1,gfc:1,goa:1,gom:1,grc:1,grv:1,lob:1,opt:1,orc:1,ore:1,prd:1,sen:1,sis:1,spe:1,sst:1,swo:1,twi:1,usw:1,usz:1,yte:1|marketing:1&asm:1,cad:1,cma:1,eam:1,fab:1,fbn:1,gad:1,gam:1,gcm:1,gdv:1,gos:1,gse:1,gst:1,kru:1,msb:1,omp:1,pin:1,ttd:1,twt:1|; _gcl_au=1.1.2080703172.1654864663; NoCookie=true; _pin_unauth=dWlkPU5ERXhaVE5pWTJZdFpEaGtPQzAwTURVM0xXRTFZemt0WWpSalpXTTNZVEUyTW1SbQ; cf_clearance=SA_u608X7uLRJs_vMu6xpDUPoner9KWCF01LAfoUiEY-1655299743-0-1-3b6693ae.23026482.6c67cc4e-150; _gid=GA1.2.1270608410.1655882585; a=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im8yc2lnbiJ9.eyJzdWIiOiJlZmYxNGY0NC1iZmYzLTRiMDMtOTY1Mi02YjUzMTMwYjA5YWEiLCJpc3MiOiJtbXNlIiwiaWF0IjoxNjU1OTY2OTYyLCJleHAiOjE2NTcxNzY1NjIsImF1ZCI6IndlYm1vYmlsZSIsInQiOiJ1IiwibyI6MTAxNX0.AL8qpjEkEiEuo20P67EsysB2oTrr_bOCNmw8hKz-I127-11AO3R4G2vcThwQsLjDmlI3HNW3dLuH1bcAxFGX_ybV2ZaTeUxd31HVgW89eKGXDkHEda8xU-lT8iADo6vrbErd6UN8RtyLDk3uhr_7KsWkVngyhbcLGFRtrs12dzuyH6Cdrl4oEbnql1-171nbKlJPexazt5Ea0j-XOnPYaTLfnpSufyb81zZMwKSNYxJPtPoFDz5YrWD84gV9ixfZIQ3lE4ICsn8CLY7_JlhjTOfnR5UbSFQ139EI7oH1APhWw1RY-U9l-VyoVUp3wS6CCiy-uh3neW2kB7jV0C3cTQ; r=SNNEXcEnxhvmK5iUOgWI73bkZ7RdPm6DnIEAxl9L66oRUN9l26wXWK0VWUQBAEam; BVBRANDID=d6ed1941-5d54-4cc5-b733-73b53a05572a; ts_id=3eae2cf6-d91d-4a19-a703-3d03c82578a1; t_fpd=true; s_id=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; MC_PS_SESSION_ID=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; p_id=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; MC_PS_USER_ID=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; __cfruid=5ce9277937f35b0509ea571d823a42e90d1feb4c-1656047481; lux_uid=165604748329125097; _clck=1vw2yro|1|f2l|0; _msbps=97; _ga=GA1.1.69ecb800-76e8-4ca4-864b-aaae21efda0b; _uetsid=28915a40f1fc11eca7afb9eecc1c579a; _uetvid=24005d80e8ba11ec98bccb532996a8b6; __cf_bm=ovzwKNsIM5n_wLhiCZCFpM3UtRjCa0EuMqnwdfomWGs-1656049282-0-AU3hWw6cFWhrHR/Vc2tfTg0sb+BVtVhHYXHO3th02J8dUtechz2ZVXZqnvzT/nUjQxjAZeR39f9gqGnRpjTHZtLJ+CClbhEEcV5D9uvuki14; _clsk=11av6ee|1656049330388|11|1|h.clarity.ms/collect; _ga_9ZJL7DLSGD=GS1.1.1656047483.31.1.1656049359.60',
    'pragma':'no-cache',
    'referer':'https://www.saturn.de/de/category/gaming-pcs-5197.html',
    'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-cacheable':'true',
    'x-flow-id':'faab86a4-5031-4040-9632-4a686758f6fe',
    'x-mms-country':'DE',
    'x-mms-language':'de',
    'x-mms-salesline':'Saturn',
    'x-operation':'CategoryV4',
    }


# HEADER3

header3={
    'authority':'www.saturn.de',
    'method':'GET',
    'path':'/api/v1/graphql?operationName=SearchV4&variables=%7B%22hasMarketplace%22%3Atrue%2C%22isRequestSponsoredSearch%22%3Atrue%2C%22maxNumberOfAds%22%3A2%2C%22isDemonstrationModelAvailabilityActive%22%3Afalse%2C%22withMarketingInfos%22%3Afalse%2C%22categoryIds%22%3A%22CAT_DE_SAT_1%22%2C%22experiment%22%3A%22mp%22%2C%22filters%22%3A%5B%22brand%3AAPPLE%22%5D%2C%22page%22%3A1%2C%22query%22%3A%22Mac%22%2C%22sessionId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22customerId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22pageType%22%3A%22Search%22%2C%22productFilters%22%3A%5B%5B%22brand%3AAPPLE%22%5D%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%223cb930f1763026b9a724d9867a77c7085731d1c4193806a9752db52bf44e3482%22%7D%2C%22pwa%22%3A%7B%22salesLine%22%3A%22Saturn%22%2C%22country%22%3A%22DE%22%2C%22language%22%3A%22de%22%2C%22ccr%22%3Atrue%7D%7D',
    'scheme':'https',
    'accept':'*/*',
    'accept-language':'en-GB,en-US;q=0.9,en;q=0.8',
    'apollographql-client-name':'pwa-client',
    'apollographql-client-version':'1.79.0',
    'cache-control':'no-cache',
    'content-type':'application/json',
    'cookie':'optid=0e26086e-b797-4ce7-b30a-c51085ddc0a7; pwaconsent=v:1.0~required:1&clf:1,cli:1,gfb:1,gtm:1,jot:1,ocx:1|comfort:1&baz:1,cne:1,fix:1,gfa:1,gfc:1,goa:1,gom:1,grc:1,grv:1,lob:1,opt:1,orc:1,ore:1,prd:1,sen:1,sis:1,spe:1,sst:1,swo:1,twi:1,usw:1,usz:1,yte:1|marketing:1&asm:1,cad:1,cma:1,eam:1,fab:1,fbn:1,gad:1,gam:1,gcm:1,gdv:1,gos:1,gse:1,gst:1,kru:1,msb:1,omp:1,pin:1,ttd:1,twt:1|; _gcl_au=1.1.2080703172.1654864663; NoCookie=true; _pin_unauth=dWlkPU5ERXhaVE5pWTJZdFpEaGtPQzAwTURVM0xXRTFZemt0WWpSalpXTTNZVEUyTW1SbQ; cf_clearance=SA_u608X7uLRJs_vMu6xpDUPoner9KWCF01LAfoUiEY-1655299743-0-1-3b6693ae.23026482.6c67cc4e-150; _gid=GA1.2.1270608410.1655882585; a=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im8yc2lnbiJ9.eyJzdWIiOiJlZmYxNGY0NC1iZmYzLTRiMDMtOTY1Mi02YjUzMTMwYjA5YWEiLCJpc3MiOiJtbXNlIiwiaWF0IjoxNjU1OTY2OTYyLCJleHAiOjE2NTcxNzY1NjIsImF1ZCI6IndlYm1vYmlsZSIsInQiOiJ1IiwibyI6MTAxNX0.AL8qpjEkEiEuo20P67EsysB2oTrr_bOCNmw8hKz-I127-11AO3R4G2vcThwQsLjDmlI3HNW3dLuH1bcAxFGX_ybV2ZaTeUxd31HVgW89eKGXDkHEda8xU-lT8iADo6vrbErd6UN8RtyLDk3uhr_7KsWkVngyhbcLGFRtrs12dzuyH6Cdrl4oEbnql1-171nbKlJPexazt5Ea0j-XOnPYaTLfnpSufyb81zZMwKSNYxJPtPoFDz5YrWD84gV9ixfZIQ3lE4ICsn8CLY7_JlhjTOfnR5UbSFQ139EI7oH1APhWw1RY-U9l-VyoVUp3wS6CCiy-uh3neW2kB7jV0C3cTQ; r=SNNEXcEnxhvmK5iUOgWI73bkZ7RdPm6DnIEAxl9L66oRUN9l26wXWK0VWUQBAEam; BVBRANDID=d6ed1941-5d54-4cc5-b733-73b53a05572a; ts_id=3eae2cf6-d91d-4a19-a703-3d03c82578a1; t_fpd=true; s_id=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; MC_PS_SESSION_ID=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; p_id=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; MC_PS_USER_ID=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; __cfruid=5ce9277937f35b0509ea571d823a42e90d1feb4c-1656047481; lux_uid=165604748329125097; _clck=1vw2yro|1|f2l|0; _msbps=97; __cf_bm=ovzwKNsIM5n_wLhiCZCFpM3UtRjCa0EuMqnwdfomWGs-1656049282-0-AU3hWw6cFWhrHR/Vc2tfTg0sb+BVtVhHYXHO3th02J8dUtechz2ZVXZqnvzT/nUjQxjAZeR39f9gqGnRpjTHZtLJ+CClbhEEcV5D9uvuki14; _ga=GA1.2.69ecb800-76e8-4ca4-864b-aaae21efda0b; _uetsid=28915a40f1fc11eca7afb9eecc1c579a; _uetvid=24005d80e8ba11ec98bccb532996a8b6; _clsk=11av6ee|1656049637110|13|1|h.clarity.ms/collect; _dc_gtm_UA-25101917-1=1; _ga_9ZJL7DLSGD=GS1.1.1656047483.31.1.1656049658.60',
    'pragma':'no-cache',
    'referer':'https://www.saturn.de/de/brand/apple/mac',
    'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-cacheable':'true',
    'x-flow-id':'5162ab59-4c92-4bf5-ae31-b67eed6efe4d',
    'x-mms-country':'DE',
    'x-mms-language':'de',
    'x-mms-salesline':'Saturn',
    'x-operation':'SearchV4',
}


# HEADER4

header4={
    'authority':'www.saturn.de',
    'method':'GET',
    'path': '/api/v1/graphql?operationName=SearchV4&variables=%7B%22hasMarketplace%22%3Atrue%2C%22isRequestSponsoredSearch%22%3Atrue%2C%22maxNumberOfAds%22%3A2%2C%22isDemonstrationModelAvailabilityActive%22%3Afalse%2C%22withMarketingInfos%22%3Afalse%2C%22categoryIds%22%3A%22CAT_DE_SAT_66%22%2C%22experiment%22%3A%22mp%22%2C%22filters%22%3A%5B%22brand%3AAPPLE%22%5D%2C%22page%22%3A1%2C%22query%22%3A%22MacBook%2BPro%20-maus%22%2C%22sessionId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22customerId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22pageType%22%3A%22Search%22%2C%22productFilters%22%3A%5B%5B%22brand%3AAPPLE%22%5D%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%223cb930f1763026b9a724d9867a77c7085731d1c4193806a9752db52bf44e3482%22%7D%2C%22pwa%22%3A%7B%22salesLine%22%3A%22Saturn%22%2C%22country%22%3A%22DE%22%2C%22language%22%3A%22de%22%2C%22ccr%22%3Atrue%7D%7D',
    'scheme':'https',
    'accept':'*/*',
    'accept-language':'en-GB,en-US;q=0.9,en;q=0.8',
    'apollographql-client-name':'pwa-client',
    'apollographql-client-version':'1.79.0',
    'cache-control':'no-cache',
    'content-type':'application/json',
    'cookie':'optid=0e26086e-b797-4ce7-b30a-c51085ddc0a7; pwaconsent=v:1.0~required:1&clf:1,cli:1,gfb:1,gtm:1,jot:1,ocx:1|comfort:1&baz:1,cne:1,fix:1,gfa:1,gfc:1,goa:1,gom:1,grc:1,grv:1,lob:1,opt:1,orc:1,ore:1,prd:1,sen:1,sis:1,spe:1,sst:1,swo:1,twi:1,usw:1,usz:1,yte:1|marketing:1&asm:1,cad:1,cma:1,eam:1,fab:1,fbn:1,gad:1,gam:1,gcm:1,gdv:1,gos:1,gse:1,gst:1,kru:1,msb:1,omp:1,pin:1,ttd:1,twt:1|; _gcl_au=1.1.2080703172.1654864663; NoCookie=true; _pin_unauth=dWlkPU5ERXhaVE5pWTJZdFpEaGtPQzAwTURVM0xXRTFZemt0WWpSalpXTTNZVEUyTW1SbQ; cf_clearance=SA_u608X7uLRJs_vMu6xpDUPoner9KWCF01LAfoUiEY-1655299743-0-1-3b6693ae.23026482.6c67cc4e-150; _gid=GA1.2.1270608410.1655882585; a=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im8yc2lnbiJ9.eyJzdWIiOiJlZmYxNGY0NC1iZmYzLTRiMDMtOTY1Mi02YjUzMTMwYjA5YWEiLCJpc3MiOiJtbXNlIiwiaWF0IjoxNjU1OTY2OTYyLCJleHAiOjE2NTcxNzY1NjIsImF1ZCI6IndlYm1vYmlsZSIsInQiOiJ1IiwibyI6MTAxNX0.AL8qpjEkEiEuo20P67EsysB2oTrr_bOCNmw8hKz-I127-11AO3R4G2vcThwQsLjDmlI3HNW3dLuH1bcAxFGX_ybV2ZaTeUxd31HVgW89eKGXDkHEda8xU-lT8iADo6vrbErd6UN8RtyLDk3uhr_7KsWkVngyhbcLGFRtrs12dzuyH6Cdrl4oEbnql1-171nbKlJPexazt5Ea0j-XOnPYaTLfnpSufyb81zZMwKSNYxJPtPoFDz5YrWD84gV9ixfZIQ3lE4ICsn8CLY7_JlhjTOfnR5UbSFQ139EI7oH1APhWw1RY-U9l-VyoVUp3wS6CCiy-uh3neW2kB7jV0C3cTQ; r=SNNEXcEnxhvmK5iUOgWI73bkZ7RdPm6DnIEAxl9L66oRUN9l26wXWK0VWUQBAEam; BVBRANDID=d6ed1941-5d54-4cc5-b733-73b53a05572a; ts_id=3eae2cf6-d91d-4a19-a703-3d03c82578a1; t_fpd=true; s_id=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; MC_PS_SESSION_ID=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; p_id=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; MC_PS_USER_ID=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; __cfruid=5ce9277937f35b0509ea571d823a42e90d1feb4c-1656047481; lux_uid=165604748329125097; _clck=1vw2yro|1|f2l|0; __cf_bm=ovzwKNsIM5n_wLhiCZCFpM3UtRjCa0EuMqnwdfomWGs-1656049282-0-AU3hWw6cFWhrHR/Vc2tfTg0sb+BVtVhHYXHO3th02J8dUtechz2ZVXZqnvzT/nUjQxjAZeR39f9gqGnRpjTHZtLJ+CClbhEEcV5D9uvuki14; _ga=GA1.2.69ecb800-76e8-4ca4-864b-aaae21efda0b; _uetsid=28915a40f1fc11eca7afb9eecc1c579a; _uetvid=24005d80e8ba11ec98bccb532996a8b6; _clsk=11av6ee|1656049696384|15|1|h.clarity.ms/collect; _ga_9ZJL7DLSGD=GS1.1.1656047483.31.1.1656049718.60; _msbps=99',
    'pragma':'no-cache',
    'referer':'https://www.saturn.de/de/brand/apple/mac/macbook-pro',
    'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-cacheable':'true',
    'x-flow-id':'e72a3964-c53e-4479-9b78-b550e7050558',
    'x-mms-country':'DE',
    'x-mms-language':'de',
    'x-mms-salesline':'Saturn',
    'x-operation':'SearchV4',
}


# HEADER5

header5={
    'authority':'www.saturn.de',
    'method':'GET',
    'path':'/api/v1/graphql?operationName=SearchV4&variables=%7B%22hasMarketplace%22%3Atrue%2C%22isRequestSponsoredSearch%22%3Atrue%2C%22maxNumberOfAds%22%3A2%2C%22isDemonstrationModelAvailabilityActive%22%3Afalse%2C%22withMarketingInfos%22%3Afalse%2C%22categoryIds%22%3A%22CAT_DE_SAT_66%22%2C%22experiment%22%3A%22mp%22%2C%22filters%22%3A%5B%22brand%3AAPPLE%22%5D%2C%22page%22%3A1%2C%22query%22%3A%22MacBook%2BAir%20-maus%22%2C%22sessionId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22customerId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22pageType%22%3A%22Search%22%2C%22productFilters%22%3A%5B%5B%22brand%3AAPPLE%22%5D%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%223cb930f1763026b9a724d9867a77c7085731d1c4193806a9752db52bf44e3482%22%7D%2C%22pwa%22%3A%7B%22salesLine%22%3A%22Saturn%22%2C%22country%22%3A%22DE%22%2C%22language%22%3A%22de%22%2C%22ccr%22%3Atrue%7D%7D',
    'scheme':'https',
    'accept':'*/*',
    'accept-language':'en-GB,en-US;q=0.9,en;q=0.8',
    'apollographql-client-name':'pwa-client',
    'apollographql-client-version':'1.79.0',
    'cache-control':'no-cache',
    'content-type':'application/json',
    'cookie':'optid=0e26086e-b797-4ce7-b30a-c51085ddc0a7; pwaconsent=v:1.0~required:1&clf:1,cli:1,gfb:1,gtm:1,jot:1,ocx:1|comfort:1&baz:1,cne:1,fix:1,gfa:1,gfc:1,goa:1,gom:1,grc:1,grv:1,lob:1,opt:1,orc:1,ore:1,prd:1,sen:1,sis:1,spe:1,sst:1,swo:1,twi:1,usw:1,usz:1,yte:1|marketing:1&asm:1,cad:1,cma:1,eam:1,fab:1,fbn:1,gad:1,gam:1,gcm:1,gdv:1,gos:1,gse:1,gst:1,kru:1,msb:1,omp:1,pin:1,ttd:1,twt:1|; _gcl_au=1.1.2080703172.1654864663; NoCookie=true; _pin_unauth=dWlkPU5ERXhaVE5pWTJZdFpEaGtPQzAwTURVM0xXRTFZemt0WWpSalpXTTNZVEUyTW1SbQ; cf_clearance=SA_u608X7uLRJs_vMu6xpDUPoner9KWCF01LAfoUiEY-1655299743-0-1-3b6693ae.23026482.6c67cc4e-150; _gid=GA1.2.1270608410.1655882585; a=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im8yc2lnbiJ9.eyJzdWIiOiJlZmYxNGY0NC1iZmYzLTRiMDMtOTY1Mi02YjUzMTMwYjA5YWEiLCJpc3MiOiJtbXNlIiwiaWF0IjoxNjU1OTY2OTYyLCJleHAiOjE2NTcxNzY1NjIsImF1ZCI6IndlYm1vYmlsZSIsInQiOiJ1IiwibyI6MTAxNX0.AL8qpjEkEiEuo20P67EsysB2oTrr_bOCNmw8hKz-I127-11AO3R4G2vcThwQsLjDmlI3HNW3dLuH1bcAxFGX_ybV2ZaTeUxd31HVgW89eKGXDkHEda8xU-lT8iADo6vrbErd6UN8RtyLDk3uhr_7KsWkVngyhbcLGFRtrs12dzuyH6Cdrl4oEbnql1-171nbKlJPexazt5Ea0j-XOnPYaTLfnpSufyb81zZMwKSNYxJPtPoFDz5YrWD84gV9ixfZIQ3lE4ICsn8CLY7_JlhjTOfnR5UbSFQ139EI7oH1APhWw1RY-U9l-VyoVUp3wS6CCiy-uh3neW2kB7jV0C3cTQ; r=SNNEXcEnxhvmK5iUOgWI73bkZ7RdPm6DnIEAxl9L66oRUN9l26wXWK0VWUQBAEam; BVBRANDID=d6ed1941-5d54-4cc5-b733-73b53a05572a; ts_id=3eae2cf6-d91d-4a19-a703-3d03c82578a1; t_fpd=true; s_id=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; MC_PS_SESSION_ID=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; p_id=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; MC_PS_USER_ID=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; __cfruid=5ce9277937f35b0509ea571d823a42e90d1feb4c-1656047481; lux_uid=165604748329125097; _clck=1vw2yro|1|f2l|0; __cf_bm=ovzwKNsIM5n_wLhiCZCFpM3UtRjCa0EuMqnwdfomWGs-1656049282-0-AU3hWw6cFWhrHR/Vc2tfTg0sb+BVtVhHYXHO3th02J8dUtechz2ZVXZqnvzT/nUjQxjAZeR39f9gqGnRpjTHZtLJ+CClbhEEcV5D9uvuki14; _dc_gtm_UA-25101917-1=1; _ga=GA1.2.69ecb800-76e8-4ca4-864b-aaae21efda0b; _uetsid=28915a40f1fc11eca7afb9eecc1c579a; _uetvid=24005d80e8ba11ec98bccb532996a8b6; _clsk=11av6ee|1656049742069|17|1|h.clarity.ms/collect; _ga_9ZJL7DLSGD=GS1.1.1656047483.31.1.1656049779.60; _msbps=97',
    'pragma':'no-cache',
    'referer':'https://www.saturn.de/de/brand/apple/mac/macbook-air',
    'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-cacheable':'true',
    'x-flow-id':'4caad086-96d2-4c80-b0a2-15e6ecce215a',
    'x-mms-country':'DE',
    'x-mms-language':'de',
    'x-mms-salesline':'Saturn',
    'x-operation':'SearchV4',
    }


# HEADER6

header6={
    'authority':'www.saturn.de',
    'method':'GET',
    'path':'/api/v1/graphql?operationName=CategoryV4&variables=%7B%22hasMarketplace%22%3Atrue%2C%22maxNumberOfAds%22%3A2%2C%22isRequestSponsoredSearch%22%3Atrue%2C%22isDemonstrationModelAvailabilityActive%22%3Afalse%2C%22withMarketingInfos%22%3Afalse%2C%22filters%22%3A%5B%5D%2C%22pimCode%22%3A%22CAT_DE_SAT_106%22%2C%22page%22%3A1%2C%22experiment%22%3A%22mp%22%2C%22sessionId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22customerId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22pageType%22%3A%22Category%22%2C%22productFilters%22%3A%5B%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22e32ccad3bd5aa0781a4e27cf31af311d7936e6513719045adc070371710afa4c%22%7D%2C%22pwa%22%3A%7B%22salesLine%22%3A%22Saturn%22%2C%22country%22%3A%22DE%22%2C%22language%22%3A%22de%22%2C%22ccr%22%3Atrue%7D%7D',
    'scheme':'https',
    'accept':'*/*',
    'accept-language':'en-GB,en-US;q=0.9,en;q=0.8',
    'apollographql-client-name':'pwa-client',
    'apollographql-client-version':'1.79.0',
    'cache-control':'no-cache',
    'content-type':'application/json',
    'cookie':'optid=0e26086e-b797-4ce7-b30a-c51085ddc0a7; pwaconsent=v:1.0~required:1&clf:1,cli:1,gfb:1,gtm:1,jot:1,ocx:1|comfort:1&baz:1,cne:1,fix:1,gfa:1,gfc:1,goa:1,gom:1,grc:1,grv:1,lob:1,opt:1,orc:1,ore:1,prd:1,sen:1,sis:1,spe:1,sst:1,swo:1,twi:1,usw:1,usz:1,yte:1|marketing:1&asm:1,cad:1,cma:1,eam:1,fab:1,fbn:1,gad:1,gam:1,gcm:1,gdv:1,gos:1,gse:1,gst:1,kru:1,msb:1,omp:1,pin:1,ttd:1,twt:1|; _gcl_au=1.1.2080703172.1654864663; NoCookie=true; _pin_unauth=dWlkPU5ERXhaVE5pWTJZdFpEaGtPQzAwTURVM0xXRTFZemt0WWpSalpXTTNZVEUyTW1SbQ; cf_clearance=SA_u608X7uLRJs_vMu6xpDUPoner9KWCF01LAfoUiEY-1655299743-0-1-3b6693ae.23026482.6c67cc4e-150; _gid=GA1.2.1270608410.1655882585; a=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im8yc2lnbiJ9.eyJzdWIiOiJlZmYxNGY0NC1iZmYzLTRiMDMtOTY1Mi02YjUzMTMwYjA5YWEiLCJpc3MiOiJtbXNlIiwiaWF0IjoxNjU1OTY2OTYyLCJleHAiOjE2NTcxNzY1NjIsImF1ZCI6IndlYm1vYmlsZSIsInQiOiJ1IiwibyI6MTAxNX0.AL8qpjEkEiEuo20P67EsysB2oTrr_bOCNmw8hKz-I127-11AO3R4G2vcThwQsLjDmlI3HNW3dLuH1bcAxFGX_ybV2ZaTeUxd31HVgW89eKGXDkHEda8xU-lT8iADo6vrbErd6UN8RtyLDk3uhr_7KsWkVngyhbcLGFRtrs12dzuyH6Cdrl4oEbnql1-171nbKlJPexazt5Ea0j-XOnPYaTLfnpSufyb81zZMwKSNYxJPtPoFDz5YrWD84gV9ixfZIQ3lE4ICsn8CLY7_JlhjTOfnR5UbSFQ139EI7oH1APhWw1RY-U9l-VyoVUp3wS6CCiy-uh3neW2kB7jV0C3cTQ; r=SNNEXcEnxhvmK5iUOgWI73bkZ7RdPm6DnIEAxl9L66oRUN9l26wXWK0VWUQBAEam; BVBRANDID=d6ed1941-5d54-4cc5-b733-73b53a05572a; ts_id=3eae2cf6-d91d-4a19-a703-3d03c82578a1; t_fpd=true; s_id=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; MC_PS_SESSION_ID=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; p_id=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; MC_PS_USER_ID=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; __cfruid=5ce9277937f35b0509ea571d823a42e90d1feb4c-1656047481; lux_uid=165604748329125097; _clck=1vw2yro|1|f2l|0; __cf_bm=ovzwKNsIM5n_wLhiCZCFpM3UtRjCa0EuMqnwdfomWGs-1656049282-0-AU3hWw6cFWhrHR/Vc2tfTg0sb+BVtVhHYXHO3th02J8dUtechz2ZVXZqnvzT/nUjQxjAZeR39f9gqGnRpjTHZtLJ+CClbhEEcV5D9uvuki14; _msbps=97; _ga=GA1.2.69ecb800-76e8-4ca4-864b-aaae21efda0b; _uetsid=28915a40f1fc11eca7afb9eecc1c579a; _uetvid=24005d80e8ba11ec98bccb532996a8b6; _clsk=11av6ee|1656050797151|21|1|h.clarity.ms/collect; _ga_9ZJL7DLSGD=GS1.1.1656047483.31.1.1656050814.60',
    'pragma':'no-cache',
    'referer':'https://www.saturn.de/de/category/all-in-one-106.html',
    'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-cacheable':'true',
    'x-flow-id':'e5485f37-c24c-40fe-bc94-e651e1226d2a',
    'x-mms-country':'DE',
    'x-mms-language':'de',
    'x-mms-salesline':'Saturn',
    'x-operation':'CategoryV4',
}

# HEADER7

header7={
    'authority':'www.saturn.de',
    'method':'GET',
    'path':'/api/v1/graphql?operationName=CategoryV4&variables=%7B%22hasMarketplace%22%3Atrue%2C%22maxNumberOfAds%22%3A2%2C%22isRequestSponsoredSearch%22%3Atrue%2C%22isDemonstrationModelAvailabilityActive%22%3Afalse%2C%22withMarketingInfos%22%3Afalse%2C%22filters%22%3A%5B%5D%2C%22pimCode%22%3A%22CAT_DE_SAT_83%22%2C%22page%22%3A1%2C%22experiment%22%3A%22mp%22%2C%22sessionId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22customerId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22pageType%22%3A%22Category%22%2C%22productFilters%22%3A%5B%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22e32ccad3bd5aa0781a4e27cf31af311d7936e6513719045adc070371710afa4c%22%7D%2C%22pwa%22%3A%7B%22salesLine%22%3A%22Saturn%22%2C%22country%22%3A%22DE%22%2C%22language%22%3A%22de%22%2C%22ccr%22%3Atrue%7D%7D',
    'scheme':'https',
    'accept':'*/*',
    'accept-language':'en-GB,en-US;q=0.9,en;q=0.8',
    'apollographql-client-name':'pwa-client',
    'apollographql-client-version':'1.79.0',
    'cache-control':'no-cache',
    'content-type':'application/json',
    'cookie':'optid=0e26086e-b797-4ce7-b30a-c51085ddc0a7; pwaconsent=v:1.0~required:1&clf:1,cli:1,gfb:1,gtm:1,jot:1,ocx:1|comfort:1&baz:1,cne:1,fix:1,gfa:1,gfc:1,goa:1,gom:1,grc:1,grv:1,lob:1,opt:1,orc:1,ore:1,prd:1,sen:1,sis:1,spe:1,sst:1,swo:1,twi:1,usw:1,usz:1,yte:1|marketing:1&asm:1,cad:1,cma:1,eam:1,fab:1,fbn:1,gad:1,gam:1,gcm:1,gdv:1,gos:1,gse:1,gst:1,kru:1,msb:1,omp:1,pin:1,ttd:1,twt:1|; _gcl_au=1.1.2080703172.1654864663; NoCookie=true; _pin_unauth=dWlkPU5ERXhaVE5pWTJZdFpEaGtPQzAwTURVM0xXRTFZemt0WWpSalpXTTNZVEUyTW1SbQ; cf_clearance=SA_u608X7uLRJs_vMu6xpDUPoner9KWCF01LAfoUiEY-1655299743-0-1-3b6693ae.23026482.6c67cc4e-150; _gid=GA1.2.1270608410.1655882585; a=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im8yc2lnbiJ9.eyJzdWIiOiJlZmYxNGY0NC1iZmYzLTRiMDMtOTY1Mi02YjUzMTMwYjA5YWEiLCJpc3MiOiJtbXNlIiwiaWF0IjoxNjU1OTY2OTYyLCJleHAiOjE2NTcxNzY1NjIsImF1ZCI6IndlYm1vYmlsZSIsInQiOiJ1IiwibyI6MTAxNX0.AL8qpjEkEiEuo20P67EsysB2oTrr_bOCNmw8hKz-I127-11AO3R4G2vcThwQsLjDmlI3HNW3dLuH1bcAxFGX_ybV2ZaTeUxd31HVgW89eKGXDkHEda8xU-lT8iADo6vrbErd6UN8RtyLDk3uhr_7KsWkVngyhbcLGFRtrs12dzuyH6Cdrl4oEbnql1-171nbKlJPexazt5Ea0j-XOnPYaTLfnpSufyb81zZMwKSNYxJPtPoFDz5YrWD84gV9ixfZIQ3lE4ICsn8CLY7_JlhjTOfnR5UbSFQ139EI7oH1APhWw1RY-U9l-VyoVUp3wS6CCiy-uh3neW2kB7jV0C3cTQ; r=SNNEXcEnxhvmK5iUOgWI73bkZ7RdPm6DnIEAxl9L66oRUN9l26wXWK0VWUQBAEam; BVBRANDID=d6ed1941-5d54-4cc5-b733-73b53a05572a; ts_id=3eae2cf6-d91d-4a19-a703-3d03c82578a1; t_fpd=true; s_id=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; MC_PS_SESSION_ID=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; p_id=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; MC_PS_USER_ID=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; __cfruid=5ce9277937f35b0509ea571d823a42e90d1feb4c-1656047481; lux_uid=165604748329125097; _clck=1vw2yro|1|f2l|0; __cf_bm=ovzwKNsIM5n_wLhiCZCFpM3UtRjCa0EuMqnwdfomWGs-1656049282-0-AU3hWw6cFWhrHR/Vc2tfTg0sb+BVtVhHYXHO3th02J8dUtechz2ZVXZqnvzT/nUjQxjAZeR39f9gqGnRpjTHZtLJ+CClbhEEcV5D9uvuki14; _ga=GA1.2.69ecb800-76e8-4ca4-864b-aaae21efda0b; _uetsid=28915a40f1fc11eca7afb9eecc1c579a; _uetvid=24005d80e8ba11ec98bccb532996a8b6; _dc_gtm_UA-25101917-1=1; _clsk=11av6ee|1656050891016|23|1|h.clarity.ms/collect; _ga_9ZJL7DLSGD=GS1.1.1656047483.31.1.1656050919.60; _msbps=98',
    'pragma':'no-cache',
    'referer':'https://www.saturn.de/de/category/2-in-1-convertibles-83.html',
    'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-cacheable':'true',
    'x-flow-id':'12054555-56a6-4dbc-aeb1-d8ec545b5d18',
    'x-mms-country':'DE',
    'x-mms-language':'de',
    'x-mms-salesline':'Saturn',
    'x-operation':'CategoryV4',
}


# HEADER8

header8={
    'authority':'www.saturn.de',
    'method':'GET',
    'path':'/api/v1/graphql?operationName=CategoryV4&variables=%7B%22hasMarketplace%22%3Atrue%2C%22maxNumberOfAds%22%3A2%2C%22isRequestSponsoredSearch%22%3Atrue%2C%22isDemonstrationModelAvailabilityActive%22%3Afalse%2C%22withMarketingInfos%22%3Afalse%2C%22filters%22%3A%5B%5D%2C%22pimCode%22%3A%22CAT_DE_SAT_66%22%2C%22page%22%3A1%2C%22experiment%22%3A%22mp%22%2C%22sessionId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22customerId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22pageType%22%3A%22Category%22%2C%22productFilters%22%3A%5B%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22e32ccad3bd5aa0781a4e27cf31af311d7936e6513719045adc070371710afa4c%22%7D%2C%22pwa%22%3A%7B%22salesLine%22%3A%22Saturn%22%2C%22country%22%3A%22DE%22%2C%22language%22%3A%22de%22%2C%22ccr%22%3Atrue%7D%7D',
    'scheme':'https',
    'accept':'*/*',
    'accept-language':'en-GB,en-US;q=0.9,en;q=0.8',
    'apollographql-client-name':'pwa-client',
    'apollographql-client-version':'1.79.0',
    'cache-control':'no-cache',
    'content-type':'application/json',
    'cookie':'optid=0e26086e-b797-4ce7-b30a-c51085ddc0a7; pwaconsent=v:1.0~required:1&clf:1,cli:1,gfb:1,gtm:1,jot:1,ocx:1|comfort:1&baz:1,cne:1,fix:1,gfa:1,gfc:1,goa:1,gom:1,grc:1,grv:1,lob:1,opt:1,orc:1,ore:1,prd:1,sen:1,sis:1,spe:1,sst:1,swo:1,twi:1,usw:1,usz:1,yte:1|marketing:1&asm:1,cad:1,cma:1,eam:1,fab:1,fbn:1,gad:1,gam:1,gcm:1,gdv:1,gos:1,gse:1,gst:1,kru:1,msb:1,omp:1,pin:1,ttd:1,twt:1|; _gcl_au=1.1.2080703172.1654864663; NoCookie=true; _pin_unauth=dWlkPU5ERXhaVE5pWTJZdFpEaGtPQzAwTURVM0xXRTFZemt0WWpSalpXTTNZVEUyTW1SbQ; cf_clearance=SA_u608X7uLRJs_vMu6xpDUPoner9KWCF01LAfoUiEY-1655299743-0-1-3b6693ae.23026482.6c67cc4e-150; _gid=GA1.2.1270608410.1655882585; a=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im8yc2lnbiJ9.eyJzdWIiOiJlZmYxNGY0NC1iZmYzLTRiMDMtOTY1Mi02YjUzMTMwYjA5YWEiLCJpc3MiOiJtbXNlIiwiaWF0IjoxNjU1OTY2OTYyLCJleHAiOjE2NTcxNzY1NjIsImF1ZCI6IndlYm1vYmlsZSIsInQiOiJ1IiwibyI6MTAxNX0.AL8qpjEkEiEuo20P67EsysB2oTrr_bOCNmw8hKz-I127-11AO3R4G2vcThwQsLjDmlI3HNW3dLuH1bcAxFGX_ybV2ZaTeUxd31HVgW89eKGXDkHEda8xU-lT8iADo6vrbErd6UN8RtyLDk3uhr_7KsWkVngyhbcLGFRtrs12dzuyH6Cdrl4oEbnql1-171nbKlJPexazt5Ea0j-XOnPYaTLfnpSufyb81zZMwKSNYxJPtPoFDz5YrWD84gV9ixfZIQ3lE4ICsn8CLY7_JlhjTOfnR5UbSFQ139EI7oH1APhWw1RY-U9l-VyoVUp3wS6CCiy-uh3neW2kB7jV0C3cTQ; r=SNNEXcEnxhvmK5iUOgWI73bkZ7RdPm6DnIEAxl9L66oRUN9l26wXWK0VWUQBAEam; BVBRANDID=d6ed1941-5d54-4cc5-b733-73b53a05572a; ts_id=3eae2cf6-d91d-4a19-a703-3d03c82578a1; t_fpd=true; s_id=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; MC_PS_SESSION_ID=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; p_id=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; MC_PS_USER_ID=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; __cfruid=5ce9277937f35b0509ea571d823a42e90d1feb4c-1656047481; lux_uid=165604748329125097; _clck=1vw2yro|1|f2l|0; __cf_bm=ovzwKNsIM5n_wLhiCZCFpM3UtRjCa0EuMqnwdfomWGs-1656049282-0-AU3hWw6cFWhrHR/Vc2tfTg0sb+BVtVhHYXHO3th02J8dUtechz2ZVXZqnvzT/nUjQxjAZeR39f9gqGnRpjTHZtLJ+CClbhEEcV5D9uvuki14; _msbps=98; _uetsid=28915a40f1fc11eca7afb9eecc1c579a; _uetvid=24005d80e8ba11ec98bccb532996a8b6; _ga=GA1.2.69ecb800-76e8-4ca4-864b-aaae21efda0b; _dc_gtm_UA-25101917-1=1; _clsk=11av6ee|1656050969425|25|1|h.clarity.ms/collect; _ga_9ZJL7DLSGD=GS1.1.1656047483.31.1.1656051012.60',
    'pragma':'no-cache',
    'referer':'https://www.saturn.de/de/category/laptops-66.html',
    'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-cacheable':'true',
    'x-flow-id':'1f7a9757-0409-4cb9-8509-db2339259665',
    'x-mms-country':'DE',
    'x-mms-language':'de',
    'x-mms-salesline':'Saturn',
    'x-operation':'CategoryV4',
    }


# HEADER9

header9={
    'authority':'www.saturn.de',
    'method':'GET',
    'path':'/api/v1/graphql?operationName=CategoryV4&variables=%7B%22hasMarketplace%22%3Atrue%2C%22maxNumberOfAds%22%3A2%2C%22isRequestSponsoredSearch%22%3Atrue%2C%22isDemonstrationModelAvailabilityActive%22%3Afalse%2C%22withMarketingInfos%22%3Afalse%2C%22filters%22%3A%5B%5D%2C%22pimCode%22%3A%22CAT_DE_SAT_105%22%2C%22page%22%3A1%2C%22experiment%22%3A%22mp%22%2C%22sessionId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22customerId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22pageType%22%3A%22Category%22%2C%22productFilters%22%3A%5B%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22e32ccad3bd5aa0781a4e27cf31af311d7936e6513719045adc070371710afa4c%22%7D%2C%22pwa%22%3A%7B%22salesLine%22%3A%22Saturn%22%2C%22country%22%3A%22DE%22%2C%22language%22%3A%22de%22%2C%22ccr%22%3Atrue%7D%7D',
    'scheme':'https',
    'accept':'*/*',
    'accept-language':'en-GB,en-US;q=0.9,en;q=0.8',
    'apollographql-client-name':'pwa-client',
    'apollographql-client-version':'1.79.0',
    'cache-control':'no-cache',
    'content-type':'application/json',
    'cookie':'optid=0e26086e-b797-4ce7-b30a-c51085ddc0a7; pwaconsent=v:1.0~required:1&clf:1,cli:1,gfb:1,gtm:1,jot:1,ocx:1|comfort:1&baz:1,cne:1,fix:1,gfa:1,gfc:1,goa:1,gom:1,grc:1,grv:1,lob:1,opt:1,orc:1,ore:1,prd:1,sen:1,sis:1,spe:1,sst:1,swo:1,twi:1,usw:1,usz:1,yte:1|marketing:1&asm:1,cad:1,cma:1,eam:1,fab:1,fbn:1,gad:1,gam:1,gcm:1,gdv:1,gos:1,gse:1,gst:1,kru:1,msb:1,omp:1,pin:1,ttd:1,twt:1|; _gcl_au=1.1.2080703172.1654864663; NoCookie=true; _pin_unauth=dWlkPU5ERXhaVE5pWTJZdFpEaGtPQzAwTURVM0xXRTFZemt0WWpSalpXTTNZVEUyTW1SbQ; cf_clearance=SA_u608X7uLRJs_vMu6xpDUPoner9KWCF01LAfoUiEY-1655299743-0-1-3b6693ae.23026482.6c67cc4e-150; _gid=GA1.2.1270608410.1655882585; a=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im8yc2lnbiJ9.eyJzdWIiOiJlZmYxNGY0NC1iZmYzLTRiMDMtOTY1Mi02YjUzMTMwYjA5YWEiLCJpc3MiOiJtbXNlIiwiaWF0IjoxNjU1OTY2OTYyLCJleHAiOjE2NTcxNzY1NjIsImF1ZCI6IndlYm1vYmlsZSIsInQiOiJ1IiwibyI6MTAxNX0.AL8qpjEkEiEuo20P67EsysB2oTrr_bOCNmw8hKz-I127-11AO3R4G2vcThwQsLjDmlI3HNW3dLuH1bcAxFGX_ybV2ZaTeUxd31HVgW89eKGXDkHEda8xU-lT8iADo6vrbErd6UN8RtyLDk3uhr_7KsWkVngyhbcLGFRtrs12dzuyH6Cdrl4oEbnql1-171nbKlJPexazt5Ea0j-XOnPYaTLfnpSufyb81zZMwKSNYxJPtPoFDz5YrWD84gV9ixfZIQ3lE4ICsn8CLY7_JlhjTOfnR5UbSFQ139EI7oH1APhWw1RY-U9l-VyoVUp3wS6CCiy-uh3neW2kB7jV0C3cTQ; r=SNNEXcEnxhvmK5iUOgWI73bkZ7RdPm6DnIEAxl9L66oRUN9l26wXWK0VWUQBAEam; BVBRANDID=d6ed1941-5d54-4cc5-b733-73b53a05572a; ts_id=3eae2cf6-d91d-4a19-a703-3d03c82578a1; t_fpd=true; s_id=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; MC_PS_SESSION_ID=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; p_id=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; MC_PS_USER_ID=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; __cfruid=5ce9277937f35b0509ea571d823a42e90d1feb4c-1656047481; lux_uid=165604748329125097; _clck=1vw2yro|1|f2l|0; __cf_bm=ovzwKNsIM5n_wLhiCZCFpM3UtRjCa0EuMqnwdfomWGs-1656049282-0-AU3hWw6cFWhrHR/Vc2tfTg0sb+BVtVhHYXHO3th02J8dUtechz2ZVXZqnvzT/nUjQxjAZeR39f9gqGnRpjTHZtLJ+CClbhEEcV5D9uvuki14; _msbps=98; _ga=GA1.2.69ecb800-76e8-4ca4-864b-aaae21efda0b; _uetsid=28915a40f1fc11eca7afb9eecc1c579a; _uetvid=24005d80e8ba11ec98bccb532996a8b6; _clsk=11av6ee|1656051052621|27|1|h.clarity.ms/collect; _ga_9ZJL7DLSGD=GS1.1.1656047483.31.1.1656051077.60',
    'pragma':'no-cache',
    'referer':'https://www.saturn.de/de/category/pc-105.html?enforcedReload=true',
    'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-cacheable':'true',
    'x-flow-id':'b61496a8-3603-4631-9735-76e835083167',
    'x-mms-country':'DE',
    'x-mms-language':'de',
    'x-mms-salesline':'Saturn',
    'x-operation':'CategoryV4',
}

# proxy_host = "proxy.zyte.com"
# proxy_port = "8011"
# proxy_auth =  "6500c987aae7435a90c249b35b1c9376:"
# proxy_auth1 =  "836fd8e1edb54ecc8ff5231d5eaa9170:"
#
# proxies = {"https": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
#            "http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)}
#
# url1='https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_2582","page":1,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"e32ccad3bd5aa0781a4e27cf31af311d7936e6513719045adc070371710afa4c"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
# r1=requests.get(url=url1,headers=header1,proxies=proxies,verify=False)
#
# url2='https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_5197","page":1,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
# r2=requests.get(url=url2,headers=header2,proxies=proxies,verify=False)
#
# url3='https://www.saturn.de/api/v1/graphql?operationName=SearchV4&variables={"hasMarketplace":true,"isRequestSponsoredSearch":true,"maxNumberOfAds":2,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"categoryIds":"CAT_DE_SAT_1","experiment":"mp","filters":["brand:APPLE"],"page":1,"query":"Mac","sessionId":"aa0c43f3-eefe-44ec-a270-852dae0dde21","customerId":"aa0c43f3-eefe-44ec-a270-852dae0dde21","pageType":"Search","productFilters":[["brand:APPLE"]]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"9fb05c43e35132d1652195e729b67ea5bffe51ed3f87338aeaceafd29004b150"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
# r3=requests.get(url=url3,headers=header3,proxies=proxies,verify=False)
#
#
# url4='https://www.saturn.de/api/v1/graphql?operationName=SearchV4&variables=%7B%22hasMarketplace%22%3Atrue%2C%22isRequestSponsoredSearch%22%3Atrue%2C%22maxNumberOfAds%22%3A2%2C%22isDemonstrationModelAvailabilityActive%22%3Afalse%2C%22withMarketingInfos%22%3Afalse%2C%22categoryIds%22%3A%22CAT_DE_SAT_66%22%2C%22experiment%22%3A%22mp%22%2C%22filters%22%3A%5B%22brand%3AAPPLE%22%5D%2C%22page%22%3A1%2C%22query%22%3A%22MacBook%2BPro%20-maus%22%2C%22sessionId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22customerId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22pageType%22%3A%22Search%22%2C%22productFilters%22%3A%5B%5B%22brand%3AAPPLE%22%5D%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%223cb930f1763026b9a724d9867a77c7085731d1c4193806a9752db52bf44e3482%22%7D%2C%22pwa%22%3A%7B%22salesLine%22%3A%22Saturn%22%2C%22country%22%3A%22DE%22%2C%22language%22%3A%22de%22%2C%22ccr%22%3Atrue%7D%7D'
# r4=requests.get(url=url4,headers=header4,proxies=proxies,verify=False)
#
#
# url5='https://www.saturn.de/api/v1/graphql?operationName=SearchV4&variables=%7B%22hasMarketplace%22%3Atrue%2C%22isRequestSponsoredSearch%22%3Atrue%2C%22maxNumberOfAds%22%3A2%2C%22isDemonstrationModelAvailabilityActive%22%3Afalse%2C%22withMarketingInfos%22%3Afalse%2C%22categoryIds%22%3A%22CAT_DE_SAT_66%22%2C%22experiment%22%3A%22mp%22%2C%22filters%22%3A%5B%22brand%3AAPPLE%22%5D%2C%22page%22%3A1%2C%22query%22%3A%22MacBook%2BAir%20-maus%22%2C%22sessionId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22customerId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22pageType%22%3A%22Search%22%2C%22productFilters%22%3A%5B%5B%22brand%3AAPPLE%22%5D%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%223cb930f1763026b9a724d9867a77c7085731d1c4193806a9752db52bf44e3482%22%7D%2C%22pwa%22%3A%7B%22salesLine%22%3A%22Saturn%22%2C%22country%22%3A%22DE%22%2C%22language%22%3A%22de%22%2C%22ccr%22%3Atrue%7D%7D'
# r5=requests.get(url=url5,headers=header5,proxies=proxies,verify=False)
#
#
# url6='https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_106","page":1,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
# r6=requests.get(url=url6,headers=header6,proxies=proxies,verify=False)
#
# url7='https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_83","page":1,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
# r7=requests.get(url=url7,headers=header7,proxies=proxies,verify=False)
#
#
# url8='https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_66","page":1,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
# r8=requests.get(url=url8,headers=header8,proxies=proxies,verify=False)
#
# url9='https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_105","page":1,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
# r9=requests.get(url=url9,headers=header9,proxies=proxies,verify=False)
#
#
# print("Status_1",r1.status_code)
# print("Status_2",r2.status_code)
# print("Status_3",r3.status_code)
# print("Status_4",r4.status_code)
# print("Status_5",r5.status_code)
# print("Status_6",r6.status_code)
# print("Status_7",r7.status_code)
# print("Status_8",r8.status_code)
# print("Status_9",r9.status_code)
#
#
#















