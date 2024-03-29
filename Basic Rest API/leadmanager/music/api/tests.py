from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Songs
from .serializers import SongSerializer

# Create your tests here.
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_song(title="", artist=""):
        if title != "" and artist != "":
            Songs.objects.create(title=title, artist=artist)

    def setUp(self):
        # add test data
        self.create_song("like glue", "sean paul")
        self.create_song("simple song", 'konshens')
        self.create_song("love is wicked", "brick and lace")
        self.create_song("jam  rock", "damien marley")


class GetAllSongsTest(BaseViewTest):
    def test_get_all_songs(self):
        """
        This test ensures that all songs added in the setUp method exist when we make a GET request to songs/ endpoint
        """

        # hit the APU endpoint
        response = self.client.get(
            reverse("song-all", kwargs={"version":"v1"})
        )

        # fetch the data from db
        expected = Songs.objects.all()
        serializer = SongsSerializer(expected, many=True)

