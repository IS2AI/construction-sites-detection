# Construction-sites-detection project
This repo contains code and dataset for training and testing ml model which implements instance segmentation of construction sites. 

# Architectures:
Yolo-v8 and Yolo-v11: [https://github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) <br/> 

# CSDS: Construction Site Detection and Segmentation

The **Construction Site Detection and Segmentation(CSDS)** is a  tool consisting of 16 CSDS models and of large-scale dataset of construction site satellite imagery with detailed polygon annotations(5 stages and footings).  
It contains both the **raw source data** (images and XML annotations) and **preprocessed training-ready splits** in YOLO format.  

## Pretrained Models
Pretrained models are available at:  
👉 [issai/CSDS_models](https://huggingface.co/issai/CSDS_models)

## Dataset 
The dataset are available at:  
👉 [datasets/issai/CSDS_models](https://huggingface.co/datasets/issai/CSDS_dataset) 
To request access, please fill out the form. Access will be provided once it has been manually.

## Data availability
The dataset is available at Digital Object Identifier (DOI) https://doi.org/10.48333/0PJD-BP65.


## Dataset Structure

- All images and annotations are provided in **ZIP archives** for efficient storage and download.  
- The `raw/` folder contains original images and XML annotations.  
- The `preprocessed/` folder contains processed input images (600px and 1200px) and corresponding annotations in YOLO-style train/test/val splits.


### Raw Data
```

raw/
├── images/                     # Original construction site images
└── annotations/
├── AOD/                     # XML annotations for *All Objects Dataset*
└── FVOD/                    # XML annotations for *Fully Visible Objects Dataset*

``` 

### Preprocessed Data
```

preprocessed/
├── AOD/
│   ├── 600/                     # Images with input resolution of 600px (YOLO format)
│   │   ├── train/
│   │   │   ├── images/
│   │   │   └── labels/
│   │   ├── val/
│   │   │   ├── images/
│   │   │   └── labels/
│   │   └── test/
│   │       ├── images/
│   │       └── labels/
│   └── 1200/                    # Images with input resolution of 1200px (YOLO format)
│       └── (train/test/val structure as above)
│
└── FVOD/
├── 600/
│   └── (train/test/val with images + labels)
└── 1200/
└── (train/test/val with images + labels)

```

- **AOD/** → Preprocessed dataset corresponding to "all objects" annotations.  
- **FVOD/** → Preprocessed dataset corresponding to "fully visible objects" annotations.  
- Each size folder (`600/`, `1200/`) contains YOLO-ready **`train/`**, **`val/`**, and **`test/`** splits with `images/` and `labels/` directories.  


## If you use the dataset/source code/pre-trained models in your research, please cite our work:

```

@dataset{issai_csds_2025,
  title        = {CSDS: AI-Based Construction Site Detection and Segmentation tool for Satellite Images},
  author       = {Bissarinova, U. and Awan, H. H. and Olagunju, S. O. and Bolatkhanov, I. and Turekhassim, A. and Varol, H. A. and Karaca, F.},
  year         = {2025},
  publisher    = {Institute of Smart Systems and Artificial Intelligence and Department of Civil Engineering, Nazarbayev University},
  howpublished = {\url{https://doi.org/10.48333/0PJD-BP65}}
}
