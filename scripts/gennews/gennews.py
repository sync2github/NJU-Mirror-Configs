import re
import json
import os
import datetime

FILE_REG = re.compile(r'(\d{4})\-(\d{2})\-(\d{2})-(.+).md')


def get_target_path(cur_path, target_dir):
    base_path = '/'.join(cur_path.split('/')[:-2])
    target_path = os.path.join(base_path, target_dir)
    return target_path


if __name__ == '__main__':
    entries = []
    cur_path = os.path.dirname(__file__)
    target_path = get_target_path(cur_path, 'news')
    for file in os.listdir(target_path):
        if (m := FILE_REG.match(file)) != None:
            y, m, d, name = m.groups()
            date = datetime.datetime(int(y), int(m), int(d))
            entries.append({
                "name": name,
                "time": date.timestamp(),
                "content": file
            })
    entries.sort(key=lambda d: d['time'], reverse=True)
    with open(os.path.join(target_path, 'index.json'), 'w') as f:
        json.dump(entries, f, indent=4)
