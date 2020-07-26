from PIL import Image
from rest_framework.decorators import api_view
from Blog.models import postmodel
from django.http import HttpResponse
# from resizeimage import resizeimage 
def image_filter(request, img, height, width):
    try:
        image = postmodel.objects.get(post_img='media_blog/' + img)
        if image:
            open_img = Image.open(image.post_img)
            resize_img_height = resizeimage.resize_height(open_img, height)
            resize_img_width = resizeimage.resize_width(resize_img_height, width)
            resize_img_width.save('media/media_blog/resized_' + img, resize_img_width.format)
            resized_image = open('media/media_blog/resized_' + img, 'rb')
            return HttpResponse(resized_image, content_type="image/png")
    except Exception:
        return HttpResponse('Image not found', status=404)




print("hello")