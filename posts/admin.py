# from django.contrib import admin
# from django.contrib.admin import ModelAdmin

# from .models import Posts
# from photo.models import Photo
# from document.models import Document
# from video.models import Video



# @admin.register(Posts)
# class PostsAdmin(ModelAdmin):
#     list_display = ('id', 'chat', 'created_date', 'modified_date', 'photos', 'videos', 'documents')

#     def photos(self, obj: Posts):
#         return ', '.join([str(photo) for photo in obj.photos.all()])

#     def videos(self, obj: Posts):
#         return ', '.join([str(video) for video in obj.videos.all()])
        
#     def documents(self, obj: Posts):
#         return ', '.join([str(document) for document in obj.documents.all()])


#     photos.short_description = 'Photos'
#     videos.short_description = 'Videos'
#     documents.short_description = 'Documents'



# @admin.register(Photo)
# class PostsAdmin(ModelAdmin):
#     list_display = ('post', 'file')



# @admin.register(Video)
# class PostsAdmin(ModelAdmin):
#     list_display = ('post', 'file')


# @admin.register(Document)
# class PostsAdmin(ModelAdmin):
#     list_display = ('post', 'file')
