# molecule-test

Some configuration and tests with molecule

Mainly :

  * `ansible-role-apache` : Molecule configuration embedded in a role
  * `playbook-test` : Test of a playbook using molecule
  * `multiroles-test` : Test of roles with exteran molecule config. (using ansible galaxy)

Random notes:

```
# Create a new ansible role from 0
molecule init role  --driver-name docker  -r ansible-supervisord

# Add test scenario on an existing role
cd ansible-supervisord/
molecule init scenario  --driver-name docker  -r ansible-supervisord --scenario-name default

# Tests
molecule test
```
