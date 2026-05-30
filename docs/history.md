---
title: ISCC - History
description: "From a 2016 idea to an international standard: the history of the International Standard Content Code."
authors: Titusz Pan
icon: lucide/history
---

# ISCC - History

The **International Standard Content Code (ISCC)** started as a single idea in 2016. Eight
years later it became an International Standard, **ISO 24138:2024**. This page traces that
path: from an early experiment in content-based identification, through an open-source
prototyping project, to ISO standardization and a role in content provenance and
authenticity.

!!! note "Creator and steward"
    The ISCC was invented by **[Titusz Pan](https://titusz.org)**, who conceived it in 2016 and
    wrote its open-source reference implementation. He served as the **Principal Editor of
    ISO 24138:2024**, authoring the standard's normative text, and is today the **Chairman
    of the [ISCC Foundation](https://iscc.io)**, the non-profit organization that maintains
    and promotes the standard.

## At a glance

| Year      | Milestone                                                                                                                                                                      |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2016      | Titusz Pan conceives the ISCC at Craft AG; the Content Blockchain Project starts, funded by Google's Digital News Initiative                                                   |
| 2017      | ISCC prototyped on the "Coblo" blockchain; first concept document and public specification repository                                                                          |
| 2018      | First open-source release (`iscc` v0.9) and the ISCC 1.0 specification; prototyping project completed                                                                          |
| 2019      | German Digital Publishing Award; ISO/TC 46/SC 9 takes up the ISCC (WG 18 established); ISCC Foundation founded in Leiden                                                       |
| 2020      | ISCC added to the ONIX for Books code lists; the work item is confirmed as NP 24138                                                                                            |
| 2021      | Codebase re-architected into `iscc-core` and `iscc-sdk`; ISO study report on the ISCC                                                                                          |
| 2022-2023 | Working Draft → Committee Draft → Draft International Standard; standardization supported by StandICT.eu                                                                       |
| 2024      | **ISO 24138:2024 published (15 May 2024)**; ISCC registered on the C2PA soft-binding algorithm list; the BioCodes project launches, bringing the ISCC to scientific bioimaging |
| 2025      | WG 18 begins a Technical Report on "soft binding"; the ISCC is referenced across content-provenance and AI-authenticity efforts                                                |

## Origins (2016)

The first ideas about a content-derived, similarity-preserving identifier were developed
in early 2016 by **Titusz Pan** at Craft AG in Freiburg, Germany. The motivation was a
practical gap: digital content is dynamic, granular, and constantly re-encoded as it moves
between systems, yet many media industries had no standard way to identify it, and no
identifier at all for short-lived or user-generated content such as journalism or images.

The core insight was to invert the usual model of media identifiers. Instead of assigning
an identifier to content and tracking that binding by hand, the identifier would be
**derived from the content itself**, so that independent parties could compute the same
code for the same content without consulting any registry.

## The Content Blockchain Project (2016-2018)

Later in 2016, the ISCC found its first home in the **Content Blockchain Project**, a
consortium initiated to research how distributed-ledger technology could serve the content
and media ecosystem. The project received funding from **Google's Digital News Initiative
(DNI)** to build a first prototype.

Within this project the ISCC moved from concept to working code:

- **2017**: The ISCC was prototyped on **"Coblo"**, a media-focused blockchain built on
  MultiChain. The first public concept document and the specification repository (then
  `iscc-specs`, today [`iscc-codes`](https://github.com/iscc/iscc-codes)) were published in
  July 2017. By November 2017 the project reached its milestone for the creation of content
  identifiers.
- **2018**: The first public, open-source release of the reference code was published as
  the [`iscc` Python package](https://pypi.org/project/iscc/) (v0.9), followed by the
  **ISCC 1.0 specification**. In April 2018 the Content Blockchain prototyping project
  reached its final milestone, with all results released under open-source licenses.

This phase established the four foundational components that still shape the standard
today: a Meta-Code, a Content-Code, a Data-Code, and an Instance-Code.

## Recognition and the road to ISO (2019)

In 2019 the ISCC moved from an open-source prototype toward a formal international standard,
and the push came from outside the project. After the Content Blockchain Project released
its results as open source, **Julia Constanze Hahn** of Beuth Verlag, the publishing house
of the German standards body DIN (today DIN Media), came across the work, saw what a
content-derived identifier could do, and reached out to the team. She championed the ISCC
within DIN, whose committee for the description and identification of documents
(NA 009-00-09 AA) took up the proposal and brought it forward to ISO.

- The Content Blockchain Project won the **Startup category of Germany's first Digital
  Publishing Award**, presented under the patronage of the Federal Ministry for Economic
  Affairs and Energy.
- At the annual meeting of **ISO/TC 46/SC 9** (Technical Committee 46, Information and
  documentation; Subcommittee 9, Identification and description) in Ottawa, the ISCC was
  accepted as a work item on the proposal of the German national body (DIN). A dedicated
  working group, **ISO/TC 46/SC 9/WG 18**, was established to develop it and held its first
  meeting on **29 October 2019**, initially convened by **Sabine Rüsch**, who chaired that
  DIN committee.
- The **ISCC Foundation** was established as a non-profit Stichting in **Leiden,
  Netherlands** (founding deed 8 May 2019), by **Sebastian Posth**, **Kira Lemke**, and
  **Titusz Pan**, to provide an independent, neutral home for the standard and its
  open-source implementations.

Throughout 2019 the team presented the ISCC at industry events across Europe, and the
toolkit was extended with identifiers for audio and video content.

## Standardization (2020-2023)

The years after ISO acceptance went into the detailed work of turning a working
specification into an international standard, and into maturing the software.

- **2020**: The ISCC was added to the **ONIX for Books** code lists (from Issue 50), the
  major metadata standard used across the book-publishing supply chain. Within ISO, the
  work item was confirmed as **NP 24138**.
- **2021**: **Titusz Pan** re-architected the reference software from the original
  proof-of-concept into focused, maintainable libraries, most importantly
  [`iscc-core`](https://github.com/iscc/iscc-core) (the reference algorithms) and
  [`iscc-sdk`](https://github.com/iscc/iscc-sdk) (a high-level toolkit). WG 18 delivered a
  study report documenting use cases and adoption interest to SC 9.
- **2022-2023**: The standard advanced through the formal ISO stages: **Working Draft →
  Committee Draft (CD) → Draft International Standard (DIS)**. The `iscc-core` reference
  implementation was aligned to each draft, reaching v1.0.0 in early 2023. This work was
  supported in part by **StandICT.eu** fellowships.

## ISO 24138:2024 (2024)

On **15 May 2024**, **ISO 24138:2024 - Information and documentation - International
Standard Content Code (ISCC)** was published as a first-edition International Standard by
ISO/TC 46/SC 9. **Titusz Pan** served as the **Principal Editor** of the standard, authoring
its normative text.

The standard defines the ISCC as a multi-component, similarity-preserving identifier for
digital content, specifying its codec, header structure, and the algorithms for the
Meta-, Content-, Data-, and Instance-Code units. The reference implementation,
[`iscc-core`](https://core.iscc.codes), provides a conformant, open-source codec under a
permissive license.

NISO, the secretariat of SC 9, introduced the standard to the wider identifier community
shortly after publication.

## Beyond the standard (2024 onward)

With ISO 24138 published, work shifted toward the standard's role in the broader content
ecosystem:

- **Soft binding**: WG 18 began preparing a Technical Report on "soft binding" for
  information identification - re-associating provenance and metadata with content after
  files are re-encoded or stripped of embedded data. The work is coordinated with ISO
  efforts on content provenance.
- **Provenance and authenticity**: Just two days after publication, the ISCC was registered
  on the **[C2PA soft-binding algorithm list](https://github.com/c2pa-org/softbinding-algorithm-list)**
  (17 May 2024), among the first algorithms admitted and the first based on content
  fingerprinting rather than digital watermarking. Within the **C2PA / Content Credentials**
  ecosystem the ISCC works as a soft binding, reconnecting content with its provenance after
  the embedded data has been stripped or re-encoded away. It is also listed
  among the asset-identifier standards in the
  [IEC/ISO/ITU technical report on AI and multimedia authenticity](https://www.worldstandardscooperation.org/what-we-do/amas/2025-press-release/)
  (2025), alongside C2PA Content Credentials and JPEG Trust.
- **Policy and rights management**: As the European Union implements the **AI Act's**
  transparency and text-and-data-mining (TDM) provisions, rights-management organizations have
  pointed to the ISCC as a content-derived basis for machine-readable rights reservations. The
  **International Federation of Reproduction Rights Organisations (IFRRO)** named the ISCC in its
  2026 response to the European Commission's consultation on TDM rights-reservation protocols,
  and the World Intellectual Property Organization (WIPO) had earlier featured it in a 2022
  webinar on copyright in the digital environment.
- **Science and bioimaging**: Launched in November 2024, the
  [BioCodes project](https://bio-codes.io/) brings the ISCC to bioimaging research, using it
  to verify data integrity, detect duplicates, and trace the provenance of scientific images
  across their lifecycle - from raw data through repositories to publication. Funded by the
  European Union through the OSCARS initiative (Horizon Europe grant 101129751), it brings
  together the ISCC Foundation (Titusz Pan), Leiden University (coordinated by **Sylvia Le
  Dévédec**), and German BioImaging (**Josh Moore**).
- **Continued development**: The ISCC Foundation and community continue to extend the
  framework with experimental units such as **Semantic-Codes** (meaning-based similarity)
  and tooling for notarization, registration, and discovery.

## People and credits

The ISCC is the work of a community, but a few roles are central to its history:

- **Titusz Pan** - inventor of the ISCC, principal developer of its open-source reference
  implementation, **Principal Editor of ISO 24138:2024**, and **Chairman of the
  [ISCC Foundation](https://iscc.io)**.
- **Kira Lemke** - co-founder of the ISCC Foundation and current convenor of ISO/TC 46/SC
  9/WG 18.
- **Martin Etzrodt** - director of the ISCC Foundation (since 2025) and a driving force
  behind the BioCodes project, which brings the ISCC to scientific and bioimaging data.
- **Sebastian Posth** - early evangelist and co-founder of the ISCC Foundation, and convenor of
  ISO/TC 46/SC 9/WG 18 through the standard's publication.
- **Sabine Rüsch** - first convenor of ISO/TC 46/SC 9/WG 18 (2019).
- **Gregor Roschkowski** - project manager at DIN who managed the ISCC standardization
  process from the German side, coordinating the national mirror committee for ISO/TC 46/SC
  9/WG 18.
- **Julia Constanze Hahn** - of Beuth Verlag / DIN (today DIN Media), who recognized the
  ISCC's potential and set its path to ISO standardization in motion through DIN.
- **Paul Jessop** - founder of County Analytics and a long-standing contributor to ISO's
  media-identifier standards (ISRC, ISWC, ISNI). Initially critical of the ISCC, he became
  one of its advocates within ISO/TC 46/SC 9/WG 18 and advised on fingerprinting and soft
  binding.

The ISCC Foundation's work has also been guided by an advisory board whose members
contribute expertise across standards, libraries, rights management, publishing, and
research:

- **Roanie Levy** - Licensing and Legal Advisor at the Copyright Clearance Center
- **Todd Carpenter** - Executive Director of NISO
- **Philippe Rixhon** - Valunode, active in EU copyright and AI policy
- **Frank Schulleri** - content licensing and media expert
- **Lambert Heller** - TIB, Leibniz Information Centre for Science and Technology
- **Giacomo D'Angelo** - CEO of StreetLib

These names are only a selection. The ISCC also owes much to the experts of
**ISO/TC 46/SC 9/WG 18**, drawn from national bodies and organizations across many
countries, to the wider open-source community that builds on and around the standard, and
to the many others who have helped along the way.
