## PROJETO DE INTEGRAÇÃO DO ZABBIX COM OTRS (TICKET TOOL)

- Eu vou demonstrar o projeto usando scripts (Bash), é uma forma automatizada de instalar as aplicações. Depois será abordado o uso do Ansible para gestão de configuração nos hosts remoto, onde criarei uma playbook para promover um ambiente automatizado.

### Etapa 1 - Preparação do ambiente para instalação do OTRS 6

- Utilizar o script (install_otrs.sh) para instalação da aplicação de tickets.

- Utilizar o script (install_zabbix.sh) para a instalação da aplicação de monitoramento.

### Etapa 2 - Instalação de dependências no sistema

- Vamos utilizar o seguinte cenário para esse projeto:
  - CentOS 7
  - Zabbix 3.4
  - OTRS 6
  - Python 2.7
  
  - # yum install python-pip
  - # pip install python-otrs
  - # pip install zabbix-api

### Etapa 3 - Download de pacote

- Você deve fazer o download do pacote Bundle no site do OTRS (Bundle - OTRS::ITSM 6 Patch Level 22)

  - https://community.otrs.com/download-otrs-community-edition/ ou siga a página abaixo:
  
  
![otrs-down.png](images/otrs-down.png)


### Etapa 4 - 





### Etapa 5 - 






