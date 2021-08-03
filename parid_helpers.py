import selenium_helpers

# These functions allow us to loop through our text file of parcel ID's and update the list after each ID is consumed

filename_ids = 'test.txt'

# Save a list of parcel ID's as a text file
def save_list(parid_list, filename):
    parid_list = '\n'.join(parid_list)
    with open(filename, 'w') as f:
        f.write(parid_list)
    
    
# Restore a text file of parcel ID's into a list in Python
def restore_list(filename):
    with open(filename, 'r') as f:
        parid_list = f.read()
    parid_list = parid_list.split('\n')
    parid_list = [x.strip() for x in parid_list]
    return parid_list


# Save a copy of tax, appraised, and assessed value information for a parcel ID
def consume_parids():
    done = False
    while not done:
        parids = restore_list(filename_ids)
        parid = parids[0]
        parids = parids[1:]
        
        selenium_helpers.scrape_chatham(parid)
        
        save_list(parids, filename_ids)
        if not parids:
            print('All Parcel IDs consumed')
            done = True