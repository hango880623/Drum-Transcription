# Drum Transcription API
## _Convert drum to midi_

- [Drum Transcription API](#drum-transcription-api)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
    - [Installation for development](#installation-for-development)
    - [Installation for production](#installation-for-production)
  - [Run the API](#run-the-api)

## Features

- Upload audio file(.wav)
- Drum to midi
- Web demo page

## Requirements

- OS: Ubuntu 20.04 x86_64 (It might also work on 18.04)
- Python >= 3.5
- flask 2.0.1
- Werkzeug 2.0.1
- magenta
- gsutil

## Installation

Clone the repository:

```bash
$ git clone https://github.com/hango880623/Drum-Transcription.git
```

### Installation for development

Install:

- [Anaconda](https://docs.anaconda.com/anaconda/install/linux/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html#linux-installers)

Install packages:
If you are running Mac OS X or Ubuntu, you can try using our automated installation script. Just paste the following command into your terminal.

```bash
$ curl https://raw.githubusercontent.com/tensorflow/magenta/main/magenta/tools/magenta-install.sh > /tmp/magenta-install.sh
$ bash /tmp/magenta-install.sh
```
After the script completes, open a new terminal window so the environment variable changes take effect.

The Magenta libraries are now available for use within Python programs and Jupyter notebooks, and the Magenta scripts are installed in your path!

**NOTE:** You will need to run `source activate magenta` to use Magenta every time you open a new terminal window:
### Installation for production
```bash
$ source activate magenta
$ (magenta) pip install magenta
$ (magenta) pip install flask
$ (magenta) pip install Werkzeug
```

Download the model check points from Google Cloud using gsutil
```bash
rm -r /content/onsets-frames
mkdir /content/onsets-frames
gsutil -q -m cp -R gs://magentadata/models/onsets_frames_transcription/*checkpoint*.zip /content/onsets-frames/
unzip -o /content/onsets-frames/maestro_checkpoint.zip -d /content/onsets-frames/maestro
unzip -o /content/onsets-frames/e-gmd_checkpoint.zip -d /content/onsets-frames/e-gmd
```
## Run the API
Run the API on local machine http://127.0.0.1:5000/
```bash
$ (magenta) python onsetsandframes.py
```
