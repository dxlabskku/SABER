# SABER : A Multi-task Framework Combining Sentiment and Behavioral Cues
Movie repository is to supplement the paper "SABER : A Multi-task Framework Combining Sentiment and Behavioral Cues".

## Abstract
As the severity of climate change intensifies, comprehending public attitudes toward this pressing issue has become increasingly crucial for developing effective mitigation strategies. Social media platforms have emerged as influential tools for shaping and reflecting public opinion on climate change. However, the discourse on these platforms is deeply polarized between those who acknowledge the urgency of the situation and those who maintain a skeptical stance. This stark divide in public opinion has significant necessity for the dissemination of accurate information and the development of effective climate change mitigation strategies, rendering stance detection a vital task in this domain. Thus, this study introduces a novel multi-task framework SABER, that jointly performs stance detection and sentiment analysis on climate change-related tweets. With different embedding techniques and attention frameworks, the proposed framework utilizes learned sentiment aspects learned from the data to obtain a comprehensive representation of the features relevant to the stance expressed in a given tweet. Extensive experiments conducted on a constructed climate change dataset demonstrate the effectiveness of our approach, highlighting the importance of considering user interaction patterns and sentiment information in recognizing stance.

## Overview of our framework
<img src="https://github.com/dxlabskku/SABER/assets/43632309/8489c93f-b601-4209-b162-5173ebbb7e75.png" width="710" height="292"><br>
<strong>Figure 1 : The overview architecture of our proposed multi-task framework SABER</strong>

## Clone
TBD

## Dataset
Our dataset comprises 70,412 climate change-related tweets collected from Twitter between January 1, 2022, and December 31, 2022, using specific denier and believer hashtags. Each tweet is labeled for stance detection as either "believe" or "deny" based on the used hashtags, with 49,006 tweets identified as denying climate change and 12,241 as believing. In addition, we assign sentiment labels in four categories: positive, negative, and neutral, using the VADER.
## Reference
TBD
