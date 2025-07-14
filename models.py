from django.db import models

class WheelSpecification(models.Model):
    formNumber = models.CharField(max_length=50, unique=True)
    submittedBy = models.CharField(max_length=100)
    submittedDate = models.DateField()

    # Fields from "fields" object
    axleBoxHousingBoreDia = models.CharField(max_length=100, blank=True, null=True)
    bearingSeatDiameter = models.CharField(max_length=100, blank=True, null=True)
    condemningDia = models.CharField(max_length=100, blank=True, null=True)
    intermediateWWP = models.CharField(max_length=100, blank=True, null=True)
    lastShopIssueSize = models.CharField(max_length=100, blank=True, null=True)
    rollerBearingBoreDia = models.CharField(max_length=100, blank=True, null=True)
    rollerBearingOuterDia = models.CharField(max_length=100, blank=True, null=True)
    rollerBearingWidth = models.CharField(max_length=100, blank=True, null=True)
    treadDiameterNew = models.CharField(max_length=100, blank=True, null=True)
    variationSameAxle = models.CharField(max_length=100, blank=True, null=True)
    variationSameBogie = models.CharField(max_length=100, blank=True, null=True)
    variationSameCoach = models.CharField(max_length=100, blank=True, null=True)
    wheelDiscWidth = models.CharField(max_length=100, blank=True, null=True)
    wheelGauge = models.CharField(max_length=100, blank=True, null=True)
    wheelProfile = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.formNumber

