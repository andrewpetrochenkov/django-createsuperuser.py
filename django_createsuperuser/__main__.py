#!/usr/bin/env python
"""create/update a superuser with password"""
# -*- coding: utf-8 -*-
import click
import django

"""
export DJANGO_SETTINGS_MODULE=settings
python -m createsuperuser "admin" "password"
python -m createsuperuser "admin" "password" foo@foo.foo
"""

MODULE_NAME = "django_createsuperuser"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s username password [email]' % MODULE_NAME


@click.command()
@click.argument('username')
@click.argument('password')
@click.argument('email',required=False)
def _cli(username,password,email=None):
    django.setup()
    from django.contrib.auth.models import User
    user, created = User.objects.get_or_create(username=username)
    user.set_password(password)
    if email:
        user.email = email
    user.save()

if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
