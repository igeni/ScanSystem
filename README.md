# Scanner system 

This scanner app built as universal and flexible platform for scan data from online resources. 

---
## Features
- Global and detailed config settings
    - System can be flexibly configured without changing code (zero code config)
    - Customer can configure all parts of system such as 
    - global settings like a timezone, proxies list & user_agent settings and theirs rotation rules, cache settings and so on
    - log target, log's rotation rules, format etc.
    - scan rules and data normalization settings
    - storage setting, easy to change storage to different type, like SQL or NoSQL storage
    - easy to add new types of crawlers regarding universal interface
    - chose your own system wide timezone
    - monitoring settings (i'm alive reports)
    - auto-recovery after server crash settings

- Universal Transport Layer
    - System wide support of proxies (including rotation proxies by Round Robin algorithm during scan process). Can be disabled any time by customer.
    - System wide support of substitution User Agents while running (by Round Robin algorithm). Can be disabled any time by customer.

-  Storages
    - easy to change storage 
    - can support different storage types (like sqlite, postgres, redis,..)

-  Logs
    - use your own storage for logs
    - short information about successful scans and detailed debug info about failed scans
    - set up log rotation and log compression conditions to keep storage free  

-  Crawlers
    - add easily own crawlers by unified crawlers interface
    - configure all crawler's settings separately if you need with config file
    - polite scheme of scanning data to prevent blocking
    - configure scan parameters like scan interval or delays between requests

- Anti-scan protection
    - To avoid anti-scan mechanisms of websites system use connections with the proxies and rotation of User Agent identification   

- Avoid extra requests from the websites by using polite mechanisms of downloads

- Auto-recovery after server crash
    - In case of server unexpectedly crash next start of scanner system will recover own state and system idempotency
    - No extra downloads when something went wrong

- Flexible configured i-am-alive reports to outer service

- Use docker to start system in container

- All code covered by tests
---


## Settings
System-wide settings stored in settings.cfg file and have detailed descpiptions

## Transport Layer
Add proxies lines to file list_proxy.cfg and set up option RotateProxies = yes in section 'CRAWLER.*' to uses rotating proxies mechanism.
Also you can add User Agents strings to file list_user_agents.cfg and set up RotateHeaders = yes in the same section to enable UA rotating tool. 
In this case every connection will be established throught new ip with new UA parameter.

## Anti-scan protection
Use RotateProxies = yes and RotateHeaders = yes like it described in the 'Transport Layer' section to activate anti-scan protection mode 

## Logs
Set up parameters in the LOGS sectin of the settings.cfg file 
    
## Storages
System uses realisation independent storage interface so you can easily add new type of storage to system without any dificulties
To add new storage just add new class inherited from StorageInterface and swith on connection in the Storage class (storages/storage.py).  

## Crawlers
System uses realisation independent crawlers interface and you can add new crawler easily. Add new crawlers class inherited from CrawlerInterface and plug it to Crawler class (crawlers/crawler.py)
Scanner uses his own mechanism to decrease load into target's website by preventing repeated requests 
    
## Data normalisation
Scanner system use DataStructure class (common.py) to unify sheduler of tasks. All datum will be normalize automaticaly
Add your own rules in the 'RULES' section

## Monitoring
Every ScanNewTasksInterval seconds system send alive status to AliveStatusURL ('CRAWLER.*' section of settings.cfg file). Option can be disabled

## Auto-recovery
If something went wrong (for example k8s restart destroyed and created instance) scanner system can obtain own previous state automaticaly. Of course you have to use storage outside your instance

---