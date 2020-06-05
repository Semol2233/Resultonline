
# # class DRFPostSerializer(serializers.ModelSerializer):
# #     #  uri       = serializers.SerializerMethodField(read_only=True)
# #      channel   = UserPublicSrtilizer(read_only=True)
# #      Ceatgory  = serializers.CharField()
# #      class Meta:
# #         model = PostCreate
# #         fields = [
# #             # 'uri',
# #             'channel',
# #             'title',
# #             'photo',
# #             'Ceatgory',
# #             'view',
# #             'uploaded',
# #         ]
# #         read_only_fields = ['channel']


# #     #  def get_uri(self,obj):
# #     #      return "/{id}".format(id=obj.id)


# # class CeatgryList(serializers.ModelSerializer):
# #     class Meta:
# #         model = PostCreate
# #         fields =[
# #             'id',
# #             'Ceatgory'
# #         ]

# # class UserPublicSrtilizer(serializers.ModelSerializer):
# #     url      =  serializers.SerializerMethodField(read_only=True)
# #     class Meta:
# #         model = User
# #         fields = [
# #             'id',
# #             'username',
# #             'url',
# #         ]
    
# #     def get_url(self,obj):
# #          return "/{id}".format(id=obj.id)

# class UserPublicSrtilizer(serializers.ModelSerializer):
#     url      =  serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model = User
#         fields = [
#             'id',
#             'username',
#             'url',
#         ]
    
#     def get_url(self,obj):
#          return "/{id}".format(id=obj.id)




# class UserListView(generics.RetrieveAPIView):
#     queryset           = User.objects.filter(is_active=True)
#     serializer_class   = UserDettails
#     lookup_field       = 'username'


# def Login(request):
#     form_valid = True
#     next = request.GET.get('next')
#     form = UserLoginForm(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(username=username,password=password)
#         login(request,user)
#         if next:
#             return redirect(next)
#         return redirect('home_api')
#         form_valid = False
#     context={
#         'form':form,
#         'valid':form_valid,
#     }
#     return render(request,"login.html",context)


# def home(request):
#     return render(request,'home.html')



# def logout_request(request):
#     logout(request)
#     return redirect('/')


# class PostCreate(models.Model):
#     channel            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title              = models.CharField(max_length = 255)
#     details            = models.TextField(blank=True)
#     Ceatgory           = models.ForeignKey(Cetagroy_list, related_name='Ceatgory',on_delete=models.CASCADE)
#     photo              = models.FileField(upload_to='documents/',)
#     view               = models.IntegerField(blank=True,null=True)
#     uploaded           = models.DateTimeField(auto_now_add = True)

#     def __str__(self):
#         return self.title
    


# #root_api
# class DRFPostSerializer(serializers.HyperlinkedModelSerializer):
#      contentowners   = ContentOwner(read_only=True)
#      contentowner = serializers.PrimaryKeyRelatedField(queryset=Ownercontents.objects.all(), source='contentowners' ,write_only=True)

#      channel         = UserPublicSrtilizer(read_only=True)
#      channellist = serializers.PrimaryKeyRelatedField(queryset=Channel.objects.all(), source='channel' ,write_only=True)   

#      mobilebrand     = BrandProfileInfo(read_only=True)
#      mobilebarand = serializers.PrimaryKeyRelatedField(queryset=Cetagroy_list.objects.all(), source='BrandProfileInfo' ,write_only=True)

#      class Meta:
#         model = PostCreate
#         fields = [
#             'contentowners',
#             'channel',
#             'contentowner',
#             'channellist',
#             'mobilebarand',
#             'id',
#             'title',
#             'details',
#             'photo',
#             'mobilebrand',
#             'slug',
#             'view',
#             'release_date',
#             'tag'
#         ]
    




    # class highss_rsatetd(APIView,):
    # parser_classes = (MultiPartParser,FormParser,JSONParser)

    # def get(self, request, format=None):
    #     snippets = Ownercontents.objects.all()
    #     serializer = ContentOwner(snippets, many=True)
    #     return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = ContentOwner(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
