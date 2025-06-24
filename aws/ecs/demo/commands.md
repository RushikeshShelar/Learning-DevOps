- Login to ECR (replace <region> and <account-id> with your actual values)
```bash
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
```

- Build the Docker image (replace <repo-name> with your ECR repository name)
```bash
docker build -t <account-id>.dkr.ecr.<region>.amazonaws.com/<repo-name>:latest .
```

- Push the Docker image to ECR (replace <repo-name> with your ECR repository name)
```bash
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/<repo-name>:latest
```
