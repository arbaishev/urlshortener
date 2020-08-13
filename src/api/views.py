from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from shortenerapp.models import URL
from .serializers import URLSerializer


class URLListView(APIView):
    def get(self, request):
        qs = URL.objects.all()
        serializer = URLSerializer(qs, many=True)
        return Response({"data": {"objects": serializer.data}}, status=status.HTTP_200_OK)


class URLShortener(APIView):
    def post(self, request, *args, **kwargs):
        input_url = request.data.get("url")

        if not request.data.get("custom") or request.data.get("custom") == "False":
            if "http" not in input_url:
                input_url = "http://" + input_url
            obj, created = URL.objects.filter(url=input_url, custom=False).get_or_create(url=input_url)
            return Response({"data": {
                "short_url": f"http://{request.get_host()}/{obj.shortcode}",
                "shortcode": obj.shortcode},
                "error": ""},
                status=status.HTTP_200_OK
            )
        else:
            input_shortcode = request.data.get("custom_shortcode")
            if len(input_shortcode) > 6:
                return Response({"data": {},
                                 "error": "Shortcode too long"},
                                status=status.HTTP_400_BAD_REQUEST
                                )

            if not URL.objects.filter(shortcode=input_shortcode).exists():
                obj = URL.objects.create(url=input_url, shortcode=input_shortcode, custom=True)
                return Response({"data": {
                    "short_url": f"http://{request.get_host()}/{obj.shortcode}",
                    "shortcode": obj.shortcode},
                    "error": ""},
                    status=status.HTTP_200_OK
                )
            else:
                return Response({"data": {},
                                 "error": "Shortcode already exists"},
                                status=status.HTTP_400_BAD_REQUEST
                                )


class URLStats(APIView):
    def get(self, request, shortcode):
        result = {}
        try:
            url = URL.objects.get(shortcode=shortcode)
            result["url"] = url.url
            result["shortcode"] = url.shortcode
            result["created"] = url.created.strftime('%d-%m-%Y %H:%M:%S')
            result["clicks"] = url.count
            if url.count == 0:
                result["recently_used"] = "Never"
            else:
                result["recently_used"] = url.updated.strftime('%d-%m-%Y %H:%M:%S')
            return Response({"data": result, "error": ""}, status=status.HTTP_200_OK)

        except URL.DoesNotExist:
            return Response({"data": {}, "error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
