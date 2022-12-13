# NJU Mirror Configs

> Configurations for [NJU Open Source Software Mirror](https://mirrors.nju.edu.cn/).

## How to Contribute

### Mirror Documentations

```
usage: Mira documentations list generator [-h] [-d DIR]

Generate documentations list for Mira

optional arguments:
  -h, --help         show this help message and exit
  -d DIR, --dir DIR  Specify the directory which contains documentations. Default value is
                     `./documentations`.
```

1. Fork this repository.
2. Place your new mirror documentation by putting your `*.md` file in `/documentations/`. A sample file is
   as follows:
   > Filename: `2021-13-37-flatter.md`  
   > Content:
   > ```markdown
   > ## Flatter 镜像安装帮助
   > 
   > 阿巴阿巴
   > 
   > ### 歪比巴卜
   > 
   > ...
   > ```
3. Add your new documentation and its route to `index.json` by running `scripts/gendoc/genjson.py` with documentations path specified such as `python genjson.py -d ../../documentations`. This will generate a new `index.json`.
4. Create a merge/pull request to let us know.

You can preview this project on [https://iori2333.github.io/Mira](https://iori2333.github.io/Mira/).

### Mirror News
```
usage: Mira news list generator [-h] [-d DIR]

Generate news list for Mira

optional arguments:
  -h, --help         show this help message and exit
  -d DIR, --dir DIR  Specify the directory which contains news. Default value is current work directory.
```

1. Fork this repository
2. Place the `*.md` news document in `/news/`. The filename of your document must match `<yyyy>-<mm>-<dd>-<title>.md`, for example, `2021-13-37-SomeNews.md`.
3. Run `scripts/gennews/gennews.py` with news path specified such as `python gennews.py -d ../../news`. This will generate a new `index.json`.
4. Create a merge/pull request to let us know.

### Mirror Download List

```
usage: Mira download list generator [-h] [-d DIR] [-R REMOTE] [-T [TEST ...]]

Generate download list for Mira

optional arguments:
  -h, --help            show this help message and exit
  -d DIR, --dir DIR     Override root directory.
  -R REMOTE, --remote REMOTE
                        [Remote Mode] Using rsync to get file list instead of reading from INI. Need the
                        base of target site, for example, `mirror.nju.edu.cn`.
  -T [TEST ...], --test [TEST ...]
                        Test specified `distro`s (multiple arguments input is supported) in INI. If Remote
                        Mode is on, `distro`s must be specified in case of heavy rsync job.
```

1. Fork this repository
2. Edit `genisolist.ini`, add, modify or remove items.
3. **(Linux Only)** After modification, run the scripts for a quick test: ` python genisolist.py -R <mirror-site-base> -T <items-you-want-to-test>`. 
4. If the test is passed, create a merge/pull request to let us know.

Exmaple:
```
python genisolist.py -R mirror.nju.edu.cn -T Ventoy "Office Tool Plus"
```

Output:
```
[RSync] mirror.nju.edu.cn/github-release/ventoy/Ventoy/
[RSync] mirror.nju.edu.cn/github-release/YerongAI/Office-Tool/
[
  {
    "distro": "Ventoy",
    "category": "app",
    "urls": [
      {
        "name": "1.0.84 (windows, zip)",
        "url": "/Ventoy 1.0.84 release/ventoy-1.0.84-windows.zip"
      },
      {
        "name": "1.0.84 (livecd, iso)",
        "url": "/Ventoy 1.0.84 release/ventoy-1.0.84-livecd.iso"
      },
      {
        "name": "1.0.84 (linux, tar.gz)",
        "url": "/Ventoy 1.0.84 release/ventoy-1.0.84-linux.tar.gz"
      }
    ]
  },
  {
    "distro": "Office Tool Plus",
    "category": "app",
    "urls": [
      {
        "name": "9.0.3.7 (Windows, with_runtime zip)",
        "url": "/Office Tool Plus v9.0.3.7/Office_Tool_with_runtime_v9.0.3.7.zip"
      },
      {
        "name": "9.0.3.7 (Windows, with_runtime exe)",
        "url": "/Office Tool Plus v9.0.3.7/Office_Tool_with_runtime_v9.0.3.7.exe"
      },
      {
        "name": "9.0.3.7 (Windows, with_runtime 7z)",
        "url": "/Office Tool Plus v9.0.3.7/Office_Tool_with_runtime_v9.0.3.7.7z"
      },
      {
        "name": "9.0.3.7 (Windows,  zip)",
        "url": "/Office Tool Plus v9.0.3.7/Office_Tool_v9.0.3.7.zip"
      }
    ]
  }
]
```