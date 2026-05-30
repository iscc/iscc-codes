title: ISCC - International Standard Content Code - ISO 24138
description: The intelligent digital media identifier.
authors: Titusz Pan

# ISCC - International Standard Content Code

## A Modern and Open Content-Based Identifier

![iscc-sample](images/iscc-algo-design.svg)

## The ISCC is...

- a universal identifier for all types of digital content (text, image, audio, video)
- a lightweight and similarity-preserving fingerprint
- designed for cross-sector applicability (journalism, books, music, film, etc.)
- designed to identify content in decentralized and networked environments
- and most importantly it is free, open-source and transparent

## Try out the ISCC

- https://demo.iscc.io
- https://huggingface.co/spaces/iscc/iscc-playground

## Developer entry points

- [iscc-core](https://github.com/iscc/iscc-core) — current Python reference implementation of the ISO 24138 core algorithms
- [iscc-sdk](https://github.com/iscc/iscc-sdk) — high-level Python toolkit for generating ISCCs from media files


!!! note "ISCC Standard - ISO 24138"
    ### Latest status of standardization:
    [ISO 24138 - Information and documentation - International Standard Content Code (ISCC)](https://www.iso.org/standard/77899.html)
    ### Current implementation guidance:
    [ISCC - Codec & Algorithms](https://core.iscc.codes) and [ISCC Software Development Kit](https://sdk.iscc.codes)



## Motivation

Increasing amounts of dynamic, short-lived, and granular content need to be managed and require new and innovative tools.

A crucial prerequisite for content-related transactions to succeed in this new and demanding environment is the capability to address and identify content efficiently. Yet many industries that deal with digital content do not even have standard identifiers. There is no existing solution for those industries that deal with short-lived or granular content such as journalism. There is also no widely adopted standardized identifier for digital images.

The overhead and cost of manually assigning and tracking identifiers for such content are prohibitive. But there is a solution to the problem: **auto-generated identifiers** created algorithmically from the content itself.

In a multi-sided ecosystem, **anybody** may have a legitimate interest to generate, lookup, or register an identifier for some digital content – whether they own the content or not.

Authorship or copyright is **not** a requirement to create or use an identifier. But **an identifier is a requirement** to communicate and agree on authorship, origin, copyright, and other information.

Technology allows us to map **identifiers to digital content** without requiring an
intermediary by using open, standardized fingerprinting algorithms.

Open and accessible **standard identifiers**, designed to manage small and sometimes transient pieces of digital content are fundamental for transactions and sales activities in our increasingly heterogeneous media environment.

By using standardized, decentralized, algorithmic identifiers for digital content, all ecosystem participants can engage more efficiently in content-related transactions.

## Key Features and Differentiators

- Decentralized issuance through algorithmic creation
- Generic content identification (text, images, audio, video)
- Algorithmic similarity detection and deduplication
- Low management costs
- Low barrier of entry

## How it works

**ISCC** identifiers are generated algorithmically **from the content itself**. Content files are processed to build the identifier. The ISCC does not have to be manually assigned, neither does it have to be carried around or embedded within the content. The content itself is the source and authority of the **ISCC-CODE**.

The **ISCC-CODE** is a unique, hierarchically structured, composite identifier. It is built from a generic and balanced mix of content-derived, locality-sensitive and similarity-preserving hashes generated from metadata and the content itself.

