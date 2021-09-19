# Azure subscription vars
subscription_id = "76b1e36a-6202-4055-914a-1618f6c3575e"
client_id = "018407bc-bed1-479c-831f-74ac6284471d"
client_secret = "_5U7Q~HfzHLFsjdd4~iWa6BrcmlRJS1t209ci"
tenant_id = "23ee68a6-8c07-455d-90fa-dc5cc9747d2a"

# Resource Group/Location
location = "Central US"
resource_group = "MyResGroup1"
application_type = "Infra-CICD-Autotest"


# Network
virtual_network_name = "myVirtualNetwork"
address_space = ["10.5.0.0/16"]
address_prefix_test = "10.5.1.0/24"

#VM

size =  "Standard_B1s"
name =  "MyVM"
publisher = "Canonical"
offer     = "UbuntuServer"
sku       = "18.04-LTS"
sourceVersion   = "latest"

