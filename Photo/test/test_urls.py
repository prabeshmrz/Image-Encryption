from django.urls import reverse, resolve


def test_index_urls():
    path = reverse('index')
    assert resolve(path).view_name == 'index'


def test_decrypt_urls():
    path = reverse('decrypt', kwargs={'i': 1})
    assert resolve(path).view_name == 'decrypt'
