# BioAnnotate
Annotation-layer for the INSDC BioSample database

## Motivation
The [BioSample](https://www.ncbi.nlm.nih.gov/biosample/) database contains descriptive meta-data for all _biological samples_ housed by the "International Nucleotide Sequence Database Collaboration", the world's central repository for biological sequence data.

Due to the diversity of available samples and their descriptions, the meta-data is not standardized. Each record is stored as an XML file, containing its own set of tags and values.

`BioAnnotate` provides an annotation layer for `BioSample` to aggregate similar tags and standardize the value formats.

## Goal
There are `42,125` unique 'tags' across >10.7 million BioSample XML files. We will annotate these tags into 4 categories, to allow for data-aggregation and ultimately a "clean" database.

- `geo`:  Geographic names and spatial coordinates
- `date`: Sample collection date and/or release date
- `organism`: Host or Pathogen species
- `ecosystem`: Environmental origin description or body-site

# Contributing

We will work on a collaborative ![Annotation Spreadsheet](https://docs.google.com/spreadsheets/d/1J-kYYDBv3K5HFYMiHhSseEcpW8TQ3ilbSxfynXNtzKo/edit?usp=sharing) which contains every unique BioSample tag.

Sign-up on the `Lockout` sheet to annotate a 'chunk' of 2,500 rows in the `biosample_tags` sheet for a particular class of data (see below).

The default for all tags is set to `F` for "FALSE". If a `biosample_tag` describes a field which is pertinent to your data-class, change this value to `T` for "TRUE".

If you are unsure of how to classify a particular `biosample_tag`, set the value to `?`

### Example Workflow

Kat would like to annotate Chunk `C` for `geo` data.

1. She reviews the `geo` data class description below to understand the inclusion and exclusion criteria for this data-class.

2. She enters her name on the `Lockout` sheet to indicate she has begun to work on this chunk.

3. On the `biosample_tags` sheet Chunk corresponds to Rows `5001 - 7500` and the `geo_name` and `geo_coord` columns.

4. After turning on some good jams, she annotates these rows.

5. Upon completing her annotation, she updates `Lockout` to indicate this chunk is complete and she can begin working on another Chunk.

## Data Classes

### `geo` data

`geo_name` :

`geo_coord` :

### `date` data

`collection_date` :

`other_date` :

### `organism` data

`host_species` :

`virus_species` :

### `ecosystem` data

`ecosystem` :

`bodysite` :
