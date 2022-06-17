
from modeltranslation.translator import translator, TranslationOptions,register
from .models import Product

@register(Product)
class ModelkaTranslationOptions(TranslationOptions):
    
    fields = ('title', 'description',)

