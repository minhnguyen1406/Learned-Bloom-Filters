# Exploring Machine Learning Enhanced Bloom Filters
## Minh Nguyen and  Utkarsh Bahuguna

## Overview
Bloom filters are extremely space efficient data structures for membership verification, but since
they are probabilistic, traditional Bloom filters frequently have a fixed false positive rate and are
not flexible enough to adjust to changing data patterns. Also in some applications, the size of the
membership set might be so large that even the bloom filter might exceed space limitations. In
this project, we will investigate how machine learning can improve Bloom filters in such situations.
In some other cases, more information beyond just membership verification is required while still
being space efficient. Given that machine learning (ML) models are able to adjust and learn from
the dataset's features, bloom filters enhanced with ML can potentially overcome some such
shortcomings of traditional Bloom filters

In this project, we implement the following variations of Bloom
Filters enhanced by utilizing Machine Learning:
- Pre-filter Learned Bloom Filter
  - Where a learned ML model is used as a pre-filter for the Bloom Filter
- Anomaly Detection Bloom Filter 
  - Where an ML model is utilized after the bloom filter as an additional layer of
  verification to reduce impact of false positives
- Class-aware Bloom Filter 
  - Where an ML model is used after the bloom filter to give additional information
    about the class of the item, rather than just its presence in the filter.
- Class-wise Bloom Filters 
  - Where a multi-class ML classifier is used to direct queries to the relevant bloom
  filter, possibly reducing FP rates in each class-specific filter.

### Usage
Our exploration is done in the form of Jupyter notebooks. The notebooks are organized as follows:
- binary_classifier_learned_bloom_filters_malicious_url.ipynb - this notebook explores the first two variants of learned bloom filters, namely pre-filter learned bloom filter and anomaly detection bloom filter. The dataset used is the malicious URL dataset.
- binary_classifier_learned_bloom_filters_NSL_KDD.ipynb - this notebook also explores the first two variants of learned bloom filters, namely pre-filter learned bloom filter and anomaly detection bloom filter. The dataset used is the NSL-KDD dataset.
- multi-class_classifier_learned_bloom_filters_malicious_url.ipynb - this notebook explores the last two variants of learned bloom filters, namely class-aware bloom filter and class-wise bloom filters. The dataset used is the malicious URL dataset.
- multi-class_classifier_learned_bloom_filters__NSL_KDD.ipynb - this notebook also explores the last two variants of learned bloom filters, namely class-aware bloom filter and class-wise bloom filters. The dataset used is the NSL-KDD dataset.

### References
- Kraska, Tim, et al. “The Case for Learned Index Structures.” arXiv.org, arXiv, 30 Apr. 2018,
arxiv.org/abs/1712.01208.
- Bhattacharya, Arunava, et al. “New Wine in an Old Bottle.” Proceedings of the VLDB Endowment,
doi.org/10.14778/3538598.3538613.
- Mitzenmacher, Michael. “A Model for Learned Bloom Filters and Optimizing by Sandwiching.”
arXiv preprint, arXiv, 2018, arxiv.org/abs/1802.00884.
- Mohi-ud-din, Ghulam. “NSL-KDD.” IEEE Dataport, 2018, dx.doi.org/10.21227/425a-3e55.
Siddhartha, Manu. “Malicious URLs.” Kaggle, www.kaggle.com/datasets/sid321axn/malicious-
urls-dataset.