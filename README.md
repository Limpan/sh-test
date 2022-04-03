Filformat:

P|förnamn|efternamn
T|mobilnummer|fastnätsnummer
A|gata|stad|postnummer
F|namn|födelseår
P kan följas av T, A och F
F kan följas av T och A


Exempel:

P|Victoria|Bernadotte
T|070-0101010|0459-123456
A|Haga Slott|Stockholm|101
F|Estelle|2012
A|Solliden|Öland|10002
F|Oscar|2016
T|0702-020202|02-202020
P|Biden|Joe
A|White House|Washington, D.C


Ger XML som:

<people>
  <person>
    <firstname>Victoria</firstname>
    <lastname>Bernadotte</lastname>
    <address>
      <street>Haga Slott</street>
      ...
     </address>
    <phone>
      <mobile>070-0101010</mobile>
      ...
    </phone>
    <family>
      <name>Estelle</name>
        <born>2012</born>
        <address>...</address>
     </family>
     <family>...</family>
  </person>
  <person>...</person>
</people>
