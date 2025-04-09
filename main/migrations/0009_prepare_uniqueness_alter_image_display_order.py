# In a new file: migrations/0002_fix_duplicate_display_orders.py
from django.db import migrations


def fix_duplicate_display_orders(apps, schema_editor):
    """Fixes any duplicate display_order values by incrementing them"""
    # Get the model dynamically (works in migrations)
    Image = apps.get_model('main', 'Image')
    Play = apps.get_model('main', 'Play')
    Video = apps.get_model('main', 'Video')
    models = [Image, Play, Video]
    for model in models:
        # Get all items ordered by display_order
        items = list(model.objects.order_by('display_order'))

        # Track seen orders to find duplicates
        seen_orders = {}
        max_order = 0

        for item in items:
            if item.display_order in seen_orders or item.display_order == 0:
                # Found a duplicate, increment max_order and use it
                max_order += 1
                item.display_order = max_order
                item.save(update_fields=['display_order'])
            else:
                # No duplicate, just track it
                seen_orders[item.display_order] = True
                max_order = max(max_order, item.display_order)


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0008_alter_image_display_order_alter_play_display_order_and_more'),  # Adjust to your previous migration
    ]

    operations = [
        migrations.RunPython(fix_duplicate_display_orders),
    ]