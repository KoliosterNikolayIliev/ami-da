class SwapDisplayOrderMixin:
    def save_model(self, request, obj, form, change):
        if change and 'display_order' in form.changed_data:
            new_order = obj.display_order
            # Get the original instance from DB to access its old order
            original = self.model.objects.get(pk=obj.pk)
            # Use the swap method
            self.model.swap_display_order(original, new_order)
        else:
            super().save_model(request, obj, form, change)