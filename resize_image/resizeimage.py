from PIL import Image
from rest_framework.decorators import api_view
from Blog.models import cat_model
from django.http import HttpResponse
# from resizeimage import resizeimage 
def image_filter(request, img, height, width):
    try:
        image = cat_model.objects.get(cat_icon='Blog_cat_icon/' + img)
        if image:
            open_img = Image.open(image.cat_icon)
            resize_img_height = resizeimage.resize_height(open_img, height)
            resize_img_width = resizeimage.resize_width(resize_img_height, width)
            resize_img_width.save('media/Blog_cat_icon/resized_' + img, resize_img_width.format)
            resized_image = open('media/Blog_cat_icon/resized_' + img, 'rb')
            return HttpResponse(resized_image, content_type="image/jpg")
    except Exception:
        return HttpResponse('Image not found', status=404)



