from GetCerCarDealer.items import GetcercardealerItem
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider

class UsedCarsSpider(CrawlSpider):
    name = "getcercarsdealer"
    allowed_domains = ['www.cars.com']
    total = 256027 #num of pages to crawl for some query, input it after post a qury on target page 
    numperpage = 250 #set by a query
    curnum = 0 #from 1st page
    
    #other_urlhead is the head of other pages to crawl
    other_urlhead = "http://www.cars.com/for-sale/searchresults.action?feedSegId=28705&rpp=250&sf2Nm=miles&cpoId=28444&requestorTrackingInfo=RTB_SEARCH&sf1Nm=price&sf2Dir=ASC&stkTypId=28881&PMmt=0-0-0&zc=60606&rd=100000&sf1Dir=DESC&searchSource=UTILITY&isDealerGrouping=true&crSrtFlds=stkTypId-feedSegId-cpoId&pgId=2102&rn="

    start_urls = [
                  #"http://www.cars.com/for-sale/searchresults.action?feedSegId=28705&rpp=250&sf2Nm=miles&cpoId=28444&requestorTrackingInfo=RTB_SEARCH&sf1Nm=price&sf2Dir=ASC&stkTypId=28881&PMmt=0-0-0&zc=60606&rd=100000&sf1Dir=DESC&searchSource=UTILITY&isDealerGrouping=true&crSrtFlds=stkTypId-feedSegId-cpoId&pgId=2102&rn=0"
                  ]
    
    def GenUrls(self):
        #self.start_urls.append(self.base_url)
        while(self.curnum <= self.total):
            #generate next page url
            
            self.curnum = self.curnum + self.numperpage
            
            self.start_urls.append(self.other_urlhead + str(self.curnum))
        
#         if((self.curnum - self.total) == self.numperpage):
#             pass
#         else:
#             self.start_urls.append(self.other_urlhead + str(self.total))

    def showUrls(self):
        nnum = len(self.start_urls)
        for i in range(nnum):
            print i,'\t',self.start_urls[i],'\n'
        
    def __init__(self):
        #pass
        self.GenUrls()
        #self.showUrls()
        
    def parse(self, response):
        '''
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        '''
        sel = Selector(response)
        
        dealerall = sel.xpath('//*[@id="resultswrapper"]/div[@class="row vehicle dg-row"]')
        
        items = []
        for adealer in dealerall:
            item = GetcercardealerItem()
            
            #item['carname'] is a list, and the elements in it is a unicode
            #carname consists of 2 parts
            
#             dealer_name = Field()
#             dealer_stocks = Field() #number of stocks to sell
#             dealer_starrate = Field()
#             dealer_ratings = Field()
#             dealer_location = Field()
#             dealer_distance = Field()
#             dealer_phn = Field()
#             dealer_moreinfo = Field()
           
            item['dealer_name'] = adealer.xpath('div[2]/h4/a/text()').extract()
            
            item['dealer_stocks'] = adealer.xpath('div[3]/h4/a/text()').extract()  

            item['dealer_starrate'] = adealer.xpath('div[2]/div[@class="rating dealer"]/div[@class="detail"]/text()').re('([0-9][.][0-9])')
             
            item['dealer_ratings'] = adealer.xpath('div[2]/div[@class="rating dealer"]/div[@class="detail"]/a/text()').extract()
            
            item['dealer_location'] = adealer.xpath('div[2]/div[@class="seller clearfix"]/p[1]/text()').extract()
            for alocation in item['dealer_location']:
                alocation = alocation.replace(r'<br>',' ')
            
            item['dealer_distance'] = adealer.xpath('div[2]/div[@class="seller clearfix"]/p[1]/span/text()').extract()
            
            item['dealer_phn'] = adealer.xpath('div[2]/div[@class="seller clearfix"]/p[2]/span[1]/text()').extract()
            
            item['dealer_moreinfo'] = adealer.xpath('div[2]/div[@class="seller clearfix"]/p[2]/span[2]/a/@href').extract()
            
            items.append(item)

        return items


#ucs = UsedCarsSpider()


