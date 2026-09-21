---
title: ISCC - Resources
description: The open-source software and live demos that make up the ISCC ecosystem.
authors: Titusz Pan
icon: lucide/library
---

# ISCC - Resources

The open-source software and live demos that make up the ISCC ecosystem. Everything below builds
on [ISO 24138:2024](https://www.iso.org/standard/77899.html), the International Standard Content
Code.

Looking for independent assessments, research, or press coverage? Those are
collected on [iscc.io/standard/adoption](https://iscc.io/standard/adoption). The ISCC Foundation's
own papers and talks are listed at
[iscc.io/foundation/publications](https://iscc.io/foundation/publications).

<svg aria-hidden="true" style="position: absolute; width: 0; height: 0; overflow: hidden;"><symbol id="gh-mark" viewBox="0 0 16 16"><path fill="currentColor" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></symbol></svg>

## Open-source ecosystem

Every repository below is developed in the open under the **Apache-2.0** license.

### Core components

<div class="iscc-repos">
<a class="iscc-repo" href="https://github.com/iscc/iscc-core">
<span class="iscc-repo__name">iscc-core</span><span class="iscc-badge iscc-badge--stable">Stable</span>
<span class="iscc-repo__desc">Authoritative ISO 24138:2024 reference implementation. The low-level codec and fingerprinting algorithms that every ISCC build rests on.</span>
<span class="iscc-repo__cta"><svg class="iscc-repo__icon" viewBox="0 0 16 16" aria-hidden="true"><use href="#gh-mark"></use></svg>View on GitHub &rarr;</span>
</a>
<a class="iscc-repo" href="https://github.com/iscc/iscc-sdk">
<span class="iscc-repo__name">iscc-sdk</span><span class="iscc-badge iscc-badge--stable">Stable</span>
<span class="iscc-repo__desc">High-level Python toolkit adding media-type detection, metadata extraction, and content processing. The primary integration entry point.</span>
<span class="iscc-repo__cta"><svg class="iscc-repo__icon" viewBox="0 0 16 16" aria-hidden="true"><use href="#gh-mark"></use></svg>View on GitHub &rarr;</span>
</a>
<a class="iscc-repo" href="https://github.com/iscc/iscc-schema">
<span class="iscc-repo__name">iscc-schema</span><span class="iscc-badge iscc-badge--stable">Stable</span>
<span class="iscc-repo__desc">JSON Schema, JSON-LD contexts, and Pydantic models for ISCC metadata interoperability.</span>
<span class="iscc-repo__cta"><svg class="iscc-repo__icon" viewBox="0 0 16 16" aria-hidden="true"><use href="#gh-mark"></use></svg>View on GitHub &rarr;</span>
</a>
<a class="iscc-repo" href="https://github.com/iscc/iscc-lib">
<span class="iscc-repo__name">iscc-lib</span><span class="iscc-badge iscc-badge--beta">Beta</span>
<span class="iscc-repo__desc">High-performance polyglot implementation of the ISO 24138:2024 core algorithms. A Rust core with bindings for Python, Java, Go, Node.js, WASM, and more, conformance-tested against iscc-core.</span>
<span class="iscc-repo__cta"><svg class="iscc-repo__icon" viewBox="0 0 16 16" aria-hidden="true"><use href="#gh-mark"></use></svg>View on GitHub &rarr;</span>
</a>
<a class="iscc-repo" href="https://github.com/iscc/iscc-crypto">
<span class="iscc-repo__name">iscc-crypto</span><span class="iscc-badge iscc-badge--beta">Beta</span>
<span class="iscc-repo__desc">Ed25519 signing, W3C Verifiable Credentials, and cryptographic verification for signed ISCC declarations.</span>
<span class="iscc-repo__cta"><svg class="iscc-repo__icon" viewBox="0 0 16 16" aria-hidden="true"><use href="#gh-mark"></use></svg>View on GitHub &rarr;</span>
</a>
<a class="iscc-repo" href="https://github.com/bio-codes/iscc-sum">
<span class="iscc-repo__name">iscc-sum</span><span class="iscc-badge iscc-badge--beta">Beta</span>
<span class="iscc-repo__desc">Fast single-pass CLI for Data-Code and Instance-Code generation in Rust with Python bindings, from the BioCodes project.</span>
<span class="iscc-repo__cta"><svg class="iscc-repo__icon" viewBox="0 0 16 16" aria-hidden="true"><use href="#gh-mark"></use></svg>View on GitHub &rarr;</span>
</a>
</div>

### Discovery infrastructure

<div class="iscc-repos">
<a class="iscc-repo" href="https://github.com/iscc/iscc-web">
<span class="iscc-repo__name">iscc-web</span><span class="iscc-badge iscc-badge--stable">Stable</span>
<span class="iscc-repo__desc">REST API service for ISCC generation. Powers the public web demo at web.iscc.io.</span>
<span class="iscc-repo__cta"><svg class="iscc-repo__icon" viewBox="0 0 16 16" aria-hidden="true"><use href="#gh-mark"></use></svg>View on GitHub &rarr;</span>
</a>
<a class="iscc-repo" href="https://github.com/iscc/iscc-hub">
<span class="iscc-repo__name">iscc-hub</span><span class="iscc-badge iscc-badge--beta">Beta</span>
<span class="iscc-repo__desc">Reference timestamping and declaration service. Issues ISCC-IDs with cryptographic receipts for public content declaration and discovery.</span>
<span class="iscc-repo__cta"><svg class="iscc-repo__icon" viewBox="0 0 16 16" aria-hidden="true"><use href="#gh-mark"></use></svg>View on GitHub &rarr;</span>
</a>
<a class="iscc-repo" href="https://github.com/iscc/iscc-search">
<span class="iscc-repo__name">iscc-search</span><span class="iscc-badge iscc-badge--beta">Beta</span>
<span class="iscc-repo__desc">Specialized multi-index similarity search with sub-millisecond retrieval for ISCC codes and SIMPRINTs.</span>
<span class="iscc-repo__cta"><svg class="iscc-repo__icon" viewBox="0 0 16 16" aria-hidden="true"><use href="#gh-mark"></use></svg>View on GitHub &rarr;</span>
</a>
</div>

### ISCC Semantic Codes

<div class="iscc-repos">
<a class="iscc-repo" href="https://github.com/iscc/iscc-sct">
<span class="iscc-repo__name">iscc-sct</span><span class="iscc-badge iscc-badge--beta">Beta</span>
<span class="iscc-repo__desc">Semantic Text-Codes built on deep learning. Generates SIMPRINTs for granular text matching across languages. A core pilot component.</span>
<span class="iscc-repo__cta"><svg class="iscc-repo__icon" viewBox="0 0 16 16" aria-hidden="true"><use href="#gh-mark"></use></svg>View on GitHub &rarr;</span>
</a>
<a class="iscc-repo" href="https://github.com/iscc/iscc-sci">
<span class="iscc-repo__name">iscc-sci</span><span class="iscc-badge iscc-badge--beta">Beta</span>
<span class="iscc-repo__desc">Semantic Image-Codes for visual content fingerprinting and similarity detection.</span>
<span class="iscc-repo__cta"><svg class="iscc-repo__icon" viewBox="0 0 16 16" aria-hidden="true"><use href="#gh-mark"></use></svg>View on GitHub &rarr;</span>
</a>
</div>

### Specifications & quality assurance

<div class="iscc-repos">
<a class="iscc-repo" href="https://github.com/iscc/iscc-ieps">
<span class="iscc-repo__name">iscc-ieps</span><span class="iscc-badge iscc-badge--draft">Draft</span>
<span class="iscc-repo__desc">ISCC Enhancement Proposals documenting new features and algorithms that inform future ISO standardization.</span>
<span class="iscc-repo__cta"><svg class="iscc-repo__icon" viewBox="0 0 16 16" aria-hidden="true"><use href="#gh-mark"></use></svg>View on GitHub &rarr;</span>
</a>
<a class="iscc-repo" href="https://github.com/iscc/twinspect">
<span class="iscc-repo__name">twinspect</span><span class="iscc-badge iscc-badge--stable">Stable</span>
<span class="iscc-repo__desc">Benchmarking framework for near-duplicate matching and similarity search across text, audio, image, and video content.</span>
<span class="iscc-repo__cta"><svg class="iscc-repo__icon" viewBox="0 0 16 16" aria-hidden="true"><use href="#gh-mark"></use></svg>View on GitHub &rarr;</span>
</a>
</div>

<div class="iscc-legend">
<span class="iscc-legend__item"><span class="iscc-badge iscc-badge--stable">Stable</span> Production-ready, stable API, ISO-aligned where applicable</span>
<span class="iscc-legend__item"><span class="iscc-badge iscc-badge--beta">Beta</span> Feature-complete, API may change before v1.0, suitable for pilots</span>
<span class="iscc-legend__item iscc-legend__item--break"><span class="iscc-badge iscc-badge--draft">Draft</span> Proposal documents under discussion</span>
</div>

## Try it live

### [Cover Matching Demo](https://covers.iscc.io/)

Three million book covers from the Amazon Reviews'23 dataset, indexed and searchable through ISCC
similarity matching.

### [ISCC Web Demo](https://web.iscc.io/)

Minimal web application for generating ISCCs directly in the browser. Live instance of
[iscc-web](https://github.com/iscc/iscc-web).

### [ISCC Playground](https://huggingface.co/spaces/iscc/iscc-playground)

Interactive Hugging Face Space for exploring every ISCC-UNIT and inspecting how codes change as
content changes.

### [BioCodes Imagewalk Demo](https://bio-codes.io/viz/imagewalk/)

Interactive visualization of the proposed **Imagewalk** algorithm for robust bio-image traversal and ISCC-CODE generation.

## Publications & talks

Third-party publications, assessments, and coverage of the ISCC are collected on
[iscc.io/standard/adoption](https://iscc.io/standard/adoption). The
[ISCC Foundation](https://iscc.io/foundation), which maintains the standard, lists its own
[papers and talks](https://iscc.io/foundation/publications) and its
[press kit](https://iscc.io/foundation/press) on iscc.io.
