from scrapy.loader import ItemLoaderfrom scrapy.loader.processors import TakeFirst, Join, Composeclass ProductLoader(ItemLoader):    default_output_processor = TakeFirst()class JdProductLoader(ProductLoader):    price_out = Compose(Join(''), lambda s: s.strip())    comments_out = Compose(Join(''), lambda s: s.strip())    title_out = Compose(Join(''), lambda s: s.strip())## def takefirst_processor(self, values):#self是必须的因为这个函数最终要称为一个类方法，values返回的是price字段获取到的值，这里它是一个列表类型#     print('takefirst_processor')#     print(values)#     print(type(values))#     yield [1, 2, 3]#     #yield values.extract_first()## class JdProductLoader(ItemLoader):#     #price_in = takefirst_processor#     price_out = Compose(Join(), lambda s: s.strip())