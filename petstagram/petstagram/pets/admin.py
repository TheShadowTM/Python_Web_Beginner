from django.contrib import admin

from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'publication_date', 'pets')

    @staticmethod
    def pets(current_photo_obj):
        # return ', '.join([p.name for p in current_photo_obj.tagged_pets.all()])
        tagged_pets = current_photo_obj.tagged_pets.all()
        if tagged_pets:
            return ', '.join(p.name for p in tagged_pets)
        return 'No pets'
