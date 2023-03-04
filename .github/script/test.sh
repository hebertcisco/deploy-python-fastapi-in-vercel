#!/bin/sh

if ! [ -x "$(command -v pip)" ]; then
  echo 'Error: pip is not installed.' >&2
  echo 'Installing pip...'
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python get-pip.py
  rm get-pip.py
  echo 'pip installed.'
fi

pip install -r requirements.txt

if ! [ -x "$(command -v pytest)" ]; then
  echo 'Error: pytest is not installed.' >&2
  echo 'Installing pytest'
  pip install pytest
  echo 'pytest installed.'
fi


pytest