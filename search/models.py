from django.db import models

# Create your models here.
from datetime import datetime
from elasticsearch_dsl import DocType, Date, Nested, Boolean, \
    analyzer, InnerObjectWrapper, Completion, Keyword, Text, Integer
from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer

from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=["localhost"])


class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}


ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])


class ArticleType(DocType):
    # 绿茶软件园类型
    suggest = Completion(analyzer=ik_analyzer)
    title = Text(analyzer="ik_max_word")
    url = Keyword()
    url_object_id = Keyword()
    front_image_url = Keyword()
    front_image_path = Keyword()
    type = Keyword()
    size = Keyword()
    update_time = Date()
    content = Text(analyzer="ik_max_word")
    tag = Text(analyzer="ik_max_word")
    fav_nums = Integer()
    download_urls = Keyword()

    class Meta:
        index = "lcsoft"
        doc_type = "article"


if __name__ == '__main__':
    ArticleType.init()
