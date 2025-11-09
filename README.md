# How To
This README will mainly cover what to read to catch up to speed and understand what is happening, as well as what the files are used for.

## What to Research
So far this project is done using GPT models. OpenAIs documentation would be one of the best things to read and understand as we are using there systems.
Included are a few links to more important topics that are being using like fine-tuning, but general reading on these areas are recomended:
- [Supervised Fine-tuning](https://platform.openai.com/docs/guides/supervised-fine-tuning?formatting=jsonl&job=ui&monitoring=ui&using=ui)
- [Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering#page-top)
- [Graders](https://platform.openai.com/docs/guides/graders)

## Files and Uses
### Questions Prompt
Used to generate questions from standings/viewpoints of different American political parties (Centre/Right/Left). 
100 questions from each are used for creating a fine-tuning job.

### Dataset Prompot
Each questions is parsed through this prompt to generate thinking traces and apply steps to be more mindful about words used and bias in output.
This is formatted as JSON and then written to a file to turn it into JSONL so that it can be used for fine-tuning.

### Fine-tuning
A small file that uses OpenAI APIs to upload fine-tuning data file and initiate fine-tuning job.
Parts will be separated or commented to indicate if they are used for SFT or RFT (RFT has been deemed not feasible as it is too expensive).

### Garder.py
A few python files for testing python graders for an RFT run. The main one used is the model-grader.py, the others are examples generated for other ways not tested.

### Reinforcement Fine-tuning
Mainly used for testing how well the grader works to check if RFT is usable for this purpose.
Contains centrist, left, and right wing prompts to create biased output to measure how effective the grader is.

## Other
There are viarious .josn and .jsonl files that store data from tests or for files that were uploaded to OpenAI for fine-tuning.
