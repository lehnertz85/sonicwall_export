import requests
from collections import OrderedDict
import json


class SonicAPI:
    def __init__(self, hostname, port, username, password):
        self.baseurl = 'https://{0}:{1}/api/sonicos/'.format(hostname, str(port))
        self.authinfo = (username, password)
        self.headers = OrderedDict([
            ('Accept', 'application/json'),
            ('Content-Type', 'application/json'),
            ('Accept-Encoding', 'application/json'),
            ('charset', 'UTF-8')])

    def auth(self):
        controller = 'auth'
        url = self.baseurl + controller
        r = requests.post(url, auth=self.authinfo, headers=self.headers, verify=False)
        if r.status_code != 200:
            return r.status_code
        else:
            response = r.json()
            return response

    def getIPv4AddressObjects(self):
        controller = 'address-objects/ipv4'
        url = self.baseurl + controller
        r = requests.get(url, auth=self.authinfo, headers=self.headers, verify=False)
        if r.status_code != 200:
            return r.status_code
        else:
            response = r.json()
            return response

    def getIPv4AddressGroupsObjects(self):
        controller = 'address-groups/ipv4'
        url = self.baseurl + controller
        r = requests.get(url, auth=self.authinfo, headers=self.headers, verify=False)
        if r.status_code != 200:
            return r.status_code
        else:
            response = r.json()
            return response

    def getServiceObjects(self):
        controller = 'service-objects'
        url = self.baseurl + controller
        r = requests.get(url, auth=self.authinfo, headers=self.headers, verify=False)
        if r.status_code != 200:
            return r.status_code
        else:
            response = r.json()
            return response

    def getServiceGroupObjects(self):
        controller = 'service-groups'
        url = self.baseurl + controller
        r = requests.get(url, auth=self.authinfo, headers=self.headers, verify=False)
        if r.status_code != 200:
            return r.status_code
        else:
            response = r.json()
            return response

    def getIP4NATPol(self):
        controller = 'nat-policies/ipv4'
        url = self.baseurl + controller
        r = requests.get(url, auth=self.authinfo, headers=self.headers, verify=False)
        if r.status_code != 200:
            return r.status_code
        else:
            response = r.json()
            return response

    def getIPV4AccessRules(self):
        controller = 'access-rules/ipv4'
        url = self.baseurl + controller
        r = requests.get(url, auth=self.authinfo, headers=self.headers, verify=False)
        if r.status_code != 200:
            return r.status_code
        else:
            response = r.json()
            return response

    def getIPV4RoutePolicies(self):
        controller = 'route-policies/ipv4'
        url = self.baseurl + controller
        r = requests.get(url, auth=self.authinfo, headers=self.headers, verify=False)
        if r.status_code != 200:
            return r.status_code
        else:
            response = r.json()
            return response
