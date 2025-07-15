from item.models import Cover_Image

def cover_image(request):
    try:
        return {
            'cover_image': Cover_Image.objects.last()
        }
    except:
        return {
            'cover_image': None
        }