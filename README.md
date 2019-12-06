# UPDATE
The competition concluded 24 Oct 2019. While this repo will persist, the competition website has been taken offline.

# Machine Learning Static Evasion Competition

This repo contains code to be used in conjunction with the [Machine Learning Static Evasion Competition](https://evademalwareml.io/).  To participate, you must [register here](https://evademalwareml.io/). This repo is intended to assist contestants in constructing a white-box attack, by providing model weights and inference code.

## Models

This competition contains three trained models
1. [MalConv](https://arxiv.org/pdf/1710.09435.pdf) trained on EMBER 2018 binaries
2. [Non-negative MalConv](https://arxiv.org/pdf/1806.06108.pdf) trained on EMBER 2018 binaries.
3. A [LightGBM](https://lightgbm.readthedocs.io/en/latest/) model trained on the [EMBER 2018 features dataset](https://github.com/EndgameInc/ember)

## Getting Started

### Pre-requisites
The model evaluation code requires Python 3.6. ([LIEF](https://github.com/lief-project/LIEF) is not easily installed with Python 3.7, so Python 3.6 is recommended.) A [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or Anaconda environment is recommended.

1. Follow the [installation instructions](https://github.com/endgameinc/ember/blob/master/README.md) for EMBER.
2. [Install pytorch](https://pytorch.org/) for Python 3.6 on your platform


### Predicting with models
1. Checkout this repository and unzip compressed LightGBM model
```git clone https://github.com/endgameinc/malware_evasion_competition.git
cd malware_evasion_competition
pushd models/ember && unzip ember_model.txt.zip && popd
```

2. Evaluate the models on a sample via the command-line
```python3 models.py some.exe```

### White-box attack
It is up to each contestant to devise a white-box attack against the models.  Weights and parameters for each model are located in individual subfolders in the [models/](models/) folder.  

For MalConv and Non-Negative MalConv, a differentiable white-box attack (for example, [the FSGM attack](https://pytorch.org/tutorials/beginner/fgsm_tutorial.html)) may be possible, although care must be taken to ensure the modified binary is still functional.  As noted in the [MalConv.py](MalConv.py), the objective function (required for differentiable attacks) used to train the models was `criterion = nn.CrossEntropyLoss()`. 

## Communicate with other participants
Follow the competition in github issues here and in the [MLSEC Slack channel](https://evademalwareml.slack.com/).
