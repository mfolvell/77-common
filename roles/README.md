#﻿#  Fellesbibliotek for Axway relatert ansible

## Bakgrunn og innhold
Det som ligger her er roller som brukes flere steder.   De jobbene som skal bruke disse rollene må clone ned innholdet i dette repo lokalt. Det gjøres av sh script som kjøre sekve jobben.   Dette gjøre med følgende kode:
```
rm -rf  ansible-common
mkdir  ansible-common
git clone ssh://git@stash.intern.sparebank1.no:22/axway/ansible-common.git ./ansible-common
```
Til slutt i jobben som kjører ansible må Fellesbibliotek slettes.  Det gjøres slik
```
# # Fjerner lokal copy
rm -rf  ./localGitFolder ./ansible-common
```

### inventories
Det ligger ikke informasjon om hvilke server som rollene i dette repo skal kjøres på. De ligger i hoved jobben som "kaller" på rollene i fellesbibliotek

## Innhold
### Roles
|Navn| Kort beskrivelse | Status|
|--|--|--|
|commonAppConfig_Update | app.config ligger i files folder.  Denne kopieres over og legges inn som default etter at det er tatt backup av den gamle.   **NB -->** instance må restartes for at siste versjon av app.config skal gjelde | **Ferdig** |
|commonCassandra_start | starter opp cassandra databasen | **Ferdig** |
|commonCassandra_stop | stopper cassandra database.    | |
|commonCron_Update | legger inn ny versjon av cron jobb som hører sammen med axway.  I første versjon ligger det cassandra backup her. | Under utvikling |
|commonEnvSettings_Update | alle envSettings er lagt inn her i en ansible template.  Ved kjørring av rollen vil den gamle envSettings.props bli kopiert over til en backup katalog med timestamp i filnavn.  Ansible template vil løses opp og kopieres inn.  **NB -->** instance må restartes for at siste versjon av app.config skal gjelde   | **Ferdig** |
|commonInstances_Start | Starter instance. | **Ferdig** |
|commonInstances_Stop | Stopper instance | **Ferdig** |
|commonNodeMgrCert_Load | Laster default standard sertifikatene som nodemanager trenger.  Dette spesielt ift akksess mot Cassandra | **Ferdig** |
|commonServer_Delete | Sletter server i fra topology.  Dette gjøres ved å bruke domainadmin verktøyet som følger med installasjonen.  Det første som gjøres er å fjerne instance.  Det andre er å fjerne server  | Under utvikling|
|commonServer_Restart | Restart av server ved å gjøre: 1) stop instance. 2) stop nodemanager. 3) start nodemanager. 4) start instance|  | **Ferdig** |
|commonServer_Start |  Start av server ved å gjøre: 1) start nodemanager. 2) start instance|  | **Ferdig** |
|commonServer_Stop | Stop av server ved å gjøre: 1) stop instance. 2) stop nodemanager. |  | **Ferdig** |
