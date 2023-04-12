source_files
------------

Les lexiques utilisés par l'application doivent être ajoutés dans ce dossier. Il n'est pas permis de redistribuer publiquement plusieurs de ces lexiques, même si leur utilisation non-commerciale est permise. C'est pourquoi nous donnons le nom des fichiers et une indication sur comment les obtenir :

- `French-fr-NRC-Emotion-Intensity-Lexicon-v1.txt` : Partie du lexique [NRC-EI](http://saifmohammad.com/WebPages/AffectIntensity.htm) par Saif Mohammad (2018). Le fichier est trouvé dans la [distribution](http://saifmohammad.com/WebDocs/Lexicons/NRC-Emotion-Intensity-Lexicon.zip), dossier `OneFilePerLanguage`.
- `French-fr-NRC-VAD-Lexicon.tsv` : Partie du lexique [NRC-VAD](http://saifmohammad.com/WebPages/nrc-vad.html) par Saif Mohammad (2018). Le fichier est trouvé dans la [distribution](http://saifmohammad.com/WebDocs/Lexicons/NRC-VAD-Lexicon.zip), dossier `OneFilePerLanguage` 
- `ELAL_all.tsv`: [ELAL](https://hal.science/hal-03655148), lexique d'émotions pour l'alsacien par Delphine Bernhard. Puisque les scores d'émotion sont en partie dérivés du lexique NRC, le fichier ne peut pas être distribué directement. Il peut être reconstitué sur la base des deux ressources suivantes :
    - https://doi.org/10.34847/nkl.40cex998 : Variantes scriptolinguistiques pour les termes alsaciens. La colonne `variantes` doit être renommée en `als`. Cette colonne est la première colonne du fichier reconstitué.
    - https://doi.org/10.34847/nkl.39b7617v : Scores d'émotion pour les mêmes termes (colonnes restantes pour le fichier reconstitué)

Concernant les autres fichiers, déjà présents dans le dossier :

- `FEEL.csv` : Lexique [FEEL](http://advanse.lirmm.fr/feel.php) par Abdaoui et al. (2016).
- `fr_hmr.txt` et `al_hmr.txt` : Font partie de la mécanique d'application des lexiques aux textes d'entrée
