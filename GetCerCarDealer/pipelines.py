# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GetcercardealerPipeline(object):
    MySep = '^^^'
    def __init__(self):
        self.file = open('CerCarsDealers.txt', 'w')
        
    def WriteAList(self,astr,alist):
        self.file.write(astr +" is ")
        if(len(alist)==0):
            self.file.write("MISSING")
        else:
            for anele in alist:
                self.file.write(('').join(anele).replace("\r\n"," ").strip()) #to a str
                self.file.write(" ")
                self.file.write('\t')
        self.file.write(self.MySep)
        
    def process_item(self, item, spider):
        
        self.WriteAList("dealer_name", item['dealer_name'])
       
        self.WriteAList("dealer_stocks", item['dealer_stocks'])
        
        self.WriteAList("dealer_starrate", item['dealer_starrate'])
        
        self.WriteAList("dealer_ratings", item['dealer_ratings'])
        
        self.WriteAList("dealer_location", item['dealer_location'])
        
        self.WriteAList("dealer_distance", item['dealer_distance'])
        
        self.WriteAList("dealer_phn", item['dealer_phn'])
        
        self.WriteAList("dealer_moreinfo", item['dealer_moreinfo'])
        
        self.file.write("\n")
        
        return item
