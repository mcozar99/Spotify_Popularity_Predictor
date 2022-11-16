## Predicting song popularity using track features
### Miguel Cozar Tramblin A20522001
### Carlos Munoz Losa A20521562

This is the project for Deep Learning Fall Semester 2022 at Illinois Tech. In this project we propose three different deep learning models for predicting a song's popularity using three different sets of features:

- General Song Features
- Musical Analysis Features
- Lyrics Features

In the repo, you will find three jupyter notebooks with the design of each model, plus the loading of the data. The created models are available in the link provided at models.txt
. The used references are available at sources.txt.

To gather data, first download The Million Song Dataset and it will automatically parse the files given a directory of a file.
To use the lyrics data gatherer, first log in to genius.com, get an API key and paste it in a new file keys.py on this way:

```
genius_tokens = ["your genius token", "another genius token", "another genius token"...]
```

