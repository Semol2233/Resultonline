from rest_framework import serializers
from Data_app.models import CoverImg,target_link

class UseracAlldata(serializers.ModelSerializer):
     class Meta:
        model = target_link
        fields = [
            'target_links'
        ]


class CoverImssge(serializers.ModelSerializer):
      target_link = serializers.SerializerMethodField("get_display")
      class Meta:
          model = CoverImg
          fields = [
            'target_link',
            'title',
            'Cover_img',
            'url'
          ]
      def get_display(self, obj):
        return "/count/"
