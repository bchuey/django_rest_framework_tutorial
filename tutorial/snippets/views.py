# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
# from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# from django.http import Http404
# from django.shortcuts import render

# from rest_framework import mixins
from rest_framework import generics

from django.contrib.auth.models import User
from snippets.serializers import UserSerializer

from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly



####### Create your views here. #######

"""
JSONResponse class is not needed anymore
"""
# class JSONResponse(HttpResponse):
# 	"""
# 	An HttpResponse that renders its content into JSON.
# 	"""
# 	def __init__(self, data, **kwargs):
# 		content = JSONRenderer().render(data)
# 		kwargs['content_type'] = 'application/json'
# 		super(JSONResponse, self).__init__(content, **kwargs)

"""
Not using rest_framework
"""
# @csrf_exempt
# def snippet_list(request):
# 	"""
# 	List all code snippets, or create a new snippet.
# 	"""
# 	if request.method == "GET":
# 		snippets = Snippet.objects.all()
# 		serializer = SnippetSerializer(snippets, many=True)
# 		return JSONResponse(serializer.data)
# 	elif request.method == 'POST':
# 		data = JSONParser().parse(request)
# 		serializer = SnippetSerializer(data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JSONResponse(serializer.data, status=201)
# 		return JSONResponse(serializer.errors, status=400)

# @csrf_exempt
# def snippet_detail(request, pk):
# 	"""
# 	Retrieve, update or delete a code snippet.
# 	"""
# 	try:
# 		snippet = Snippet.objects.get(pk=pk)
# 	except Snippet.DoesNotExist:
# 		return HttpResponse(status=404)

# 	if request.method == 'GET':
# 		serializer = SnippetSerializer(snippet)
# 		return JSONResponse(serializer.data)
# 	elif request.method == 'PUT':
# 		data = JSONParser().parse(request)
# 		serializer = SnippetSerializer(snippet, data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JSONResponse(serializer.data)
# 		return JSONResponse(serializer.errors, status=400)
# 	elif request.method == 'DELETE':
# 		snippet.delete()
# 		return HttpResponse(status=204)

"""
REST Framework using FBV

format=None : gives URLs support when an explicit format is given
"""
# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
# 	"""
# 	list all snippets, or create a new snippet
# 	"""
# 	if request.method == 'GET':
# 		snippets = Snippet.objects.all()
# 		serializer = SnippetSerializer(snippets, many=True)
# 		return Response(serializer.data)
# 	elif request.method == 'POST':
# 		serializer = SnippetSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
# 	"""
# 	retrieve, update or delete a snippet instance
# 	"""
# 	try:
# 		snippet = Snippet.objects.get(pk=pk)
# 	except Snippet.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	if request.method == 'GET':
# 		serializer = SnippetSerializer(snippet)
# 		return Response(serializer.data)
# 	elif request.method == 'PUT':
# 		serializer = SnippetSerializer(snippet, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 	elif request.method == 'DELETE':
# 		snippet.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)

"""
Using CBV (w/o Mixins) w/ REST framework 
"""

# class SnippetList(APIView):
# 	"""
# 	list all snippets, or create a new snippet
# 	"""
# 	def get(self, request, format=None):
# 		snippets = Snippet.objects.all()
# 		serializer = SnippetSerializer(snippets, many=True)
# 		return Response(serializer.data)

# 	def post(self, request, format=None):
# 		serializer = SnippetSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SnippetDetail(APIView):
# 	"""
# 	retrieve, update or delete a snippet instance
# 	"""
# 	def get_object(self, pk):
# 		try:
# 			return Snippet.objects.get(pk=pk)
# 		except Snippet.DoesNotExist:
# 			raise Http404

# 	def get(self, request, pk, format=None):
# 		snippet = self.get_object(pk)
# 		serializer = SnippetSerializer(snippet)
# 		return Response(serializer.data)

# 	def put(self, request, pk, format=None):
# 		snippet = self.get_object(pk)
# 		serializer = SnippetSerializer(snippet, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# 	def delete(self, request, pk, format=None):
# 		snippet = self.get_object(pk)
# 		snippet.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)

"""
Using Mixins 
"""
# class SnippetList(mixins.ListModelMixin,
# 					mixins.CreateModelMixin,
# 					generics.GenericAPIView):
# 	queryset = Snippet.objects.all()
# 	serializer_class = SnippetSerializer

# 	def get(self, request, *args, **kwargs):
# 		return self.list(request, *args, **kwargs)

# 	def post(self, request, *args, **kwargs):
# 		return self.create(request, *args, **kwargs)

# class SnippetDetail(mixins.RetrieveModelMixin,
# 					mixins.UpdateModelMixin,
# 					mixins.DestroyModelMixin,
# 					generics.GenericAPIView):

# 	queryset = Snippet.objects.all()
# 	serializer_class = SnippetSerializer

# 	def get(self, request, *args, **kwargs):
# 		return self.retrieve(request, *args, **kwargs)

# 	def put(self, request, *args, **kwargs):
# 		return self.update(request, *args, **kwargs)

# 	def delete(self, request, *args, **kwargs):
# 		return self.destroy(request, *args, **kwargs)


"""
Using generic class based views
"""
# class SnippetList(generics.ListCreateAPIView):

# 	queryset = Snippet.objects.all()
# 	serializer_class = SnippetSerializer
# 	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# 	def perform_create(self, serializer):
# 		serializer.save(owner=self.request.user)

# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

# 	queryset = Snippet.objects.all()
# 	serializer_class = SnippetSerializer
# 	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

"""
Adding the User views
"""
# class UserList(generics.ListAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer

"""
creating entry point to API
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(('GET',))
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format=format),
		'snippets': reverse('snippet-list', request=request, format=format),
	})

"""
creating endpoint for highlight snippets
"""
from rest_framework import renderers

# class SnippetHighlight(generics.GenericAPIView):
# 	queryset = Snippet.objects.all()
# 	renderer_classes = (renderers.StaticHTMLRenderer,)

# 	def get(self, request, *args, **kwargs):
# 		snippet = self.get_object()
# 		return Response(snippet.highlighted)


"""
Refactoring UserList and UserDetail View to use ViewSet
"""
from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	automatically provides 'list' and 'detail' actions
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer



"""
Refactoring Snippet to use ModelViewSet
"""
from rest_framework.decorators import detail_route

class SnippetViewSet(viewsets.ModelViewSet):

	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

	"""
	provide extra 'highlight' action
	"""
	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)










