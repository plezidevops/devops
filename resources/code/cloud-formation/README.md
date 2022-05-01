# Things to keep in mind as you secure the infrastructure

## Security Groups
1. Security groups are specific to individual resources (ex. EC2)
2. All traffic is block by default
3. If a traffic is allowed to come in, the return traffic is automatically allowed

## Commands to run to create the stacks

```
1. Create the infrastructure statck
./create.sh my-devops-network-stack my-infrastructure.yml my-network-parameters.json

2. Create the security rules stack
./create.sh my-devops-servers-sg-stack my-servers.yml my-servers-param.json

```