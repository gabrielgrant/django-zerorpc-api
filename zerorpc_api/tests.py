#!/usr/bin/env python

from django.utils import unittest
from django.test import TestCase
from django.contrib.auth.models import User

import adapter

class ZeroRPCTests(TestCase):
    pass

class AdapterTests(TestCase):
    def test_get(self):
        u = User.objects.create_user('name', 'em@il.com', 'pass')
        u.save()
        print adapter.get('auth.User', {'username': 'name'})
    def test_query(self):
        u1 = User.objects.create_user('name1', 'em@il.com', 'pass')
        u1.save()
        u2 = User.objects.create_user('name2', 'em@il.com', 'pass')
        u2.save()
        u3 = User.objects.create_user('3name', 'em@il.com', 'pass')
        u3.save()
        adapter.query('auth.User', [
            {'type': 'filter', 'params': {'username__startswith': 'name'}},
        ])
        adapter.query('auth.User', [
            {'type': 'exclude', 'params': {'username__endswith': '1'}},
            {'type': 'exclude', 'params': {'username__endswith': '2'}},
        ])
        print adapter.query('auth.User', [
            {'type': 'filter', 'params': {'username__startswith': 'name'}},
            {'type': 'exclude', 'params': {'username__endswith': '1'}},
        ])
