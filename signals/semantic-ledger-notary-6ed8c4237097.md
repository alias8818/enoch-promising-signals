# Semantic Ledger Notary

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `semantic-ledger-notary-6ed8c4237097`
Run ID: `semantic-ledger-notary-6ed8c4237097-20260521T223326136473+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2eeb37ddb77e

## What looked useful

Raw and canonical hashes rejected all benign paraphrases; token Jaccard accepted all tampered edits; the final semantic fingerprint accepted 10/10 benign paraphrases and rejected 10/10 meaning-changing edits, with chain mismatch at the edited index.

## Boundaries and scale limits

Synthetic handcrafted cases only; no real ledger corpus, adversarial paraphrase benchmark, neural semantic model, production append-only storage, key management, public timestamping, or distributed consensus was tested.

## Claim scope

In a deterministic 20-pair synthetic English ledger task, a direction-sensitive semantic fingerprint separated benign paraphrases from meaning-changing ledger edits better than raw hashes, canonical hashes, and token-similarity baselines, while hash-chain mismatch behavior remained intact.

## Why it stopped

The mechanism is supported only by a small synthetic/proxy probe, not by direct real-world or adversarial evidence sufficient for publication.

## Recommended next action

Stop this run as no-paper useful synthetic evidence; next run should evaluate the same notary interface on a held-out realistic ledger mutation corpus with adversarial party-role and accounting-direction cases.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out realistic ledger mutation benchmark for semantic notary fingerprints
- Success threshold: Semantic notary reaches >=0.95 benign accept rate and >=0.95 tamper reject rate on held-out realistic mutations, with no party-role swap false accepts and no chain persistence failures.
- Stop condition: Stop if semantic notary tamper reject rate is below 0.90, benign accept rate is below 0.90, or any party-role swap is falsely accepted after one extractor repair pass.

## Evidence references

- Artifact root: `<local-path>/projects/semantic-ledger-notary-6ed8c4237097`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
