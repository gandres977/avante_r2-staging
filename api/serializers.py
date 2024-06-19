from rest_framework import serializers


try:

    from avantecore.models import Provider, ProviderDispatchLocation
    from avantecore.models import Customer, CustomerDispatchLocation
    from avantecore.models import Scale, SmartEdgeSensor
    from avantecore.models import Tote, ToteMove
    from avantecore.models import ScaleEntry, HaulEntry, LedgerEntry
    from avantecore.models import LogisticsState

except:
    pass 

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Provider
        except:
            pass    
        fields = '__all__'

class ProviderDispatchLocationSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = ProviderDispatchLocation
        except:
            pass
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Customer
        except:
            pass
        fields = '__all__'

class CustomerDispatchLocationSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = CustomerDispatchLocation
        except:
            pass
        fields = '__all__'

class ScaleSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Scale
        except:
            pass
        fields = '__all__'

class SmartEdgeSensorSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = SmartEdgeSensor
        except:
            pass
        fields = '__all__'

class ToteSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = Tote
        except:
            pass
        fields = '__all__'

class ToteMoveSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = ToteMove
        except:
            pass
        fields = '__all__'

class ScaleEntrySerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = ScaleEntry
        except:
            pass
        fields = '__all__'

class HaulEntrySerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = HaulEntry
        except:
            pass
        fields = '__all__'

class LedgerEntrySerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = LedgerEntry
        except:
            pass
        fields = '__all__'

class LogisticsStateSerializer(serializers.ModelSerializer):
    class Meta:

        try:
            model = LogisticsState
        except:
            pass
        fields = '__all__'