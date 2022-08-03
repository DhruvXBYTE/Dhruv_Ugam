# colour_finsh1=response.xpath('//table[@id="productDetails_techSpec_section_1"]//*[contains(text(),"Color")]').getall()
# if not colour_finsh1:
#     colour_finsh2 = response.xpath(
#         '//table[@id="product-specification-table"]//*[contains(text(),"Color")]//..//td//text()').get()
#     if colour_finsh2:
#         mn_colour = c_replace(colour_finsh2).replace('"', '')
#     else:
#         colour_finsh3 = response.xpath(
#             '//table[@id="productDetails_detailBullets_sections1"]//*[contains(text(),"Color")]//..//td//text()').get()
#         if colour_finsh3:
#             mn_colour = c_replace(colour_finsh2).replace('"', '')
#         else:
#             colour_finsh4 = response.xpath(
#                 '//table[@class="a-normal a-spacing-micro"]//*[contains(text(),"Color")]//../following-sibling::td/span/text()').get()
#             if colour_finsh4:
#                 mn_colour = c_replace(colour_finsh4).replace('"', '')
#             else:
#                 mn_colour = "n/a"
# else:
#     if colour_finsh1:
#         mn_colour = c_replace(colour_finsh1).replace('"', '')
#     else:
#         mn_colour = "n/a"



#--------------------  screenshot ---------
# dd = webdriver.ChromeOptions()
#                 dd = webdriver.Chrome(ChromeDriverManager().install())
#                 dd.get("https://www.amazon.com/")
#                 dd.maximize_window()
#                 time.sleep(2)
#                 dd.find_element_by_xpath('//a[@id="nav-global-location-popover-link"]').click()
#                 time.sleep(2)
#                 try:
#                     dd.find_element_by_id('GLUXZipUpdateInput').send_keys(f'{zipcode}')
#                     dd.find_element_by_xpath('//span[@id="GLUXZipUpdate"]').click()
#                     time.sleep(3)
#                     dd.find_element_by_xpath('//div[@class="a-popover-wrapper"]//div[@class="a-popover-footer"]//span[@class="a-declarative"]').click()
#                     time.sleep(2)
#                     cookieimid = ""
#                     d = dd.get_cookies()
#                     for c in d:
#                         cookieimid += '{name}={value}; '.format(
#                             name=c['name'],
#                             value=c['value']
#                         )
#
#                     print(cookieimid)
#
#                 except Exception as e:
#                     print(e)
#
#
#
#                 self.cursor.execute(f"SELECT Id,url,zipcode_input FROM {product_table} where zipcode_input='{zipcode}' AND Status='Pending'")
#                 al_url = [x for x in self.cursor.fetchall()]
#
#                 for i in al_url:
#
#                     row_id = i[0]
#                     url = i[1]
#                     zipcode = i[2]



# ---------------- colour _finsh-----------------

# keyc = response.xpath('//table[@id="productDetails_techSpec_section_1"]//tr//th//text()').getall()
# valc = response.xpath('//table[@id="productDetails_techSpec_section_1"]//tr//td//text()').getall()
#
# if keyc == []:
#     keyc = response.xpath('//table[@id="product-specification-table"]//tr//th//text()').getall()
#     valc = response.xpath('//table[@id="product-specification-table"]//tr//td//text()').getall()
#
#     if keyc == []:
#         keyc = response.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr//th//text()').getall()
#         valc = response.xpath(
#             '//table[@id="productDetails_detailBullets_sections1"]//tr//td[@class="a-size-base prodDetAttrValue"]//text()').getall()
#
#         if keyc == []:
#             keyc = response.xpath(
#                 '//table[@class="a-normal a-spacing-micro"]//*[contains(text(),"Color")]//../following-sibling::td/span/text()').get()
#             if keyc == [] or keyc == None:
#                 mn_colour = "n/a"
#             else:
#                 mn_colour = c_replace(keyc)
#         else:
#             clrc = {}
#             for i, j in zip(keyc, valc):
#                 clrc[i] = j
#             print(clrc)
#             mn_colour = ''
#             for x, l in clrc.items():
#                 if 'Color' == x.strip() or 'Color Code' == x.strip() or 'Color:' == x.strip():
#                     mn_colour = mn_colour + l
#                     break
#             print(mn_colour)
#             if mn_colour == '':
#                 mn_colour = 'n/a'
#             else:
#                 mn_colour = mn_colour
#     else:
#         clrc = {}
#         for i, j in zip(keyc, valc):
#             clrc[i] = j
#         print(clrc)
#         mn_colour = ''
#         for x, l in clrc.items():
#             if 'Color' == x.strip() or 'Color Code' == x.strip() or 'Color:' == x.strip():
#                 mn_colour = mn_colour + l
#                 break
#         print(mn_colour)
#         if mn_colour == '':
#             mn_colour = 'n/a'
#         else:
#             mn_colour = mn_colour
# else:
#     clrc = {}
#     for i, j in zip(keyc, valc):
#         clrc[i] = j
#     print(clrc)
#     mn_colour = ''
#     for x, l in clrc.items():
#         if 'Color' == x.strip() or 'Color Code' == x.strip() or 'Color:' == x.strip():
#             mn_colour = mn_colour + l
#             break
#     print(mn_colour)
#     if mn_colour == '':
#         mn_colour = 'n/a'
#     else:
#         mn_colour = mn_colour