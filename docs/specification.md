---
title: ISCC - Specification
description: The ISCC specification — ISO 24138:2024 and the community ISCC Enhancement Proposals (IEPs).
authors: Titusz Pan
icon: lucide/book-open
---

# ISCC - Specification

The ISCC is specified at two complementary levels. **ISO 24138:2024** is the authoritative
International Standard that fixes the normative core. The **ISCC Enhancement Proposals
(IEPs)** are the open community specification process that documents the standard in detail
and develops new functionality. The open-source reference implementation connects the two.

!!! note "ISCC Standard - ISO 24138:2024"
    [**ISO 24138:2024 - International Standard Content Code (ISCC)**](https://www.iso.org/standard/77899.html)
    is the authoritative specification of the ISCC.

## ISO 24138:2024 — the International Standard

ISO 24138:2024 was developed under **ISO/TC 46/SC 9/WG 18** and published on 15 May 2024 as
the first-edition International Standard for the ISCC. It is the authoritative, normative
specification.

The standard defines the ISCC as a multi-component, similarity-preserving code for
digital content and specifies:

- the **ISCC-CODE** structure — a self-describing header (MainType, SubType, Version, and
  Length) and a composite body assembled from one or more **ISCC-UNITs**;
- the **Meta-Code** — similarity of the content's metadata;
- the **Content-Code** — perceptual and structural content similarity, with per-modality
  algorithms for Text, Image, Audio, Video, and Mixed content;
- the **Data-Code** — similarity of the raw bitstream;
- the **Instance-Code** — exact data identity via a cryptographic checksum.

ISO 24138:2024 also carries a normative annex, **Annex D, "Reference implementation"**. The
reference software is published as a freely available **electronic insert** to the standard at
<https://standards.iso.org/iso/24138/ed-1/en/>. It is *normative* in a precise sense: any
conforming implementation, given the same conformant input, must produce the same output as
the reference software. Implementations need not reuse its algorithms or programming
techniques, and the reference software cannot add anything to the standard's textual technical
description. The code of this electronic insert is maintained as the open-source
[`iscc-core`](https://github.com/iscc/iscc-core) library.

- [ISO 24138:2024 at ISO](https://www.iso.org/standard/77899.html) — the full standard text
- [Reference software — electronic insert](https://standards.iso.org/iso/24138/ed-1/en/) — freely available

## Enhancing the standard — the ISCC Enhancement Proposals

ISO 24138:2024 is a complete working specification, and future editions are expected to add
functionality, track the state of the art, address security concerns, and retire deprecated
features. Annex C of the standard names the channel for this work:

> A process to structure and substantiate proposals to enhance ISCC is maintained by the
> ISCC community. \[…\] The ISCC community is gathering ISCC enhancement proposals at
> <https://github.com/iscc/iscc-ieps>.

The **ISCC Enhancement Proposals (IEPs)** are design documents that describe a feature of the
ISCC system or provide information about its processes and environment. They are the detailed,
openly developed working specifications of the ISCC community, and the route through which new
work is substantiated before it can feed into a future edition of the standard.

- **Rendered specifications:** <https://ieps.iscc.codes>
- **Source repository:** <https://github.com/iscc/iscc-ieps>

### How the IEP process works

The process is itself defined in an IEP (IEP-0000). In outline:

1. **Idea and discussion** — a champion develops the idea and fosters public discussion.
2. **Draft submission** — the proposal is submitted as a pull request to
   [`iscc/iscc-ieps`](https://github.com/iscc/iscc-ieps).
3. **Editor review and numbering** — an editor assigns a number and category and checks that
   the proposal is sound, complete, and motivated.
4. **Iteration** — the author refines the draft through further pull requests.

IEPs are categorized as **Core** (changes affecting most implementations; require both a
design document and a reference implementation), **Informational**, or **Process**. Each IEP
moves through a status workflow of `Draft → Proposed → Stable → Obsolete`, with side paths for
`Deferred`, `Withdrawn`, and `Rejected` proposals.

### IEPs and the scope of ISO 24138

Several IEPs were contributed as input to ISO/TC 46/SC 9/WG 18, and the corresponding
normative material was published in the standard. Others document ongoing community work that
extends beyond the current edition.

- **Within the normative scope of ISO 24138:2024** — the ISCC structure, the standardized
  ISCC-UNITs (Meta-, Content-, Data-, and Instance-Code), the composite ISCC-CODE, and ISCC
  metadata.
- **Beyond the current standard** — work such as the ISCC-ID, decentralized content
  registries, the ISCC DID method, and experimental Semantic-Codes. These may inform a future
  edition but are **not** part of ISO 24138:2024 today.

When precision matters, treat "contributed as input to ISO" and "published in the standard" as
distinct claims, and consult the published standard for the definitive normative scope.

## Open-source software

The specifications are made executable and verifiable through open-source software, released
under permissive licenses:

- [**`iscc-core`**](https://core.iscc.codes) — the reference implementation of the
  standardized codec and fingerprinting algorithms. Its code is the reference software
  published as the normative electronic insert of ISO 24138:2024, and the foundation for all
  ISCC generation.
- [**`iscc-sdk`**](https://sdk.iscc.codes) — the high-level Python toolkit and primary
  integration entry point. It builds on `iscc-core` and adds content-type detection, metadata
  extraction and embedding, and content extraction so applications can produce a full
  ISCC-CODE directly from a media file.

```python
import iscc_sdk as idk

# Generate a full ISCC-CODE from a media file
iscc_meta = idk.code_iscc("example.jpg")
print(iscc_meta.iscc)
```

## Historical specification drafts

Before standardization, the ISCC was developed as a public working specification by Titusz Pan
within the [Content Blockchain Project](https://content-blockchain.org). These
early drafts predate ISO 24138:2024 and current implementations. They are **superseded** and
retained for historical reference and URL continuity only:

- [ISCC Specification v1.x](legacy/specification.md) — the archived working draft (formerly
  published at this page).
- [ISCC Specification v1.0](https://github.com/iscc/iscc-codes/blob/version-1.0/docs/specification.md)
  — the 2018 draft, on the `version-1.0` branch.

For the history of how these drafts became an International Standard, see the
[History](history.md) page.
