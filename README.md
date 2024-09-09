# LAPP Stack Setup Guide Using Ansible Roles

This project sets up a LAPP (Linux, Apache, Postgresql, Python) stack using Ansible roles. It covers project structure, role creation, and playbook execution.

## Project Structure

1. Create the following directory structure for your Ansible project:

   ```
   lamp_playbook/
   ├── ansible.cfg
   ├── inventory
   ├── site.yml
   ├── group_vars/
   │   └── all/
   │       ├── main.yml
   │       └── vault.yml
   ├── host_vars/
   │   └── ubuntu-lamp.yml
   └── roles/
       ├── common/
       ├── web/
       ├── db/
       └── app/
   ```

2. Each role has the following structure:

   ```
   roles/[role_name]/
   ├── tasks/
   │   └── main.yml
   ├── handlers/
   │   └── main.yml
   ├── templates/
   ├── files/
   ├── vars/
   │   └── main.yml
   └── defaults/
       └── main.yml
   ```

## Pre-requisite 

1. Create `lamp` user and place the public key of the ansible host inside it's `.ssh/authorized_keys`.

2. Edit the inventory file:
   - In the `host_vars/`, create a .yml file, place your target host ip, and mention this file in inventory.

3. Create the main playbook:
   - In `site.yml`, define the playbook that will use all the roles.

## Role-specific descriptions 

1. The common role:
   - This will install and configure all the system related settings, e.g. firewall, services, etc..

2. The web role (Apache):
   - Create the directory structures, installs required packages for the web role.
   - Create necessary templates in `roles/web/templates/` to place it in `/etc/apache2/sites-available`.
   - Define default variables in `roles/web/defaults/main.yml`.

3. The app role (Python):
   - installs python-specific dependencies, flask as the web framework, tools for using it with apache2..
   - Necessary templates and source codes in `roles/app/templates/` and `roles/app/files/`.

4. The db role (Postgresql):
   - Installs and configures packages and databases.
   - Create necessary templates in `roles/db/templates/`.


## Run the playbook:
    - Execute the playbook using the command: `ansible-playbook site.yml -K`.
    - Try a dry check (syntax, etc) before making actual changes.

## To-Do
- Secure sensitive data:
    - Use Ansible Vault to encrypt sensitive data (database and user passwords) in `group_vars/all/vault.yml`.
