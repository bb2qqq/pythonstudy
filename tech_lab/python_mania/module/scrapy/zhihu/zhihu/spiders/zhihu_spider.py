import scrapy
import os
import datetime
from re import findall

from zhihu.items import ZhihuItem

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ["zhihu.com"]
    start_urls = [
#        "http://www.zhihu.com/people/zengjuchen/answers?order_by=vote_num",
#        "http://www.zhihu.com/people/hu-wen-chao/answers?order_by=vote_num",
#        "http://www.zhihu.com/people/lisongwei/answers?order_by=vote_num",
#        "http://www.zhihu.com/people/kaiserwang730/answers?order_by=vote_num",
        "http://www.zhihu.com/people/liangbianyao/answers?order_by=vote_num",
#        "http://www.zhihu.com/people/zengjuchen/posts",
    ]

    # parse() will process through responses returned by requests send to start_urls
    def parse(self, response):
        self.url_head = 'http://www.zhihu.com'

        self.dirname = os.getcwd() + "/" + response.url.split("/")[-2] + "/"
        if not os.path.exists(self.dirname):
            os.makedirs(self.dirname)

        page_list = response.xpath('//span').re('page=[0-9]*')
        page_dict = {int(i.split('=')[-1]): i for i in page_list}
        max_page = max(page_dict.keys())

        for i in xrange(1, max_page + 1):
            page_url = response.url + '&page=' + str(i)
            yield scrapy.Request(page_url, callback=self.parse_page)

    def parse_page(self, response):
        answers_url_list = response.xpath('//a[@class="question_link"]').re('/[A-z0-9/]{5,}')
        for answer_url in answers_url_list:
            yield scrapy.Request(self.url_head + answer_url, callback=self.parse_content)

    def parse_content(self, response):
        file_name = response.xpath('//title/text()').extract()[0].replace("/", "_")
        # Prepend vote nums in the name of file for every answers
        vote_num_list = findall( r'data-votecount="[0-9]*', response.body)
        vote_num = vote_num_list[0].split('="')[-1]
        file_name = vote_num + '_' + file_name
        self.write_files(self.dirname,  file_name, response.body)

    def write_files(self, dirname, file_name, content, flag=None):
        if flag == 'a':
            with open(dirname + file_name, 'a') as f:
                f.write(content)
        else:
            with open(dirname + file_name, 'wb') as f:
                f.write(content)



class QuestionSpider(scrapy.Spider):
    name = 'zhihu_question'
    allowed_domains = ["zhihu.com"]
    start_urls = [
        "http://www.zhihu.com/#signin",
    ]

    # parse() will process through responses returned by requests send to start_urls
    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'poor33@126.com', 'password': 'vimisgood'},
            callback=self.after_login
        )

    def after_login(self, response):
        page_url = "http://www.zhihu.com/question/34535765",
        yield scrapy.Request(page_url, callback=self.parse_page)

    def parse_page(self, response):
        dirname = os.getcwd() + "/" + "questions" + "/"
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        file_name = response.url.split("/")[-1] + "_" + response.xpath('//title/text()').extract()[0].replace("/", "_")
        with open(dirname + file_name, 'wb') as f:
            f.write(response.body)
