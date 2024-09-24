# Azure Point to Site VPN

Point to Site VPN - end user will connect to VPN to access remote resources on Azure


1. Create virtual network

 - az network vnet create -g accademy -n myVNETlesson18 --tags lesson=lesson18

```shell
tadas@DESKTOP-ECR7J7D:/$ az network vnet create -g accademy -n myVNETlesson18 --tags lesson=lesson18
{
  "newVNet": {
    "addressSpace": {
      "addressPrefixes": [
        "10.0.0.0/16"
      ]
    },
    "enableDdosProtection": false,
    "etag": "W/\"82d6fbe2-464f-4477-9ddc-638c77da24f7\"",
    "id": "/subscriptions/86be2189-be33-4652-afff-cd871cf1d882/resourceGroups/accademy/providers/Microsoft.Network/virtualNetworks/myVNETlesson18",
    "location": "swedencentral",
    "name": "myVNETlesson18",
    "provisioningState": "Succeeded",
    "resourceGroup": "accademy",
    "resourceGuid": "61a531fe-925d-40a3-ab46-23461528e3e1",
    "subnets": [],
    "tags": {
      "lesson": "lesson18"
    },
    "type": "Microsoft.Network/virtualNetworks",
    "virtualNetworkPeerings": []
  }
}
```
2. Create NAT GW - used UI for this. 

3. Create a subnet
 - az network vnet subnet create -n mySubNetlesson18 -g accademy –vnet-name myVNETlesson18 –address-prefixes 10.0.0.0/24 --tags lesson=lesson18


 az network vnet subnet create --name MySubnetlesson18 --vnet-name myVNETlesson18 --resource-group accademy --nat-gateway lesson18natgw --address-prefixes "10.0.0.0/21"

 ```shell
 tadas@DESKTOP-ECR7J7D:/$ az network vnet subnet create --name MySubnetlesson18 --vnet-name myVNETlesson18 --resource-group accademy --nat-gateway lesson18natgw --address-prefixes "10.0.0.0/21"
{
  "addressPrefix": "10.0.0.0/21",
  "delegations": [],
  "etag": "W/\"7891b25f-5e81-4cfd-b1c8-397037d4c4ea\"",
  "id": "/subscriptions/86be2189-be33-4652-afff-cd871cf1d882/resourceGroups/accademy/providers/Microsoft.Network/virtualNetworks/myVNETlesson18/subnets/MySubnetlesson18",
  "name": "MySubnetlesson18",
  "natGateway": {
    "id": "/subscriptions/86be2189-be33-4652-afff-cd871cf1d882/resourceGroups/accademy/providers/Microsoft.Network/natGateways/lesson18natgw",
    "resourceGroup": "accademy"
  },
  "privateEndpointNetworkPolicies": "Disabled",
  "privateLinkServiceNetworkPolicies": "Enabled",
  "provisioningState": "Succeeded",
  "resourceGroup": "accademy",
  "type": "Microsoft.Network/virtualNetworks/subnets"
}
```

4. 

- az network vnet subnet create -g accademy -n lesson18natgw –vnet-name myVNETlesson18 –address-prefix 10.0.0.0/21

