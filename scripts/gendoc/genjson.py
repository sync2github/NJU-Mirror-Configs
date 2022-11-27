from typing import List, Dict
import os
import json


def get_target_path(cur_path, target_dir):
    base_path = '/'.join(cur_path.split('/')[:-2])
    target_path = os.path.join(base_path, target_dir)
    return target_path


if __name__ == '__main__':
    res: List[Dict[str, str]] = []
    cur_path = os.path.dirname(__file__)
    target_path = get_target_path(cur_path, 'documentations')
    for file in os.listdir(target_path):
        if file[-3:] == '.md':
            path = file
            name = file[:-3].split('-')[3:]
            name = '-'.join(name)
            res.append({'name': name, 'path': path, 'route': name})
    res.sort(key=lambda d: d['name'].lower())
    with open(os.path.join(target_path, 'index.json'), 'w') as f:
        json.dump(res, f, indent=4)
