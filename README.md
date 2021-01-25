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
Alle rollene er har navn som skal være selvforklarende.   Det er ikke nødvendig med mere info.  