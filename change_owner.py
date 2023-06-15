import datetime, math, time
from KalturaClient import *
from KalturaClient.Plugins.Core import *

def main():
    client = get_client()

    entry_list = open('change_owner.txt', 'r')

    for entry in entry_list:
        entry_id, userId = entry.split("\t")
        base_entry = KalturaBaseEntry()
        base_entry.userId = userId
        change_owner(client, entry_id, base_entry)

    entry_list.close()


def change_owner(client, entry_id, userId):
    try:
        result = client.baseEntry.update(entry_id, userId);
        print(entry_id,"owner changed");

    except Exception as e:
    	print(e)


def get_client():
    config = KalturaConfiguration()
    config.serviceUrl = "https://admin.kaltura.com/"
    client = KalturaClient(config)

    ks = client.session.start(
      "[KALTURAKEY]",
      None,
      KalturaSessionType.ADMIN,
      [PID],
      432000,
	"appID:change-owner"
      )
    client.setKs(ks)

    return client

main()
