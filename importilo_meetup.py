import requests

#ekzempla evento
# url = 'https://www.meetup.com/Esperanto-Calgary/events/qnqmgpybckbbc/'


def importas_el_meetup(url):
    evento = {}

    idx = url.split('/')

    grupo = idx[3]
    id = idx[5]

    res = requests.get(f"https://api.meetup.com/{grupo}/events/{id}")
    res_json = res.json()
    if res.status_code != 200:
        code = res_json['errors'][0]['code']
        message = res_json['errors'][0]['message']
        retrokuplo = f"{code} {message}"

        if res.status_code == 404:
            if code == 'event_error' and message == 'invalid event':
                retrokuplo = f"evento '{id}' ne ekzistas"
            elif code == 'group_error' and message.startswith('Invalid group urlname'):
                retrokuplo = f"grupo '{grupo}' ne ekzistas"

        return f"importado ne sukcesis: {retrokuplo}"

    evento['titolo'] = grupo + ': ' + res_json['name']
    evento['urbo'] = res_json['venue']['city']
    evento['ligilo'] = res_json['link']
    evento['landa_id'] = res_json['venue']['country']
    evento['latitudo'] = res_json['venue']['lat']
    evento['longitudo'] = res_json['venue']['lon']
    evento['adreso'] = f"{res_json['venue']['name']}, {res_json['venue']['address_1']}"
    evento['horzono'] = res_json['group']['timezone']
    evento['komenco'] = res_json['local_date'] + ' ' + res_json['local_time']
    # evento['fino']    = Time.at((res_json['time'].to_i + res_json['duration'].to_i) / 1000).in_time_zone(evento['time_zone']).strftime("%Y-%m-%d %H:%M:%S")
    evento['kontento'] = res_json['description'] # + res.fetch('_find_us', '')
    evento['priskribo'] = res_json['name']


    return evento

