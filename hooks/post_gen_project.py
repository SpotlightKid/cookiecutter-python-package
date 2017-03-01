#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Init git repository and add remote repo as origin."""

from subprocess import call

origin_url = "{{ cookiecutter.repo_url }}"

call(['git', 'init'])
call(['git', 'remote', 'add', 'origin', origin_url])
