from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WheelSpecification
from .serializers import WheelSpecificationSerializer

# ✅ POST View: Create a new Wheel Specification
class WheelSpecificationCreateView(APIView):
    def post(self, request):
        serializer = WheelSpecificationSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response({
                "data": {
                    "formNumber": instance.formNumber,
                    "status": "Saved",
                    "submittedBy": instance.submittedBy,
                    "submittedDate": str(instance.submittedDate)
                },
                "message": "Wheel specification submitted successfully.",
                "success": True
            }, status=status.HTTP_201_CREATED)
        return Response({
            "errors": serializer.errors,
            "message": "Validation failed.",
            "success": False
        }, status=status.HTTP_400_BAD_REQUEST)


# ✅ GET View: Return list of all wheel specifications
class WheelSpecificationListView(APIView):
    def get(self, request):
        specs = WheelSpecification.objects.all()
        formatted_data = []

        for spec in specs:
            formatted_data.append({
                "fields": {
                    "condemningDia": spec.condemningDia,
                    "lastShopIssueSize": spec.lastShopIssueSize,
                    "treadDiameterNew": spec.treadDiameterNew,
                    "wheelGauge": spec.wheelGauge
                },
                "formNumber": spec.formNumber,
                "submittedBy": spec.submittedBy,
                "submittedDate": str(spec.submittedDate)
            })

        return Response({
            "data": formatted_data,
            "message": "Filtered wheel specification forms fetched successfully.",
            "success": True
        }, status=status.HTTP_200_OK)

