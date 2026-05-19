# Cross-Instance Evidence Verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cross-instance-evidence-verification-7c114bf77ca0`
Run ID: `cross-instance-evidence-verification-7c114bf77ca0-20260517T194909648294+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2e8dc4035b73

## What looked useful

A 2-of-3 cross-instance quorum reduced false positives from 47 to 30 while preserving 479/480 supported claims. Unanimity reduced false positives to 23 but rejected 46 supported claims, making quorum the better local tradeoff.

## Boundaries and scale limits

The result used synthetic documents and deterministic lexical verifiers only: 8 seeds, 80 entities per seed, 60 sampled facts per seed, 1,920 policy-level claims, and 5,760 instance-level decisions. It did not test real LLM instances, natural corpora, paraphrased evidence, or external citation behavior.

## Claim scope

On a deterministic synthetic registry benchmark, requiring a 2-of-3 quorum across independent retrieval/chunking/tokenization verifier instances reduced false acceptance of unsupported, contradicted, and adversarially misattributed evidence claims versus accepting any single verifier.

## Why it stopped

Synthetic proxy produced a useful mechanism signal but not direct publication-grade evidence for real cross-instance LLM evidence verification.

## Recommended next action

Run a bounded real-corpus follow-up with actual LLM verifier instances and labeled claim/evidence pairs; do not write a paper from this synthetic proxy alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Corpus Cross-Instance Evidence Verification
- Success threshold: 2-of-3 quorum reduces false acceptance by >=25% versus single-instance acceptance while supported-claim recall remains >=95% on the real-corpus benchmark.
- Stop condition: Stop if quorum reduces false acceptance by <10%, recall falls below 90%, or gains are explained entirely by duplicate retrieval failures rather than independent verification.

## Evidence references

- Artifact root: `<local-path>/projects/cross-instance-evidence-verification-7c114bf77ca0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
