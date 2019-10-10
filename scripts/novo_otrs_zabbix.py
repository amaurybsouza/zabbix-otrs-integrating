#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------ #
# Script Name:   zabbix-otrs-integrate.py 
# Description:   Zabbix
# Author: Janssen dos Reis Lima - janssenreislima@gmail.com
# Maintenance:   Amaury Souza  - amaurybsouza@gmail.com
# ------------------------------------------------------------------------ #
# Usage:         
#       $ /usr/lib/zabbix/externalscripts/zabbix-otrs-integrate.py
# ------------------------------------------------------------------------ #
from otrs.ticket.template import GenericTicketConnectorSOAP
from otrs.client import GenericInterfaceClient
from otrs.ticket.objects import Ticket, Article, DynamicField, Attachment
import sys, os
from zabbix_api import ZabbixAPI
#Zabbix Connection
server = "http://IP/zabbix"
username = "Admin"
password = "zabbix"
conexao = ZabbixAPI(server = server)
conexao.login(username, password)
#OTRS Connection
server_uri = 'http://IP' # IP do servidor web do OTRS
webservice_name = 'integraZabbix' # Nome do webservice importado no OTRS
client = GenericInterfaceClient(server_uri, tc=GenericTicketConnectorSOAP(webservice_name))
client.tc.SessionCreate(user_login='root@localhost', password='senha')
fechar_ticket = Ticket(State='fechado automaticamente')
assunto_artigo_fechado = "Ticket fechado automaticamente atraves do evento " + sys.argv[4]
estado_trigger = sys.argv[6]
artigo_fechar = Article(Subject=sys.argv[2], Body=assunto_artigo_fechado, Charset='UTF8', MimeType='text/plain')
#Open ticket OTRS
def abrirTicket():
    corpo = sys.argv[3] + " " + sys.argv[4]
    evento = sys.argv[4]
    t = Ticket(State='new', Priority='3 normal', Queue='Zabbix', Title=sys.argv[1], CustomerUser='root@localhost', Type='Unclassified')
    a = Article(Subject=sys.argv[2], Body=corpo, Charset='UTF8', MimeType='text/plain')
    df1 = DynamicField(Name='ZabbixIdTrigger', Value=sys.argv[5])
    df2 = DynamicField(Name='ZabbixStateTrigger', Value=sys.argv[6])
    df3 = DynamicField(Name='ZabbixEvento', Value=sys.argv[4])
    ticket_id, numero_ticket = client.tc.TicketCreate(t, a, [df1, df2, df3])
    conexao.event.acknowledge({"eventids": evento, "action": 2, "message": "O ticket Nº " + str(numero_ticket) + " foi criado com sucesso no OTRS."})
    conexao.event.acknowledge({"eventids": evento, "action": 4, "message": "O ticket Nº " + str(numero_ticket) + " foi criado com sucesso no OTRS."})
#Close ticket OTRS
def fecharTicket():
    df_searchId = DynamicField(Name='ZabbixIdTrigger', Value=sys.argv[5], Operator='Like')
    df_searchState = DynamicField(Name='ZabbixStateTrigger', Value=sys.argv[6], Operator='Like')
    busca_df=client.tc.TicketSearch(OwnerIDs=1,Queues='Zabbix', dynamic_fields=[df_searchId])
    client.tc.TicketUpdate(ticket_id=busca_df[0], ticket=fechar_ticket, article=artigo_fechar)
    conexao.event.acknowledge({"eventids": evento, "action": 2, "message": "O ticket Nº " + str(numero_ticket) + " foi fechado com sucesso no OTRS."})
    conexao.event.acknowledge({"eventids": evento, "action": 4, "message": "O ticket Nº " + str(numero_ticket) + " foi fechado com sucesso no OTRS."})
if estado_trigger == "OK":
    fecharTicket()
else:
    abrirTicket()
