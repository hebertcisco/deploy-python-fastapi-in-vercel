# FastApi + Vercel

## How it Works

This example uses the Web Server Gateway Interface (WSGI) with FastApi to enable handling requests on Vercel with Serverless Functions.

## Running Locally

### With Docker Compose

```bash
docker-compose up
```

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
