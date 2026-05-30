# ISCC - Spec and Reference Code

[![License](https://img.shields.io/pypi/l/iscc.svg)](https://pypi.python.org/pypi/iscc/)
[![Downloads](https://pepy.tech/badge/iscc)](https://pepy.tech/project/iscc)
[![DOI](https://zenodo.org/badge/96668860.svg)](https://zenodo.org/badge/latestdoi/96668860)

| WARNING: The code and specs in this repository are an **out of date** early draft and retained for historic reasons only. For the current reference implementation see: [iscc-core](https://github.com/iscc/iscc-core). For status of specs see: [ISO/DIS 24138](https://www.iso.org/standard/77899.html). |
| --- |

The **International Standard Content Code** is a proposal for an [open standard](https://en.wikipedia.org/wiki/Open_standard) for decentralized content identification. This repository contains the specification of the proposed **ISCC Standard** and a reference implementation in Python3. The latest published version of the specification can be found at [iscc.codes](https://iscc.codes)

## Installing the reference code

The reference code is published with the package name [iscc](https://pypi.org/project/iscc/#history) on Python Package Index. Install the latest beta release with:

``` bash
pip install iscc==1.1.0b17
```

If your system is setup to compile c-extensions install with:

``` bash
pip install iscc[turbo]==1.1.0b17
```

This will install cython and build binary extansions for faster ISCC processing.

To install the required binaries for content extraction do:

```python
from iscc.bin import install
install()
```

## Using the reference code

A short example on how to create an ISCC Code with the reference implementation.

``` python
>>> import iscc
>>> iscc.code_iscc("README.md", all_granular=True)
{'version': '0-0-0',
 'iscc': 'KADYHLZUJ43U3LX7G7PNLS54JHAET3ANW4EQ3YQIP3LDAZHEYIS5GWI',
 'title': '# ISCC Spec and Reference Code',
 'filename': 'README.md',
 'filesize': 3840,
 'mediatype': 'text/markdown',
 'tophash': '00194e2c4e5570e637bd18667740fdcf7f1683d6ccace7f5c0cc6531f6e982e5',
 'metahash': '828dd01bf76b78fc448f6d2ab25008835d2993c6acde205235dc942083c4677d',
 'datahash': 'd63064e4c225d3594bdf60c30bcb04554e53059d9077a6f330f8295b4420ded5',
 'gmt': <GMT.text: 'text'>,
 'characters': 3457,
 'language': 'en',
 'features': [{'kind': <FeatureType.data: 'data'>,
               'version': 0,
               'features': ['7A23CQ3iCH4'],
               'sizes': [3840]},
              {'kind': <FeatureType.text: 'text'>,
               'version': 0,
               'features': ['Nt6V67hJxmk',
                            '9HvPYqt1rQw',
                            'ld1FLbp7A50',
                            'M8aTn6atuB0'],
               'sizes': [2340, 309, 292, 516]}]}
```

## Working with the specification

| NOTE: This is ISCC Version 1.1 - The specs are not yet updated!!! |
| --- |

The entire **ISCC Specification** is written in plain text [Markdown](https://en.wikipedia.org/wiki/Markdown). The Markdown content is built and published with [Zensical](https://zensical.org/). If you have basic command line skills you can build and run the specification site on your own computer. Make sure you have [git](https://git-scm.com/) and [Python](https://www.python.org/) installed on your system and follow these steps on the command line:

```bash
git clone https://github.com/iscc/iscc-codes.git
cd iscc-codes
python -m pip install zensical==0.0.43
zensical serve
```

All specification documents can be found in the `./docs` subfolder of the repository. The site configuration lives in `zensical.toml`.

## Contribute

Pull requests and other contributions are welcome. Use the [Github Issues](https://github.com/iscc/iscc-codes/issues) section of this project to discuss ideas for the **ISCC Specification**. You may also want  join our developer chat on Telegram at <https://t.me/iscc_dev>.

## License

All of documentation is licensed under the [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

Reference code is licensed under BSD-2-Clause.
