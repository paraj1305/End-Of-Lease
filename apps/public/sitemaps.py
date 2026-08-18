from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticPagesSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return ['public:home', 'public:services', 'public:about', 'public:contact', 'public:faq', 'bookings:step_1_package']

    def location(self, item):
        return reverse(item)
