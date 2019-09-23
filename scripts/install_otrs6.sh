#! /usr/bin/env bash
# ------------------------------------------------------------------------ #
# Script Name:   install_otrs6.sh
# Description:   Show informations about machine hardware.
# Written by:    Amaury Souza
# Maintenance:   Amaury Souza
# ------------------------------------------------------------------------ #
# Usage:
#       $ ./install_otrs6.sh
# ------------------------------------------------------------------------ #
# Bash Version:
#              Bash 4.4.19
# ------------------------------------------------------------------------ #


#Starting script

yum update -y
yum install net-tools vim epel-release -y 

#Disable SElinux firewall

sudo sed -i 's/enforcing/disabled/g' /etc/selinux/config /etc/selinux/config

#Install MariaDB Server and Apache Web Server

yum install httpd httpd-devel gcc mariadb-server -y
systemctl start httpd
systemctl enable httpd
echo 
"max_allowed_packet=64M
query_cache_size=32M
innodb_log_file_size=256M
character-set-server=utf8
collation-server=utf8_unicode_ci" >> /etc/my.cnf 
systemctl start mariadb
systemctl enable mariadb
mysql_secure_installation

#Install Community Edition OTRS 6 

yum install https://ftp.otrs.org/pub/otrs/RPMS/rhel/7/otrs-6.0.17-01.noarch.rpm -y
systemctl restart httpd

#Allow http & https ports in OS firewall

firewall-cmd --permanent --add-service=http
firewall-cmd --permanent --add-service=https
firewall-cmd --reload


yum install "perl(Crypt::Eksblowfish::Bcrypt)" "perl(DBD::Pg)" "perl(Encode::HanExtra)" "perl(JSON::XS)" "perl(Mail::IMAPClient)" "perl(Authen::NTLM)" "perl(ModPerl::Util)" "perl(Text::CSV_XS)" "perl(YAML::XS)" -y

#Checking for modules... 

/opt/otrs/bin/otrs.CheckModules.pl




