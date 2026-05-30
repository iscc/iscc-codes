title: ISCC - Resources
description: ISCC software, demos, tools, developer libs, integrations, presentations, articles and other resources
authors: Titusz Pan

# ISCC - Resources

If you find something that is missing from this collection of resources for the ISCC, [please add it](https://github.com/iscc/iscc-codes/edit/main/docs/resources.md).

## ISCC - Official Software & Tools

### [iscc-core](https://github.com/iscc/iscc-core)

Current Python reference implementation of the ISCC core algorithms defined by [ISO 24138:2024](https://www.iso.org/standard/77899.html). Install from PyPI with `pip install iscc-core`. Documentation: <https://core.iscc.codes/>.

### [iscc-sdk](https://github.com/iscc/iscc-sdk)

High-level Python toolkit for creating and managing ISCCs from media files. It builds on `iscc-core` and adds media type detection, metadata handling, content extraction, and a command-line interface. Install from PyPI with `pip install iscc-sdk`. Documentation: <https://sdk.iscc.codes/>.

### [ISCC Web Demo](https://demo.iscc.io/)

Minimal web application for generating ISCCs in the browser. Source code: [iscc-web](https://github.com/iscc/iscc-web).

### [ISCC Codes](https://github.com/iscc/iscc-codes)

Source repository for this `iscc.codes` documentation site and historical ISCC Version 1.1 specification material. The legacy Python package [`iscc`](https://pypi.org/project/iscc/) is an outdated proof-of-concept retained for compatibility; new integrations should use `iscc-core` or `iscc-sdk`.

## ISCC - Third-Party Implementations

### [ISCC-RS](https://github.com/iscc/iscc-rs)

Rust implementation of the [ISCC specification](https://iscc.codes/specification).

### [ISCC-RS-CLI](https://github.com/iscc/iscc-rs-cli)

Command-line tool based on the [iscc-rs](https://github.com/iscc/iscc-rs) library.

### [ISCC-GOLANG](https://github.com/coblo/iscc-golang)

Golang implementation of the ISCC protocol.

### [ISCC-DOTNET](https://github.com/iscc/iscc-dotnet)

C# .Net Core implementation of the ISCC protocol.

## ISCC - Technical Demos & Integrations

### [Web Demo](https://iscc.coblo.net/)

A demo web application that can generate and lookup ISCC codes from files or URLs and visualizes differences between ISCC Codes. The [source code](https://github.com/coblo/iscc-demo) is also available.

### [Data Streams](https://explorer.coblo.net/streams/)

The Content Blockchain Testnet is running a public data-stream of ISCC codes for testing and demonstration purposes. The web demo uses the [ISCC data-stream](https://explorer.coblo.net/stream/iscc) for lookups.

### [Clink.ID](https://clink.id/)

[CLink.ID](https://clink.id/) is an interoperable registry, architected to recognize identifiers and meta-data regardless of whether they are Handle- or content-based and/or block-chain inspired. CLink.ID is operated by [CLink Media , Inc.](https://clink.media/) and has integrated [ISCC in its registry](https://clink.id/#objects/20.500.12200.100/5d8e3c3f9d6c6a759261).

### [Smart License Demo](https://smartlicense.coblo.net/)

Prototype demo of a smart licensing framework that uses ISCC codes for content identification. [Source code](https://github.com/coblo/smartlicense) is also available.

### [Blockchain Wallet Demo](https://github.com/coblo/gui-demo)
An early prototype demo of a blockchain wallet that uses ISCC codes for license tokenization.

## ISCC - Presentations & Articles

### [Blockchain for Science Conference (Berlin, 2019)](https://www.youtube.com/watch?v=4OCvPrDhGuQ)

ISCC - Similarity hashing for digital content identification in decentralized environments. [Recording](https://www.youtube.com/watch?v=4OCvPrDhGuQ) of the 30-minute talk.

## Organizations and Initiatives

### [ISCC Foundation](https://iscc.foundation/)

The **ISCC Foundation** is an independent international **nonprofit organization** that promotes information technologies for the common good.

In particular, the foundation supports the **ISCC** and promotes the development and adoption of open standards and open source technologies as well as tools and services that enable individuals and organizations to better **create, manage, discover, access, share, and monetize digital content, knowledge, and ideas**.

### [ISO - International Organization for Standardization](https://www.iso.org/committee/48836.html)

**ISO/TC 46/SC 9** (Identification and description) standardized the **International Standard Content Code** as [ISO 24138:2024](https://www.iso.org/standard/77899.html).
