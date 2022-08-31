#### Bugs:

##### Bugs caused by xml file:

1. Fichier pas bien forme, peut pas construire l'arbre xml:
```shell
greber-d-jumpfer-prinzesse.xml  xml.etree.ElementTree.ParseError: not well-formed (invalid token): line 8, column 46
greber-lucie.xml xml.etree.ElementTree.ParseError: not well-formed (invalid token): line 8, column 74
```
Le problem est à cause de l'encodage, dans ces deux articles,
```xml
<?xml version='1.0' encoding='utf8'?>
, utf8 est utilisé au lieu de UTF-8, donc les lettres comme ü, ß ne peuvent pas être lu.
```

##### Old bugs fixed:

1. parfois, il y a des tags sans attributs:
par exemple dans <personGrp>
```xml
<personGrp xml:id="alli" sex="UNKNOWN">
  <persName>Alli</persName>
</personGrp>

<personGrp>
  <persName>Zwei Page, Mickeymies, hochi Staatsbeamti, Diener un Dienere biem Maharadscha, e
  Drache</persName>
</personGrp>
```

3. (fixed) Dans arnold-der-pfingstmontag, 
```xml
<person xml:id="christinel" sex="F">
<sp who="#christinle">
<speaker>Christinel</speaker>
<stage>eintretend</stage>
```
Le nom de personnage est different <sp who="#christinle">, <speaker>Christinel</speaker>, je prends "christinel" comme le vrai nom


```xml 
<sp who="#rosine #prechtere">
    <speaker>Fr. Rosine, Fr. Prechtere</speaker>
    <stage>zugleich</stage>
    <l>Guede Daa, Frau Bas. Isch Si wohl uf?</l>
</sp>
```
double id in <sp>, problem fixed

