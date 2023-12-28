<p align="center">
 <img width="100px" src="https://raw.githubusercontent.com/hebertcisco/vercel-typescript-express-api/cebd0c563141a4cc7d279997b8cb5dd9232d7591/.github/images/favicon512x512-vercel-typescript-express-api.png" align="center" alt=":package: deploy-python-fastapi-in-vercel" />
 <h2 align="center">:package: deploy-python-fastapi-in-vercel</h2>
 <p align="center">This example shows how to use FastApi  on Vercel with Serverless Functions using the Python Runtime.</p>
</p>

  <p align="center">
    <a href="https://github.com/hebertcisco/deploy-python-fastapi-in-vercel/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/hebertcisco/deploy-python-fastapi-in-vercel?style=flat&color=336791" />
    </a>
    <a href="https://github.com/hebertcisco/deploy-python-fastapi-in-vercel/pulls">
      <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/hebertcisco/deploy-python-fastapi-in-vercel?style=flat&color=336791" />
    </a>
    <br />
  <a href="https://github.com/hebertcisco/deploy-python-fastapi-in-vercel/issues/new/choose">Report Bug</a>
  <a href="https://github.com/hebertcisco/deploy-python-fastapi-in-vercel/issues/new/choose">Request Feature</a>
  </p>
  <h3 align="center">Systems on which it has been tested.</h3>
 <p align="center">
  <a href="https://ubuntu.com/download">
      <img alt="Ubuntu" src="https://img.shields.io/badge/Ubuntu-E95420?style=flat&logo=ubuntu&logoColor=white" />
    </a>
  <a href="https://www.microsoft.com/pt-br/software-download/windows10">
      <img alt="Windows" src="https://img.shields.io/badge/Windows-0078D6?style=flat&logo=windows&logoColor=white" />
    </a>
  </p>
<p align="center">Did you like the project? Please, considerate <a href="https://www.buymeacoffee.com/hebertcisco">a donation</a> to help improve!</p>

<p align="center"><strong></strong>✨</p>

# Getting started

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fhebertcisco%2Fdeploy-python-fastapi-in-vercel%2Ftree%2Fmain%2Fpython%2FFastApi&demo-title=FastApi%20%2B%20Vercel&demo-description=Use%20FastApi%202%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2FFastApi-python-template.vercel.app%2F&demo-image=https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

# FastApi + Vercel

This example shows how to use FastApi 0.88.0 on Vercel with Serverless Functions using the [Python Runtime](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python).

[![Python testing](https://github.com/hebertcisco/deploy-python-fastapi-in-vercel/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/hebertcisco/deploy-python-fastapi-in-vercel/actions/workflows/python-app.yml)
[![Docker Image CI](https://github.com/hebertcisco/deploy-python-fastapi-in-vercel/actions/workflows/docker-image.yml/badge.svg)](https://github.com/hebertcisco/deploy-python-fastapi-in-vercel/actions/workflows/docker-image.yml)

## Demo

[deploy-python-fastapi-in-vercel.vercel.app](https://deploy-python-fastapi-in-vercel.vercel.app)

## How it Works

This example uses the Web Server Gateway Interface (WSGI) with FastApi to enable handling requests on Vercel with Serverless Functions.

## Running Locally

### With Docker
```bash
# Build the Docker image
docker build -t deploy-python-fastapi-in-vercel .

# Run the Docker container
docker run -p 8000:8000 deploy-python-fastapi-in-vercel

```

### With uvicorn

#### Install dependencies

```bash
pip install -r requirements.txt
```
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Your FastApi application is now available at `http://localhost:8000`.

## One-Click Deploy

Deploy the example using [Vercel](https://vercel.com?utm_source=github&utm_medium=readme&utm_campaign=vercel-examples):

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fhebertcisco%2Fdeploy-python-fastapi-in-vercel%2Ftree%2Fmain%2Fpython%2FFastApi&demo-title=FastApi%20%2B%20Vercel&demo-description=Use%20FastApi%202%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2FFastApi-python-template.vercel.app%2F&demo-image=https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](issues).

## Show your support

Give a ⭐️ if this project helped you!

Or buy me a coffee 🙌🏾

<a href="https://www.buymeacoffee.com/hebertcisco">
    <img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=hebertcisco&button_colour=FFDD00&font_colour=000000&font_family=Inter&outline_colour=000000&coffee_colour=ffffff" />
</a>

## 📝 License

Copyright © 2023 [Hebert F Barros](https://github.com/hebertcisco).<br />
This project is [MIT](LICENSE) licensed.
