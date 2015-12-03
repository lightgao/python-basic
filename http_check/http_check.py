#!/usr/bin/python

import urllib2
import yaml
import boto.ec2.cloudwatch
import time
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description='Do http check')
parser.add_argument('-c','--configfile', help="The configuration file contains all urls need to check")
parser.add_argument('-n','--noreport', help='Will not report to cloudwatch', action="store_true", default=False)
args = parser.parse_args()

# Parse Config file
cfgfile = open(args.configfile)
configs = yaml.load(cfgfile)

# use to send metrics to cloudwatch
def post_metric(name, value):
    str = "%s: %s reports %s with %d" % (time.strftime("%Y-%m-%d %H:%M:%S %Z",time.localtime()), configs['reporter'], name, value)
    # if args.noreport == False:
        # c = boto.ec2.cloudwatch.connect_to_region(configs['region'])
        # c.put_metric_data(namespace=configs['namespace'], name=name, value=value, dimensions={'Reporter':configs['reporter']})
    print (str)

# Check each services
for k,v in configs['services'].items():
    try:
        check_url = v['url'] + v['check_path']
        response = urllib2.urlopen( check_url, timeout=v['timeout'] )
        post_metric(v['name'], 1.0)
    except Exception, e:
        post_metric(v['name'], 0.0)
