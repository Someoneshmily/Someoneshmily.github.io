#coding=utf-8
from haystack import indexes
from models import BlogContent
#指定对于某个类的某些数据建立索引
class BlogContentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return BlogContent

    def index_queryset(self, using=None):
        return self.get_model().objects.all()