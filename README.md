পোল এ্যাপ ডেমো 
===========

অনলাইন পোল প্রোজেক্টটি  পাইথন এর জ্যাঙ্গো ফ্রেমওআর্ক দিয়ে বানানো একটি ছোট্ট প্রোজেক্ট। আবু আশরাফ মাসনুন ভাই এর ধারাবাহিক (জ্যাঙ্গো টিওটোরিয়াল)[https://github.com/masnun/django-bangla-book] এবং জ্যাঙ্গোর অফিসিয়াল সাইট থেকে অনুপ্রানিত হয়ে মুলত এটি ডেভেলপ করা হয়েছে। এর কাজ খুব সাধারন। 
ব্যাবহারকারী হোম পেজ থেকে একটি পোল সিলেক্ট করবে এবং এর যেকোনো একটি অপশন সিলেক্ট করে ভোট দেবে। ভোট দেওয়া শেষ হলে ব্যাবহারকারী সাথে সাথে একটি নতুন পেজে রিডাইরেক্টেড হবে এবং সেখানে ভোটের ফলাফল প্রদর্শিত হবে। 

নতুন পোল তৈরি করা, পোলে অপশন যোগ করা, পোল এডিট এবং ডিলিট করার জন্য জ্যাঙ্গোর এ্যাডমিন এ্যাপটি ব্যাবহার করে সেখানে পোল এ্যাপটি হুক করা হয়েছে (টিউটোরিয়াল দ্রষ্টব্য)।

প্রজেক্টটির পোল এ্যাপ এবং এ্যাডমিন এ্যাপে টুইটার বুট স্ট্রাপড থিম ব্যাবহার করা হয়েছে। এ্যাডমিন এ্যপে এটি ব্যাবহার করার পুর্বে থিমটি ডাউনলোড করে নিতে হবে। ডাউনলোড করার জন্য টারমিনালে গিয়ে লিখতে হবে `pip install django-admin-bootstrapped` এবং settings.py ফাইলে INSTALLED_APPS এর `django.contrib.admin` এর পুর্বে গিয়ে লিখতে হবে `django_admin_bootstrapped` ।


