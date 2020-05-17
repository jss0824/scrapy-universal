# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import csv
class ScrapyuniversalPipeline(object):
    def process_item(self, item, spider):
        Title = ('').join(item['Title'])
        Content = ('').join(item['Content'])
        result = {}
        result['Title'] = Title
        result['Content'] = Content
        result = json.dumps(result)

        with open('test.csv', 'a', encoding='utf-8',newline='') as f:
            csv_writer = csv.writer(f)
            # csv_writer.writerow(["Title", "Content"])
            csv_writer.writerow([Title, Content])



        # with open('news.csv', 'a', newline='') as f:
        #     f.write(result + '\n')
        return item
