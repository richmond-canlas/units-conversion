from .models import ConversionRule, ConversionHistory

class ConversionService:
    @staticmethod
    def convert(value, from_unit, to_unit):
        try:
            rule = ConversionRule.objects.get(from_unit=from_unit, to_unit=to_unit)
            converted_value = value * rule.conversion_rate
            ConversionHistory.objects.create(from_unit=from_unit, to_unit=to_unit, value=value, converted_value=converted_value)
            return converted_value
        except ConversionRule.DoesNotExist:
            raise ValueError("Conversion rule does not exist.")

    @staticmethod
    def batch_convert(conversions):
        results = {}
        for conversion in conversions:
            from_unit = conversion['from_unit']
            to_unit = conversion['to_unit']
            value = conversion['value']
            results[f"{from_unit} to {to_unit}"] = ConversionService.convert(value, from_unit, to_unit)
        return results

    @staticmethod
    def get_supported_units(unit_type):
        # This method should return supported units based on the unit type
        # For simplicity, let's assume we have a predefined dictionary
        supported_units = {
            'length': ['meters', 'kilometers', 'miles'],
            'weight': ['grams', 'kilograms', 'pounds'],
        }
        return supported_units.get(unit_type, [])

    # Add more methods for other functionalities as needed