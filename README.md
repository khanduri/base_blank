

## SETUP

### LOCAL
 - Set you ENVIRONMENT to local
 - git clone git@github.com:khanduri/base_blank.git workouts
 - git remote remove origin
 - virtualenv virenv --no-site-packages
 - source virenv/bin/activate
 - pip install -r requirements.txt
 - python db_create.py
 - npm init

### HEROKU
 - config setting :
    - BOOTSWATCH_TEMPLATE_INDEX
    - DATABASE_URL
    - ENVIRONMENT


