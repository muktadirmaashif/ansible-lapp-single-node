# LAMP Stack Setup Guide Using Ansible Roles

This guide outlines the steps to set up a LAMP (Linux, Apache, MariaDB, PHP/Python) stack using Ansible roles. It covers project structure, role creation, and playbook execution.

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
   │   └── webserver.yml
   └── roles/
       ├── common/
       ├── web/
       ├── db/
       └── app/
   ```

2. Each role (common, web, db, app) should have the following structure:

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

## Step-by-Step Guide

1. Set up the project structure:
   - Create the main project directory and subdirectories as shown above.
   - Create an empty `ansible.cfg` file in the root directory.

2. Create the inventory file:
   - In the `inventory` file, define your target hosts.

3. Create the main playbook:
   - In `site.yml`, define the playbook that will use all the roles.

4. Set up the common role:
   - Create the directory structure for the common role.
   - In `roles/common/tasks/main.yml`, define common tasks for all servers.

5. Set up the web role (Apache):
   - Create the directory structure for the web role.
   - In `roles/web/tasks/main.yml`, define tasks to install and configure Apache.
   - Create necessary templates in `roles/web/templates/`.
   - Define default variables in `roles/web/defaults/main.yml`.

6. Set up the db role (MariaDB):
   - Create the directory structure for the db role.
   - In `roles/db/tasks/main.yml`, define tasks to install and configure MariaDB.
   - Create necessary templates in `roles/db/templates/`.
   - Define default variables in `roles/db/defaults/main.yml`.

7. Set up the app role (Python/PHP):
   - Create the directory structure for the app role.
   - In `roles/app/tasks/main.yml`, define tasks to set up the application environment.
   - Create necessary templates and files in `roles/app/templates/` and `roles/app/files/`.
   - Define default variables in `roles/app/defaults/main.yml`.

8. Configure group variables:
   - In `group_vars/all/main.yml`, define variables that apply to all hosts.
   - Use `group_vars/all/vault.yml` for sensitive data (ensure this file is encrypted).

9. Configure host variables:
   - In `host_vars/webserver.yml`, define variables specific to your web server.

10. Secure sensitive data:
    - Use Ansible Vault to encrypt sensitive data in `group_vars/all/vault.yml`.

11. Review and adjust configurations:
    - Go through all role tasks, templates, and variable files to ensure they meet your specific requirements.

12. Run the playbook:
    - Execute the playbook using the command: `ansible-playbook -i inventory site.yml --ask-vault-pass`

13. Verify the setup:
    - Check that Apache, MariaDB, and your application are running correctly on the target server.

## Best Practices

1. Use meaningful names for roles, tasks, and variables.
2. Keep roles focused on a single responsibility.
3. Use variables for values that might change between deployments.
4. Use templates for configuration files to make them dynamic.
5. Use handlers to restart services only when necessary.
6. Keep sensitive information in encrypted vault files.
7. Use tags in your tasks for selective execution of parts of your playbook.
8. Document your roles and playbooks for easier maintenance and collaboration.

## Customization

- Adjust the roles and tasks according to your specific LAMP stack requirements.
- Modify variable values in `defaults/main.yml` of each role to suit your needs.
- Add additional roles or tasks as needed for your specific application setup.

By following this guide, you'll have a well-structured Ansible project for deploying and managing a LAMP stack. Remember to test thoroughly in a non-production environment before deploying to production servers.

# LAMP Stack Ansible Roles Overview

## Common Role

### Tasks:
1. Update package cache
2. Install common packages (e.g., vim, curl, git)
3. Configure system-wide settings
4. Set up firewall rules

### Templates:
- None specific to this role

## Web Role (Apache)

### Tasks:
1. Install Apache web server
2. Start and enable Apache service
3. Configure Apache virtual hosts
4. Set up SSL certificates (if applicable)
5. Configure mod_php or PHP-FPM (if using PHP)

### Templates:
1. Apache main configuration file
2. Virtual host configuration
3. SSL configuration (if applicable)

## DB Role (MariaDB)

### Tasks:
1. Install MariaDB server
2. Start and enable MariaDB service
3. Secure MariaDB installation
4. Create application database
5. Create and configure database user
6. Import initial data (if needed)

### Templates:
1. MariaDB configuration file
2. Initial SQL script for database setup (if needed)

## App Role (Python/PHP)

### Tasks:
1. Install Python/PHP and necessary extensions
2. Set up virtual environment (for Python)
3. Install application dependencies
4. Deploy application code
5. Configure application settings
6. Set up application service (e.g., Gunicorn for Python)

### Templates:
1. Application configuration file
2. Environment variables file
3. Systemd service file for application

## Additional Notes:

1. Each role may include handlers to restart services when configuration changes.
2. The `files` directory in each role may contain static files to be copied to the server.
3. The `vars` directory may contain role-specific variables.
4. The `defaults` directory contains default values for role variables that can be overridden.

This structure allows for a modular and reusable approach to deploying a LAMP stack. Each role focuses on its specific component, making the overall playbook easier to maintain and adapt to different requirements.
