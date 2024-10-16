from api.serializers import OwnerSerializer, BikeSerializer, BusSerializer, CarSerializer, VehicleSerializer
from rest_framework.views import APIView
from api.models import Car, Vehicle, Bus, Bike, Owner
from rest_framework.response import Response
from .MyPagination import MyPageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from .MyPermission import IsOwnerOrReadOnly


class OwnerApiWithoutId(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, format=None):
        query = Owner.objects.all()
        paginator = MyPageNumberPagination()
        paginated_query = paginator.paginate_queryset(query, request)
        serializer = OwnerSerializer(paginated_query, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post(self,request, format=None):
        serializer = OwnerSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({'msg': 'OWNER CREATED '})

        return Response(serializer.errors)


class OwnerAPIWithId(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, pk=None, format=None):
        idd = pk
        query = Owner.objects.get(id=idd)
        serializer = OwnerSerializer(query)

        return Response(serializer.data)

    def put(self, request, pk=None, format=None):
        idd = pk

        query = Owner.objects.get(pk=idd)
        serializer = OwnerSerializer(query, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({'msg': 'OWNER UPDATED '})

        return Response(serializer.errors)

    def patch(self, request, pk=None, format=None):

        idd = pk
        query = Owner.objects.get(pk=idd)
        serializer = OwnerSerializer(query, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response({'msg': 'PARTIAL UPDATE OF OWNER IS DONE '})

        return Response(serializer.errors)

    def delete(self, request, pk=None, format=None):

        idd = pk
        query = Owner.objects.get(id=idd)
        query.delete()

        return Response({'msg': ' OWNER DELETED SUCCESSFULLY '})


class VehicleApiWithoutId(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, format=None):
        query = Vehicle.objects.all()
        paginator = MyPageNumberPagination()
        paginated_query = paginator.paginate_queryset(query, request)
        serializer = VehicleSerializer(paginated_query, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self,request, format=None):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'msg': 'Vehicle CREATED '})

        return Response(serializer.errors)


class VehicleAPIWithId(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, pk=None, format=None):

        idd = pk
        query = Vehicle.objects.get(id=idd)
        serializer = VehicleSerializer(query)

        return Response(serializer.data)

    def put(self, request, pk=None, format=None):

        idd = pk

        query = Vehicle.objects.get(pk=idd)
        serializer = VehicleSerializer(query, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({'msg': 'Vehicle UPDATED '})

        return Response(serializer.errors)

    def patch(self, request, pk=None, format=None):

        idd = pk
        query = Vehicle.objects.get(pk=idd)
        serializer = VehicleSerializer(query, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response({'msg': 'PARTIAL UPDATE OF Vehicle IS DONE '})

        return Response(serializer.errors)

    def delete(self, request, pk=None, format=None):

        idd = pk
        query = Vehicle.objects.get(id=idd)
        query.delete()

        return Response({'msg': ' OWNER DELETED SUCCESSFULLY '})


class BikeApiWithoutId(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, format=None):
        query = Bike.objects.all()
        paginator = MyPageNumberPagination()
        paginated_query = paginator.paginate_queryset(query, request)
        serializer = BikeSerializer(paginated_query, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self,request, format=None):
        serializer = BikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'msg': 'Bike CREATED '})

        return Response(serializer.errors)


class BikeAPIWithId(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, pk=None, format=None):
        idd = pk
        query =  Bike.objects.get(id=idd)
        serializer = BikeSerializer(query)

        return Response(serializer.data)

    def put(self, request, pk=None, format=None):

        idd = pk

        query = Bike.objects.get(pk=idd)
        serializer = BikeSerializer(query, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({'msg': 'Bike UPDATED '})

        return Response(serializer.errors)

    def patch(self, request, pk=None, format=None):

        idd = pk
        query = Bike.objects.get(pk=idd)
        serializer = BikeSerializer(query, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response({'msg': 'PARTIAL UPDATE OF Bike IS DONE '})

        return Response(serializer.errors)

    def delete(self, request, pk=None, format=None):

        idd = pk
        query = Bike.objects.get(id=idd)
        query.delete()

        return Response({'msg': ' Bike DELETED SUCCESSFULLY '})


class BusApiWithoutId(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, format=None):

        query = Bus.objects.all()
        paginator = MyPageNumberPagination()
        paginated_query = paginator.paginate_queryset(query, request)
        serializer = BusSerializer(paginated_query, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = BusSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'msg': 'bus CREATED '})

        return Response(serializer.errors)


class BusAPIWithId(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, pk=None, format=None):
        idd = pk
        query = Bus.objects.get(id=idd)
        serializer = BusSerializer(query)

        return Response(serializer.data)

    def put(self, request, pk=None, format=None):
        idd = pk

        query = Bus.objects.get(pk=idd)
        serializer = BusSerializer(query, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'msg': 'BUS UPDATED '})

        return Response(serializer.errors)

    def patch(self, request, pk=None, format=None):

        idd = pk
        query = Bus.objects.get(pk=idd)
        serializer = BusSerializer(query, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({'msg': 'PARTIAL UPDATE OF BUSS IS DONE '})

        return Response(serializer.errors)

    def delete(self, request, pk=None, format=None):

        idd = pk
        query = Bus.objects.get(id=idd)
        query.delete()

        return Response({'msg': ' BUS DELETED SUCCESSFULLY '})


class CarApiWithoutId(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, format=None):
        query = Car.objects.all()
        paginator = MyPageNumberPagination()
        paginated_query = paginator.paginate_queryset(query, request)
        serializer = CarSerializer(paginated_query, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):

        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'msg': 'CAR CREATED '})

        return Response(serializer.errors)


class CarAPIWithId(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, pk=None, format=None):
        idd = pk
        query = Car.objects.get(id=idd)
        serializer = CarSerializer(query)

        return Response(serializer.data)

    def put(self, request, pk=None, format=None):

        idd = pk

        query = Car.objects.get(pk=idd)
        serializer = CarSerializer(query, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'msg': 'CAR UPDATED '})

        return Response(serializer.errors)

    def patch(self, request, pk=None, format=None):

        idd = pk
        query = Car.objects.get(pk=idd)
        serializer = CarSerializer(query, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({'msg': 'PARTIAL UPDATE OF CAR IS DONE '})

        return Response(serializer.errors)

    def delete(self, request, pk=None, format=None):

        idd = pk
        query = Car.objects.get(id=idd)
        query.delete()

        return Response({'msg': ' CAR DELETED SUCCESSFULLY '})













