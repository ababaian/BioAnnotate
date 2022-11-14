## Creating annotation matrix

Part of the meta data contained in BioSample XML data are attributes (“tags”) and corresponding text (“values”).

From the [BioAnnotate spreadsheet](https://docs.google.com/spreadsheets/d/1J-kYYDBv3K5HFYMiHhSseEcpW8TQ3ilbSxfynXNtzKo/), a [Body_site Matrix](https://docs.google.com/spreadsheets/d/1pFDiM9vZkttKOMPB8Es7HAro46TF3-ps/edit?usp=sharing&ouid=111190611970066466857&rtpof=true&sd=true) (rows 2-250 on the `matrix` sheet) was created with tags that were `T` for the `body_site` data class.

The annotation system, displayed on the `BRENDA` sheet, was based on the [BRENDA Tissue Ontology (BTO)](https://www.ebi.ac.uk/ols/ontologies/bto) which was chosen for its hierarchal system that groups terms into organ systems, anatomical structures, tissue and cell types, and derived cell lines. The ontology originated from the BRaunschweig ENzyme Database and helpfully encapsulates animals, fungi, and plants.

After the first annotation pass, tags that could be classified into the ontology were considered Level 1 terms. Tags that were not informative were omitted from the matrix (see `tags_sorted` sheet), and tags that were too general but whose value may contain tissue or organ information were moved to a list on the `needs_value_lookup` sheet.

BioSample XML data was downloaded from NCBI and the 80 GB file was split using [XML_breaker.py](https://gist.github.com/nicwolff/b4da6ec84ba9c23c8e59) into files containing 1,000,000 BioSample elements so that the value lookup could be done locally.

From the XML files, values were pulled for attributes that matched the tags on the `needs_value_lookup` list. Values were filtered to remove integers and some special characters were removed/replaced for consistency with the original BioAnnotate spreadsheet.

To check how promiscuous the Level 1 terms are when conducting a string search, the Level 1 terms were cross-referenced against the list of unique values and the frequency for each term was calculated. The results can be viewed in the [Cross-reference spreadsheet](https://docs.google.com/spreadsheets/d/1pyRJH8HhSYFXZt4E7T20Fr3044lInH87/edit?usp=sharing&ouid=111190611970066466857&rtpof=true&sd=true) on the `frequency` sheet. Values that are informative will later be classified as Level 2 terms.

## Extending the matrix

All BTO terms were pulled from the downloadable .owl file. Umbrella terms such as "has_exact_synonym" and those relating to culture conditions or language were omitted.

BTO terms were added to the `matrix` of Level 1 terms (rows 251 and onward) and need to be annotated according to the existing ontology categories *i.e.* columns.

### Tips for annotating:

1. As the focus of this annotation layer is human organ systems, some tissue types have been annotated with more specificity than others. For each Level 1 term, annotate according to the most specific ontology category possible.
    - *E.g.* “blood” is marked `T` for **blood**; “hippocampus” is marked `T` for **forebrain**; "bulb" is marked `T` for **whole_plant**.

2. Some terms will fall under multiple categories.
    - *E.g.* “uterine_endometrial_stromal_cell” is marked `T` for **connective_tissue** and **uterus**; “breast_cancer_cell” is marked `T` for **cancer** and **breast**.

3. There are 6214 BTO terms, so it is easiest to start at the top of one tree in the ontology viewer and systematically work downwards through each node, `Crtl+F` to find each term in the `matrix` and changing the text from purple to black when done.
    - The sheet `bto_nodes_wip` tracks the annotation progress.
    - For the terms, dashes and spaces have been replaced by underscores while periods, slashes, and parentheses have been left intact.

