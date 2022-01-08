This utility converts security artifacts (*.pem and *.p7s files) in the current working directory into strings. These strings are defined as macros in a C/C++ header file named "artifacts.h". Currently, this utility does not scan directories recursively, so all security artifacts of interest should be moved to a common directory.

The macros can then be used in RTI Connext Micro 3.x + Security SDK applications on systems where a filesystem is not available, such as memory constrained RTOS' running on microcontrollers.

For example, in the Connext Micro 3.0.3 HelloWorld_dpde_secure example, including a generated "artifacts.h" file allows sec_material to be populated without any external files:

```
struct ApplicationSecMaterial sec_material(
     /* ca_id_cert */   CA_PEM,                        //"file:security/ca/ca.pem",
     /* ca_perm_cert */ CA_PEM,                        //"file:security/ca/ca.pem",
     /* peer_key */     PUBLISHER_KEY_PEM,             //"file:security/ca/certs/" PEER_NAME "_key.pem",
     /* peer_cert */    PUBLISHER_PEM,                 //"file:security/ca/certs/" PEER_NAME ".pem",
     /* xml_gov */      GOVERNANCE_P7S,                //"file:security/xml/governance.p7s",
     /* xml_perm */     PERMISSIONS_PUBLISHER_P7S);    //"file:security/xml/permissions_" PEER_NAME ".p7s");
PEER_MATERIAL_DEFAULT = sec_material;
```
