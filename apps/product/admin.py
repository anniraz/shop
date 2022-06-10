from django.contrib import admin
from apps.product.models import Category,Product,Images,Review
from mptt.admin import DraggableMPTTAdmin
from apps.product.forms import ReviewForm

# Register your models here.


# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ['title']}
#     list_display=('title','parent')
#     empty_value_display = '----'


# admin.site.register(Category,CategoryAdmin)


admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        'id',
        
    ),
    list_display_links=(
        'indented_title',
    ),
    prepopulated_fields = {'slug': ['title']},empty_value_display = '----'
)



class ProductImagesInine(admin.TabularInline):
    model=Images
    extra= 3

class ProductAdmin(admin.ModelAdmin):
    # ModelAdmin.list_max_show_all
    empty_value_display = '-empty-'
    prepopulated_fields={'slug':['title']}
    list_display = ('title','category', 'status', 'price', 'image_tag','id')
    readonly_fields=('image_tag',)
    list_filter=['category']
    inlines = [ProductImagesInine]


admin.site.register(Product,ProductAdmin)


class ImagesAdmin(admin.ModelAdmin):
    # ModelAdmin.list_max_show_all
    empty_value_display = '-empty-'
    list_display = ('id','product', 'image_tag')
    readonly_fields=('image_tag',)


admin.site.register(Images,ImagesAdmin)


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewForm
    # ModelAdmin.list_max_show_all
    empty_value_display = '-empty-'
    


admin.site.register(Review,ReviewAdmin)