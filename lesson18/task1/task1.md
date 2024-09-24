# Install Azure CLI

Use one line command 

- curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash


https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt

To login use this command. It will be interactive login. You will be redirect to page where you need to select Microsoft account and that's it.
- az login

```shell
tadas@DESKTOP-ECR7J7D:/$ az login
A web browser has been opened at https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize. Please continue the login in the web browser. If no web browser is available or if the web browser fails to open, use device code flow with `az login --use-device-code`.
tcgetpgrp failed: Not a tty
The following tenants don't contain accessible subscriptions. Use 'az login --allow-no-subscriptions' to have tenant level access.
76ff9255-ca8e-46b2-8d2e-f988f23ab709 'OpsBean'
f1604ea6-a036-4ccc-82ba-4400cebda34e 'tameitb2c'
[
  {
    "cloudName": "AzureCloud",
    "homeTenantId": "93cc82fb-d302-44a9-8f26-191ef7aa770e",
    "id": "86be2189-be33-4652-afff-cd871cf1d882",
    "isDefault": true,
    "managedByTenants": [],
    "name": "Free Trial",
    "state": "Enabled",
    "tenantId": "93cc82fb-d302-44a9-8f26-191ef7aa770e",
    "user": {
      "name": "tadas.andriuska@outlook.com",
      "type": "user"
    }
  }
]


```