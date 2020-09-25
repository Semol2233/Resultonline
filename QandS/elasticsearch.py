# from haystack import indexes
# from .models import *

# import datetime
# class AlbumIndex(indexes.SearchIndex, indexes.Indexable):
#    qname = indexes.CharField(document=True, use_template=True)
#    q_slug = indexes.CharField(model_attr="q_slug")
#    post_views = indexes.IntegerField(model_attr="post_views")
   
#    def get_model(self):
#       return postmodel_q

#    def index_queryset(self, using=None):
#         return self.get_model().objects.all()