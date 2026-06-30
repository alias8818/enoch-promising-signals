# Quantized small-model agent with evidence ledger integrity

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-small-model-agent-with-evidence-ledger-integrity-b4dad4e5d3bb`
Run ID: `quantized-small-model-agent-with-evidence-ledger-integrity-b4dad4e5d3bb-20260609T091602035867+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a08a821698a2

## What looked useful

The benchmark supports separating quantized policy behavior from ledger integrity: int8 storage preserved toy ranking behavior and hash/quote verification caught direct tampering, but a semantic mismatch control passed integrity while failing entailment, showing ledger integrity is not claim truth.

## Boundaries and scale limits

Toy synthetic corpus only; no real language model generation, real retrieval corpus, open-domain adversarial claims, signatures, append-only persistence, concurrent ledger writes, or optimized int8 kernel throughput were tested.

## Claim scope

In a deterministic synthetic claim-evidence benchmark with a small neural ranker, portable weight-only int8 storage reduced model state size by 72.8% without changing held-out ranking/abstention outcomes, and exact quote plus SHA-256 ledger checks detected explicit quote/hash/evidence-id tampering.

## Why it stopped

Proxy synthetic evidence is useful but insufficient for a publication-grade claim; it also exposes that cryptographic evidence-ledger integrity does not guarantee semantic support.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use a real small quantized LLM or retrieval agent with semantic verifier controls before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-model agent ledger integrity with semantic verifier controls
- Success threshold: Quantized model changes task accuracy by no more than 2 percentage points versus dense baseline, ledger tamper detection is 100%, and semantic mismatch acceptance is below 1% on at least 500 real-corpus claim cases.
- Stop condition: Stop if quantization causes more than a 5 percentage point accuracy drop, if ledger tamper detection is below 100%, or if semantic mismatch acceptance remains above 5% after adding the verifier.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-small-model-agent-with-evidence-ledger-integrity-b4dad4e5d3bb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
