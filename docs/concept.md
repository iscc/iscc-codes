---
title: ISCC - Concept
description: The idea behind the ISCC — identifying digital content by what it is, and describing sameness in layers.
authors: Titusz Pan
icon: lucide/lightbulb
---

# ISCC - Concept

This page explains the idea behind the **ISCC** — how it thinks about digital
content and about what it means for two files to be "the same." The
[Capabilities](capabilities.md) page describes what the ISCC can do; this page
explains *why it is shaped the way it is*.

## "The same" is not one thing

Digital content never stops moving. As a file travels between systems it is
re-encoded, resized, recompressed, and copied. Each step rewrites the underlying
bytes, yet to a person the content is unchanged: a photo exported at three
resolutions, a manuscript saved as PDF, EPUB, and Word, or a song offered in
several audio formats are all "the same thing."

The catch is that *sameness* has more than one meaning:

- A resized photo is the **same picture**, but not the **same file**.
- A translated article carries the **same meaning**, but not the **same words**.
- A re-saved document may be the **same bytes**, or differ by a single character.

So "are these the same?" has several valid answers at once, and a single label
attached to a work cannot capture them all. The ISCC is built around this
observation: it describes content at several levels and keeps them separate, so a
system can tell not just *whether* two assets are related, but *how*.

!!! abstract "In plain terms"
    The ISCC is a digital fingerprint calculated from a file's own content.
    Identical files share the same code, and similar files get similar codes.
    Anyone can compute it with open software and get the same result, with no
    central registry involved.

## A code read from the content

Most identifiers are *assigned*: an authority issues an ISBN or DOI and attaches
it to a work. The ISCC inverts this. It is **derived from the content itself** by
running the open algorithms defined in
[ISO 24138:2024](https://www.iso.org/standard/77899.html). The code is a function
of the data, so unrelated parties can independently compute the *same* ISCC for
the *same* content, and the code references that content without implying anything
about ownership.

Reading the code from the content is also what makes it *similarity-preserving*:
when the content changes a little, the code changes a little. A re-compressed
image or a transcoded audio file produces a code that stays recognizably close to
the original, even though the raw bytes differ. That is the bridge across the gap
that re-encoding and resizing create.

## Identification in layers

The ISCC describes a piece of content on a spectrum, from the **abstract** idea
at the top down to the **concrete** bytes at the bottom. Each level is captured by
its own **ISCC-UNIT**, and the units combine into a single composite
**ISCC-CODE**.

| Layer        | What it identifies                                   | ISCC-UNIT                  |
| ------------ | --------------------------------------------------- | -------------------------- |
| **Creation** | the work as an idea, via its title and metadata     | Meta-Code                  |
| **Meaning**  | the concepts it conveys, across wording and language | Semantic-Code *(reserved)* |
| **Content**  | what you read, see, or hear — independent of format | Content-Code               |
| **Data**     | the encoded file as a stream of bytes               | Data-Code                  |
| **Instance** | this one exact file, down to the last bit           | Instance-Code              |

The upper layers describe the *content* — what it is and what it means; the lower
layers describe the *data* — how it happens to be stored. The **Content-Code**
applies a dedicated algorithm per media type (Text, Image, Audio, Video, and
Mixed). A complete ISCC-CODE always includes the Data-Code and Instance-Code,
with the other units added when they are available.

!!! note "Semantic-Code"
    ISO 24138:2024 reserves the **Semantic-Code** layer (sameness of *meaning*)
    but does not yet define its algorithm. Experimental implementations exist for
    text ([iscc-sct](https://github.com/iscc/iscc-sct)) and images
    ([iscc-sci](https://github.com/iscc/iscc-sci)).

## Kinds of sameness

The layers correspond to a few independent kinds of similarity. Two files can be
alike on one and differ on another, and the ISCC keeps each kind separate:

- **Data similarity** — nearly the same bytes. *"Almost the same file."*
- **Content similarity** — the same once decoded and perceived, regardless of
  format, compression, or minor edits. *"Looks, reads, or sounds the same."*
- **Semantic similarity** — the same meaning, including paraphrase and across
  languages. *"Means the same thing."* (reserved; not yet standardized)

A separate axis, **metadata similarity**, compares how content is *described* —
its title and description — rather than the content itself.

Set apart from all of these is **data identity**: the Instance-Code is not a
similarity measure but an exact, bit-for-bit checksum. It does not ask "how
similar?" — it answers "is this the very same file?" with yes or no.

## Whole works and their parts

Sameness can be judged for an entire work or for parts of it. Two articles may
share a single quoted paragraph; two recordings may share one sampled passage.
A *global* comparison asks whether two works match overall, while a *granular*
comparison finds matching segments within them. The ISCC supports both, so
partial overlap, quotation, and reuse can be detected — not only whole-file
duplicates.

## Design principles

The ISCC is deliberately kept simple and broadly useful. A few principles guide
its design:

- Target real, unsolved content-identification problems.
- Derive codes algorithmically, with no central authority required.
- Stay generic across media types, sectors, and use cases.
- Keep the standard pragmatic and simple to implement.
- Remain extendable and forward-compatible.
- Build on open specifications and open-source software.
- Complement existing identifiers rather than replace them.

## Where to go next

- [Capabilities](capabilities.md) — what the ISCC can do in practice.
- [Specification](specification.md) — ISO 24138:2024 and the community IEPs.
- [Resources](resources.md) — software, demos, and tools for generating ISCCs.
