# ACI Controller Configuration using Direct API

This program configures the ACI Controller using the Direct API. There are three stages/menu options in this program:

1. **Counting Existing Tenants and Application Profiles**: Counts the number of existing Tenants and Application Profiles.
2. **Configuring Tenant and Application Profiles**: Adds 1 Tenant (Normativitas) and 3 Application Profiles.
3. **Displaying Member Information**: Shows the names and student IDs of group members, and removes the configurations that were added.

## Requirements

Before running the program, ensure that you have installed the necessary dependencies. Use the following command:

```bash
pip install -r requirements.txt
```

## How to Run the Program

After installing the dependencies, you can run the program with the following command:

```bash
python aci-controller-direct-api.py
```

## Naming Structure

- **Tenant**:  
  - Normativitas  

- **Application Profiles**:  
  - Kritis  
  - Kreatif  
  - Inovatif  

### Configured Attributes

- `descr`
- `annotation`

Feel free to customize the "Contact" section with your own information.
