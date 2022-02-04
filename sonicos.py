import csv
import pprint

import SonicOS


def main():
    s = SonicOS.SonicAPI('<your_firewall_hostname>', <your_firewall_port>, '<your_firewall_user>', '<your_firewall_password>')
    res1 = s.auth()
    # print(res1)

    #############################################################
    #                       address objects                     #
    #############################################################
    with open('output/address_obj.csv', 'w') as output:
        res = s.getIPv4AddressObjects()
        # pprint.pprint(res, output)
        csv_writer = csv.writer(output, lineterminator='\n')
        header = ['name', 'ip', 'zone', 'subnet', 'mask']
        csv_writer.writerow(header)

        for obj in res['address_objects']:
            ip = ''
            name = ''
            zone = ''
            subnet = ''
            mask = ''
            obj_s = obj['ipv4']

            if 'name' in obj_s.keys():
                name = obj_s['name']
            if 'host' in obj_s.keys():
                if 'ip' in obj_s['host'].keys():
                    ip = obj_s['host']['ip']
            if 'zone' in obj_s.keys():
                zone = obj_s['zone']
            if 'network' in obj_s.keys():
                if 'subnet' in obj_s['network'].keys():
                    subnet = obj_s['network']['subnet']
            if 'network' in obj_s.keys():
                if 'mask' in obj_s['network'].keys():
                    mask = obj_s['network']['mask']
            row = (name, ip, zone, subnet, mask)
            csv_writer.writerow(row)

    #############################################################
    #                       address groups                      #
    #############################################################
    with open('output/address_group_obj.csv', 'w') as output_1:
        res = s.getIPv4AddressGroupsObjects()
        # pprint.pprint(res, output_1)
        csv_writer = csv.writer(output_1, lineterminator='\n')
        header = ['group_name', 'subnets']
        csv_writer.writerow(header)

        for obj in res['address_groups']:
            group_name = ''
            uuid = ''
            subnets = ''
            obj_s = obj['ipv4']

            if 'name' in obj_s.keys():
                group_name = obj_s['name']
            if 'address_object' in obj_s.keys():
                if 'ipv4' in obj_s['address_object'].keys():
                    first = True
                    for name in obj_s['address_object']['ipv4']:
                        if first:
                            subnets += "{0}".format(name['name'])
                            first = False
                        else:
                            subnets += ", {0}".format(name['name'])
            elif 'address_group' in obj_s.keys():
                if 'ipv4' in obj_s['address_group'].keys():
                    first = True
                    for name in obj_s['address_group']['ipv4']:
                        if first:
                            subnets += "{0}".format(name['name'])
                            first = False
                        else:
                            subnets += ", {0}".format(name['name'])

            row = (group_name, subnets)
            csv_writer.writerow(row)

    #############################################################
    #                       Service objects                     #
    #############################################################
    with open('output/service_obj.csv', 'w') as output_2:
        res = s.getServiceObjects()
        # pprint.pprint(res, output_2)
        csv_writer = csv.writer(output_2, lineterminator='\n')
        header = ['name', 'tcp/udp', 'begin', 'end']
        csv_writer.writerow(header)

        for obj in res['service_objects']:
            name = ''
            tcp_udp = ''
            begin = ''
            end = ''

            if 'name' in obj.keys():
                name = obj['name']

            if 'tcp' in obj.keys():
                for key, value in obj.items():
                    if key == 'tcp':
                        tcp_udp = key
                if 'begin' in obj['tcp'].keys():
                    begin = obj['tcp']['begin']
                if 'end' in obj['tcp'].keys():
                    end = obj['tcp']['end']
            elif 'udp' in obj.keys():
                for key, value in obj.items():
                    if key == 'udp':
                        tcp_udp = key
                if 'begin' in obj['udp'].keys():
                    begin = obj['udp']['begin']
                if 'end' in obj['udp'].keys():
                    end = obj['udp']['end']

            row = (name, tcp_udp, begin, end)
            csv_writer.writerow(row)

    #############################################################
    #                   Service Group objects                   #
    #############################################################
    with open('output/service_group_obj.csv', 'w') as output_3:
        res = s.getServiceGroupObjects()
        # pprint.pprint(res, output_3)
        csv_writer = csv.writer(output_3, lineterminator='\n')
        header = ['name', 'service_group', 'service_object']
        csv_writer.writerow(header)

        for obj in res['service_groups']:
            srv_group_name = ''
            service_group = ''
            service_object = ''

            if 'name' in obj.keys():
                srv_group_name = obj['name']

            if 'service_group' in obj.keys():
                first = True
                for name in obj['service_group']:
                    if first:
                        service_group += "{0}".format(name['name'])
                        first = False
                    else:
                        service_group += ", {0}".format(name['name'])
            if 'service_object' in obj.keys():
                first = True
                for name in obj['service_object']:
                    if first:
                        service_object += "{0}".format(name['name'])
                        first = False
                    else:
                        service_object += ", {0}".format(name['name'])

            row = (srv_group_name, service_group, service_object)
            csv_writer.writerow(row)

    #############################################################
    #                       NAT Policies                        #
    #############################################################
    with open('output/NAT_policies.csv', 'w') as output_4:
        res = s.getIP4NATPol()
        # pprint.pprint(res, output_4)
        csv_writer = csv.writer(output_4, lineterminator='\n')
        header = ['enable',
                  'name',
                  'source',
                  'destination',
                  'inbound',
                  'outbound',
                  'service',
                  'translated_source',
                  'translated_destination',
                  'translated_service',
                  'comment']
        csv_writer.writerow(header)

        for obj in res['nat_policies']:
            enable = ''
            name = ''
            source = ''
            destination = ''
            inbound = ''
            outbound = ''
            service = ''
            translated_source = ''
            translated_destination = ''
            translated_service = ''
            comment = ''
            obj_s = obj['ipv4']

            if 'enable' in obj_s.keys():
                enable = obj_s['enable']
            if 'name' in obj_s.keys():
                name = obj_s['name']
            if 'source' in obj_s.keys():
                source_dict = obj_s['source']
                if 'any' in source_dict.keys():
                    source = "any"
                elif 'name' in source_dict.keys():
                    source = source_dict['name']
            if 'destination' in obj_s.keys():
                destination_dict = obj_s['destination']
                if 'any' in destination_dict.keys():
                    source = "any"
                elif 'name' in destination_dict.keys():
                    source = destination_dict['name']
            if 'inbound' in obj_s.keys():
                inbound = obj_s['inbound']
            if 'outbound' in obj_s.keys():
                outbound = obj_s['outbound']
            if 'service' in obj_s.keys():
                service_dict = obj_s['service']
                if 'group' in service_dict.keys():
                    service = "group - " + service_dict['group']
                elif 'name' in service_dict.keys():
                    service = service_dict['name']
            if 'translated_source' in obj_s.keys():
                translated_source_dict = obj_s['translated_source']
                if 'name' in translated_source_dict.keys():
                    translated_source = translated_source_dict['name']
                elif 'original' in translated_source_dict.keys():
                    translated_source = 'original'
            if 'translated_destination' in obj_s.keys():
                translated_destination_dict = obj_s['translated_destination']
                if 'name' in translated_destination_dict.keys():
                    translated_destination = translated_destination_dict['name']
                elif 'original' in translated_destination_dict.keys():
                    translated_destination = 'original'
            if 'translated_service' in obj_s.keys():
                translated_service_dict = obj_s['translated_service']
                if 'name' in translated_service_dict.keys():
                    translated_service = translated_service_dict['name']
                elif 'original' in translated_service_dict.keys():
                    translated_service = 'original'
                elif 'group' in translated_service_dict.keys():
                    translated_service = 'group - ' + translated_service_dict['group']
            if 'comment' in obj_s.keys():
                comment = obj_s['comment']

            row = (enable,
                   name,
                   source,
                   destination,
                   inbound,
                   outbound,
                   service,
                   translated_source,
                   translated_destination,
                   translated_service,
                   comment)
            csv_writer.writerow(row)

    #############################################################
    #                       Access Rules                        #
    #############################################################
    with open('output/access_rules.csv', 'w') as output:
        res = s.getIPV4AccessRules()
        # pprint.pprint(res, output)
        csv_writer = csv.writer(output, lineterminator='\n')
        header = ['action', 'enable', 'from_zone', 'to_zone', 'source', 'destination', 'service', 'name', 'comment']
        csv_writer.writerow(header)

        for obj in res['access_rules']:
            action = ''
            enable = ''
            from_zone = ''
            to_zone = ''
            source = ''
            destination = ''
            service = ''
            name = ''
            comment = ''
            obj_s = obj['ipv4']

            if 'action' in obj_s.keys():
                action = obj_s['action']
            if 'enable' in obj_s.keys():
                enable = obj_s['enable']
            if 'from' in obj_s.keys():
                from_zone = obj_s['from']
            if 'to' in obj_s.keys():
                to_zone = obj_s['to']
            if 'source' in obj_s.keys():
                if 'any' in obj_s['source']['address'].keys():
                    source = 'any'
                elif 'name' in obj_s['source']['address'].keys():
                    source = obj_s['source']['address']['name']
                elif 'group' in obj_s['source']['address'].keys():
                    source = 'group - ' + obj_s['source']['address']['group']
            if 'destination' in obj_s.keys():
                if 'group' in obj_s['destination']['address'].keys():
                    destination = 'group - ' + obj_s['destination']['address']['group']
                elif 'any' in obj_s['destination']['address'].keys():
                    destination = 'any'
                elif 'name' in obj_s['destination']['address'].keys():
                    destination = obj_s['destination']['address']['name']
            if 'service' in obj_s.keys():
                if 'group' in obj_s['service'].keys():
                    service = 'group - ' + obj_s['service']['group']
                elif 'name' in obj_s['service'].keys():
                    service = obj_s['service']['name']
            if 'name' in obj_s.keys():
                name = obj_s['name']
            if 'comment' in obj_s.keys():
                comment = obj_s['comment']

            row = (action, enable, from_zone, to_zone, source, destination, service, name, comment)
            csv_writer.writerow(row)

    #############################################################
    #                       static routes                       #
    #############################################################
    with open('output/static_routes.csv', 'w') as output:
        res = s.getIPV4RoutePolicies()
        # pprint.pprint(res, output)
        csv_writer = csv.writer(output, lineterminator='\n')
        header = ['name', 'source', 'destination', 'gateway', 'interface', 'service', 'metric', 'comment']
        csv_writer.writerow(header)

        for obj in res['route_policies']:
            name = ''
            source = ''
            destination = ''
            gateway = ''
            interface = ''
            service = ''
            metric = ''
            comment = ''
            obj_s = obj['ipv4']

            if 'name' in obj_s.keys():
                name = obj_s['name']
            if 'source' in obj_s.keys():
                if 'any' in obj_s['source']:
                    source = 'any'
                elif 'name' in obj_s['source']:
                    source = obj_s['source']['name']
                elif 'group' in obj_s['source']:
                    source = 'group - ' + obj_s['source']['group']
            if 'destination' in obj_s.keys():
                if 'any' in obj_s['destination']:
                    destination = 'any'
                elif 'name' in obj_s['destination']:
                    destination = obj_s['destination']['name']
                elif 'group' in obj_s['destination']:
                    destination = 'group - ' + obj_s['destination']['group']
            if 'gateway' in obj_s.keys():
                if 'default' in obj_s['gateway']:
                    gateway = obj_s['gateway']['default']
                elif 'name' in obj_s['gateway']:
                    gateway = obj_s['gateway']['name']
                elif 'group' in obj_s['gateway']:
                    gateway = 'group - ' + obj_s['gateway']['group']
            if 'service' in obj_s.keys():
                if 'any' in obj_s['service']:
                    service = 'any'
                elif 'name' in obj_s['service']:
                    service = obj_s['service']['name']
                elif 'group' in obj_s['service']:
                    service = 'group - ' + obj_s['service']['group']
            if 'metric' in obj_s.keys():
                name = obj_s['metric']
            if 'comment' in obj_s.keys():
                comment = obj_s['comment']

            row = (name, source, destination, gateway, interface, service, metric, comment)
            csv_writer.writerow(row)


if __name__ == "__main__":
    main()
