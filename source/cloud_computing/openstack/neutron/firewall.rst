防火墙
======

几个概念

- rule
- policy
- firewall

.. code-block:: console

   # openstack firewall group rule create --name test_rule_icmp_deny --action deny --protocol icmp
   +------------------------+--------------------------------------+
   | Field                  | Value                                |
   +------------------------+--------------------------------------+
   | Action                 | deny                                 |
   | Description            |                                      |
   | Destination IP Address | None                                 |
   | Destination Port       | None                                 |
   | Enabled                | True                                 |
   | ID                     | d7b3ffb2-3702-4208-888a-8dd9cfd78906 |
   | IP Version             | 4                                    |
   | Name                   | test_rule_icmp_deny                  |
   | Project                | 1fac5da33e6c48ffb990b6da2ec40020     |
   | Protocol               | icmp                                 |
   | Shared                 | False                                |
   | Source IP Address      | None                                 |
   | Source Port            | None                                 |
   | firewall_policy_id     | None                                 |
   | project_id             | 1fac5da33e6c48ffb990b6da2ec40020     |
   +------------------------+--------------------------------------+

.. code-block:: console

   # openstack firewall group policy create --firewall-rule d7b3ffb2-3702-4208-888a-8dd9cfd78906 icmp_policy
   +----------------+-------------------------------------------+
   | Field          | Value                                     |
   +----------------+-------------------------------------------+
   | Audited        | False                                     |
   | Description    |                                           |
   | Firewall Rules | [u'd7b3ffb2-3702-4208-888a-8dd9cfd78906'] |
   | ID             | dd9f661a-9d61-447a-b32a-b0b2e0d744ca      |
   | Name           | icmp_policy                               |
   | Project        | 1fac5da33e6c48ffb990b6da2ec40020          |
   | Shared         | False                                     |
   | project_id     | 1fac5da33e6c48ffb990b6da2ec40020          |
   +----------------+-------------------------------------------+

.. code-block:: console

   # openstack firewall group create --name icmp_test --ingress-firewall-policy dd9f661a-9d61-447a-b32a-b0b2e0d744ca
   +-------------------+--------------------------------------+
   | Field             | Value                                |
   +-------------------+--------------------------------------+
   | Description       |                                      |
   | Egress Policy ID  | None                                 |
   | ID                | e969c06a-bbc8-4b2a-88aa-beac16b94c7f |
   | Ingress Policy ID | dd9f661a-9d61-447a-b32a-b0b2e0d744ca |
   | Name              | icmp_test                            |
   | Ports             | []                                   |
   | Project           | 1fac5da33e6c48ffb990b6da2ec40020     |
   | Shared            | False                                |
   | State             | UP                                   |
   | Status            | INACTIVE                             |
   | project_id        | 1fac5da33e6c48ffb990b6da2ec40020     |
   +-------------------+--------------------------------------+