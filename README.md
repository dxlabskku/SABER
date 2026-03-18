# SABER : Integrating Sentiment and Stance Detection for Climate Change Discourse on Social Media
This repository is to supplement the paper "SABER: Integrating sentiment and stance detection for climate change discourse on social media".

## Abstract
As the severity of climate change intensifies, understanding public attitudes toward this pressing issue is crucial for developing effective mitigation strategies. Social media platforms have emerged as influential tools for shaping and reflecting public opinions on climate change. However, the discourse on these platforms is deeply polarized, divided between those who acknowledge the urgency of the situation and those who maintain a skeptical stance, often fueled by misinformation and denial. This stark divide underscores the necessity of disseminating accurate information and developing effective climate change mitigation strategies, making stance detection a vital task in this domain. In response to this need, this study introduces a novel multi-task framework, SABER, which jointly performs stance detection and sentiment analysis on climate change-related tweets. Given the unique and critical nature of climate change discourse, SABER is designed to capture the polarized opinions that characterize these discussions. By employing various embedding techniques and attention frameworks, SABER leverages sentiment aspects learned from the data to create a comprehensive representation of the features relevant to the stance expressed in a tweet. Extensive experiments conducted on a curated climate change dataset demonstrate the effectiveness of our approach, highlighting the importance of considering user interaction patterns and sentiment information in stance recognition. The dataset and code are publicly available, providing a valuable resource for further research in this field.

## Overview of our framework
<img src="https://github.com/dxlabskku/SABER/assets/43632309/8489c93f-b601-4209-b162-5173ebbb7e75.png" width="710" height="292"><br>
<strong>Figure 1 : The overview architecture of our proposed multi-task framework SABER</strong>

## Clone
```
git clone https://github.com/dxlabskku/SABER.git
```

## Dataset
Our dataset comprises 61,247 climate change-related tweets collected from Twitter between January 1, 2022, and December 31, 2022, using specific denier and believer hashtags. Each tweet is labeled for stance detection as either "believe" or "deny" based on the used hashtags, with 49,006 tweets identified as denying climate change and 12,241 as believing. We assign sentiment labels in four categories: positive, negative, and neutral, using the VADER.

## Reference
```@article{ahn2026saber,
  title={SABER: Integrating Sentiment and Stance Detection for Climate Change Discourse on Social Media},
  author={Ahn, Hyeongjin and Jeong, Dahye and Park, Eunil},
  journal={Knowledge-Based Systems},
  pages={115668},
  year={2026},
  publisher={Elsevier}
}
```
