import json
all_contacts = []


def backup_contacts():
    # Writing contact to a JSON file
    with open('all_contacts.json', 'w') as json_file:
        json.dump(all_contacts, json_file, indent=4)

    print('Contacts data are backuped!')


def restore_contacts():

    # Data restoring for contacts

    try:
        all_contacts.clear()

        with open('all_contacts.json', 'r') as json_file:
            contacts = json.load(json_file)
            for data in contacts:
                all_contacts.append(data)

        print('Contacts restored successfully!')

    except:
        print('File refreshed!')
