# Evidence Anchor Ledger for Agent Reasoning Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-anchor-ledger-for-agent-reasoning-reliability-6d25674bc8a1`
Run ID: `evidence-anchor-ledger-for-agent-reasoning-reliability-6d25674bc8a1-20260530T021021701293+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8f28ee149113

## What looked useful

A reproducible local benchmark supports the mechanism that source-anchor verification can prevent reasoning-state corruption from unanchored or forged intermediate observations, but the evidence is not broad or direct enough for a paper.

## Boundaries and scale limits

Proxy-only synthetic evidence; no real LLM agent, natural-language extraction, retrieval miss, ambiguous source, corrupted source corpus, or deployed latency/cost evaluation was tested.

## Claim scope

In a synthetic multi-hop chain benchmark with complete immutable source facts, an evidence-anchor ledger that rejects unanchored and source-mismatched observations preserved 100% answer accuracy across tested noise rates while a last-write-wins working-memory baseline degraded from 68.16% accuracy at 0.10 noise to 4.31% at 0.75 noise.

## Why it stopped

Stopped after a successful synthetic proxy mechanism probe; this is useful no-paper evidence, not full validation of real agent reasoning reliability.

## Recommended next action

Run a bounded direct-evidence follow-up with a real tool-using LLM agent on document-grounded QA, comparing no-ledger versus ledger conditions on answer accuracy, unsupported-claim rate, and latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real LLM Evidence Ledger Ablation on Document-Grounded QA
- Success threshold: Unsupported-claim rate decreases by at least 30% relative while answer accuracy drops by no more than 5 percentage points and citation validity improves versus baseline.
- Stop condition: Stop if ledger overhead exceeds 2x latency/cost or if unsupported-claim reduction is below 10% relative on the labeled QA set.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-anchor-ledger-for-agent-reasoning-reliability-6d25674bc8a1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
