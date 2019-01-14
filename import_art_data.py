import json
import requests
import numpy as np
import pandas as pd
import sys
import os
from pathlib import Path

def import_data(df, con, id):
    df.loc[df['id'] == id, 'medium'] = con['medium']
    df.loc[df['id'] == id, 'classification'] = con['classification']
    df.loc[df['id'] == id, 'dated'] = con['dated']
    df.loc[df['id'] == id, 'style'] = con['style']
    return df
    
def get_data(df, ids, try_again):
    for id in ids:
        res = requests.get(f'https://search.artsmia.org/id/{id}')
        if res.status_code in [200, 201]:
            con = json.loads(res.content)
            df = import_data(df, con, id)
        else:
            try_again.append(id)
    
    return df, try_again

def main(argv):
    dir = Path(os.getcwd())
    art_df = pd.read_csv(dir/argv[0])
    art_df['medium'] = np.nan
    art_df['classification'] = np.nan
    art_df['dated'] = np.nan
    art_df['style'] = np.nan

    ids = list(art_df['id'])
    try_again = []

    art_df, try_again = get_data(art_df, ids, try_again)

    failed_ids = []
    if len(try_again) > 0:
        art_df, failed_ids = get_data(art_df, try_again, failed_ids)

    art_df.to_csv(dir/argv[1], index=False)

    for id in failed_ids:
        print(f'Request for id {id} failed')

if __name__ == "__main__":
    main(sys.argv[1:])