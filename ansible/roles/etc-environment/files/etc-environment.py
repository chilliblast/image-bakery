#!/usr/bin/env python

import os
import boto3
import yaml

env_vars = {}

with open('/var/lib/cloud/instance/user-data.txt') as f:
  user_data = yaml.load(f)
  if user_data is not None and user_data.has_key('environment'):
    for k, v in user_data['environment'].iteritems():
      env_vars[k.upper()]=v

with open('/etc/environment', 'a+') as f:
  for k, v in env_vars.iteritems():
    f.writelines("%s=%s\n" % (k, v))
