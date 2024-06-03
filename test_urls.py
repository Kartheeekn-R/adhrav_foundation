# test_urls.py
from django.urls import reverse

def test_urls():
    try:
        print(reverse('home'))     # Should print: /disk/home/
        print(reverse('about'))    # Should print: /disk/about/
        print(reverse('causes'))   # Should print: /disk/causes/
        print(reverse('contact'))  # Should print: /disk/contact/
        print(reverse('gallery'))  # Should print: /disk/gallery/
    except Exception as e:
        print(f"Error: {e}")

test_urls()
