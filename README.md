# HMER-MTL: Towards efficient recognition of handwritten mathematical expressions with multi-task learning.

> Please press ⭐ button and/or cite papers if you feel helpful.

<p align="center">
<img src="https://img.shields.io/github/stars/trungtndev/HMER-MTL">
<img src="https://img.shields.io/github/forks/trungtndev/HMER-MTL">
<img src="https://img.shields.io/github/watchers/trungtndev/HMER-MTL">
</p>

<p align="center">
<img src="https://img.shields.io/badge/Last%20updated%20on-13.01.2025-brightgreen?style=for-the-badge">
<img src="https://img.shields.io/badge/Written%20by-Nguyen%20Thanh%20Trung-pink?style=for-the-badge"> 
</p>


## Abstract 
> Handwritten Mathematical Expression Recognition (HMER) is challenging due to structural relationships, implicit symbols, and handwriting styles. Therefore, this paper presents a novel combining multi-task learning with advanced attention mechanisms, including the Convolutional Block Attention Module (CBAM) integrated into the Attention Refinement Module (ARM), which optimizes attention mechanisms, context-aware interpretation, and generalization of architecture. Integrating multi-task learning enhances the model's ability to work well on the main task. By sharing knowledge across tasks, the model reduces overfitting leads to better generalization in the inference stage. Advanced attention mechanisms refine the attention distribution to capture highly complex structure expressions and implicit correction. Our approach addresses the limitations of traditional methods and demonstrates improving the expression recognition rate on CROHME data sets. Experimental results show that our model has competitive performance and lower parameters when compared with state-of-the-art.
>
> Index Terms: Handwritten mathematical expression recognition, Transformer, Attention mechanism, Multi-task learning.
## Table of Contents

- [**Abstract**](#Abstract)
- [**Usage**](#Usage)
  - [Dataset](#dataset)
  - [Clone this repository](#clone-this-repository)
  - [Create Conda Enviroment and Install Requirement](#create-conda-enviroment-and-install-requirement)
- [**References**](#references)
- [**Citation**](#citation)
- [**Contact**](#Contact)

## Usage
### Dataset
The CROHME dataset can be downloaded [CoMER/blob/master/data.zip](https://github.com/Green-Wood/CoMER/blob/master/data.zip) (provided by the **CoMER** project)

### Clone this repository
```
git clone https://github.com/trungtndev/HMER-MTL
```

### Create Conda Enviroment and Install Requirement
```bash
cd HMER-MTL
# install project   
conda create -y -n HMER-MTL python=3.7
conda activate HMER-MTL
conda install pytorch=1.8.1 torchvision=0.2.2 cudatoolkit=11.1 pillow=8.4.0 -c pytorch -c nvidia
# training dependency
conda install pytorch-lightning=1.4.9 torchmetrics=0.6.0 -c conda-forge
# evaluating dependency
conda install pandoc=1.19.2.1 -c conda-forge
pip install -e .
```

## Training
```bash
python train.py --config config.yaml  
```

You may change the `config.yaml` file:
```yaml
lambda_1: 1 # weight of the main task
lambda_2: 1 # weight of the auxiliary task
```
GPU configuration:
```yaml
gpus: 1 # number of GPU
```

## Evaluation
```bash
python test.py 0 2016 # 2014, 2016, 2019
```


## References
Zhao, W., & Gao, L. (2022, October). Comer: Modeling coverage for transformer-based handwritten mathematical expression recognition. In European conference on computer vision (pp. 392-408). Cham: Springer Nature Switzerland.

Zhao, W., Gao, L., Yan, Z., Peng, S., Du, L., & Zhang, Z. (2021). Handwritten mathematical expression recognition with bidirectionally trained transformer. In Document analysis and recognition–ICDAR 2021: 16th international conference, Lausanne, Switzerland, September 5–10, 2021, proceedings, part II 16 (pp. 570-584). Springer International Publishing.

Guan, T., Lin, C., Shen, W., & Yang, X. (2025). PosFormer: recognizing complex handwritten mathematical expression with position forest transformer. In European Conference on Computer Vision (pp. 130-147). Springer, Cham.

Zhu, J., Gao, L., & Zhao, W. (2024, August). ICAL: Implicit Character-Aided Learning for Enhanced Handwritten Mathematical Expression Recognition. In International Conference on Document Analysis and Recognition (pp. 21-37). Cham: Springer Nature Switzerland.
## Citation
If you use this code or part of it, please cite the following papers:
```
Update soon
```
## Contact
For any information, please contact the main author:

Thanh Trung Nguyen at FPT University, Vietnam

**Email:** <link>trunglh113@gmail.com </link><br>
**ORCID:** <link>https://orcid.org/0009-0004-7553-4848</link> <br>
**GitHub:** <link>https://github.com/trungtndev/</link>


