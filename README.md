# How To
This README will mainly cover what to read to catch up to speed and understand what is happening, as well as what the files are used for.

## What to Research
So far this project is done using GPT models. OpenAIs documentation would be one of the best things to read and understand as we are using there systems.
Included are a few links to more important topics that are being using like fine-tuning, but general reading on these areas are recomended:
- [Supervised Fine-tuning](https://platform.openai.com/docs/guides/supervised-fine-tuning?formatting=jsonl&job=ui&monitoring=ui&using=ui)
- [Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering#page-top)

## Files and Uses
### Questions Prompt
Used to generate questions from standings/viewpoints of different American political parties (Centre/Right/Left). 
100 questions from each are used for creating a fine-tuning job.

### Dataset Prompot
Each questions is parsed through this prompt to generate thinking traces and apply steps to be more mindful about words used and bias in output.
This is formatted as JSON and then written to a file to turn it into JSONL so that it can be used for fine-tuning.

### Fine-tuning
A small file that uses OpenAI APIs to upload fine-tuning data file and initiate fine-tuning job.
