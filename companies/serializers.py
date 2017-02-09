from rest_framework import serializers

from .models import Stock

class StockSerializer(serializers.ModelSerializer):
	class Meta:
		model = Stock 
		fields = ('ticker', 'volume')
		# fields = '__all__' would return everything defined in the Stocks models
		# the above may be bad if there is private information stored in Stocks