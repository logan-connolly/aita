#  Am I the Asshole? (aita)

[![Build Status](https://travis-ci.com/logan-connolly/aita.svg?branch=master)](https://travis-ci.com/logan-connolly/aita)

Ever asked yourself, *"Am I the asshole here?"* This application helps you answer that. Based on the famous subreddit [/r/AmItheAsshole](https://www.reddit.com/r/AmItheAsshole/)

To find out if you are the asshole, simply go to the [website](https://github.com/logan-connolly/aita), type in the argument that you are having with someone (more detail the better) and click submit. The output should be a prediction with one of the following categories:

- **YTA**: You're the Asshole
- **NTA**: Not the Asshole
- **ESH**: Everyone Sucks here
- **NAH**: No Assholes here
- **INFO**: Not Enough Info

In order to help explain why a decision was made, the input text will also be highlighted on areas that contributed to the respective decision.

# Setup

Define `.env` file in project root ([OAuth Guide](https://asyncpraw.readthedocs.io/en/latest/getting_started/authentication.html#oauth)):

```shell
POSTGRES_USER=aita
POSTGRES_PASSWORD=aita
POSTGRES_DB=aita_db
POSTGRES_HOST=db

# need to generate your own OAuth credentials
REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=
REDDIT_PASSWORD=
REDDIT_USERNAME=

API_PORT=8020
WEB_PORT=8021
```

Build images with `docker-compose build` and start services with `docker-compose up -d`.

# Disclaimer

No data that you pass to Asshole Predictor will be saved. The model will only be trained on posts from [/r/AmItheAsshole](https://www.reddit.com/r/AmItheAsshole/), which are monitored to prevent users from posting personally-identifying information like names, numbers, addresses, etc.
