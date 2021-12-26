## 👀 Am I the Asshole? (aita)

[![api](https://github.com/logan-connolly/aita/actions/workflows/test_api.yaml/badge.svg)](https://github.com/logan-connolly/aita/actions/workflows/test_api.yaml)
[![nlp](https://github.com/logan-connolly/aita/actions/workflows/test_nlp.yaml/badge.svg)](https://github.com/logan-connolly/aita/actions/workflows/test_nlp.yaml)

## 📦 Overview

Ever asked yourself, *"Am I the asshole here?"* This application helps you answer that. Based on the famous subreddit [/r/AmItheAsshole](https://www.reddit.com/r/AmItheAsshole/), the goal of the app is to take a story yours and classify whether:

- **YTA**: You're the Asshole
- **NTA**: Not the Asshole
- **ESH**: Everyone Sucks here
- **NAH**: No Assholes here

## 🛺 Roadmap

- Develop API that fetches AITA posts from reddit ✔️
- Create v1 text categorizer that predicts YTA/NTA ✔️
- Develop v1 frontend that accepts a story and predict category 🚧
- Add explainable AI that highlights why category was selected 🚧

## 💻 Development

Define `.env` file in project root and supply reddit credential. Here is the official [OAuth Guide](https://asyncpraw.readthedocs.io/en/latest/getting_started/authentication.html#oauth) from `asyncpraw`, the library used for fetching posts from reddit:

```shell
# need to generate your own OAuth credentials
REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=
REDDIT_PASSWORD=
REDDIT_USERNAME=
```
Common commands are detailed in the projects Makefiles.

## ‼️ Disclaimer

No data that you pass to Asshole Predictor will be saved. The model will only be trained on posts from [/r/AmItheAsshole](https://www.reddit.com/r/AmItheAsshole/), which are monitored to prevent users from posting personally-identifying information like names, numbers, addresses, etc. Also, any model that is generated from this data is **highly biased** so don't take the response seriously.
