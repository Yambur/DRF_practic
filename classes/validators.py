from rest_framework.serializers import ValidationError


class LinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, link):
        youtube = 'https://youtube.com/'

        if link.get('link_video'):
            if youtube not in link.get('link_video'):
                raise ValidationError('Не правильная сылка')
        else:
            return None
