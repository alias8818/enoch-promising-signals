# Small-transformer anchor-gated KV retention on synthetic long-context QA

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-transformer-anchor-gated-kv-retention-on-synthetic-l-8081cbedd2`
Run ID: `small-transformer-anchor-gated-kv-retention-on-synthetic-l-8081cbedd2-20260528T205613284419+0000`

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

- Parent run decision: Anchor-Gated KV Eviction: exact-anchor tokens decide KV retention vs compression: enoch://control-plane/projects/anchor-gated-kv-eviction-exact-anchor-tokens-decide-kv-retention-vs-compression-b580f2280ea3/runs/anchor-gated-kv-eviction-exact-anchor-tokens-decide-kv-retention-vs-compression-b580f2280ea3-20260528T170411368504+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f6f0cc80afa4

## What looked useful

Anchor-gated retention reached 0.1628 mean held-out accuracy versus 0.0164 for recency-only retention and 0.0156 random baseline, but the absolute gain of 0.1464 missed the 0.30 success threshold. This supports a bounded mechanism signal but not a paper-ready claim.

## Boundaries and scale limits

Three seeds, 2000 training steps, 96-token batches, sequence length 192, eight synthetic fact triples, oracle-coded retention masks, no learned gate, no natural-language QA, no production KV-cache implementation, no GPT-2-small-class or larger baseline.

## Claim scope

On a controlled synthetic long-context key-value QA task with oracle anchor markers and a fixed 24-token retained-fact budget, anchor-gated retention gives a reproducible small-transformer retrieval advantage over recency-only retention, but the advantage is below the predeclared Tier 1 success threshold.

## Why it stopped

No-paper closure: the direct Tier 1 synthetic test produced a reproducible mechanism signal but failed the stated success threshold, so this is not a publication-grade positive result.

## Recommended next action

Run a bounded deepen test with a learned anchor gate or a stronger small-transformer training budget and require at least 0.30 absolute accuracy over matched recency retention before any paper escalation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned anchor-gated retention on synthetic long-context KV QA
- Success threshold: Mean held-out accuracy for anchor-gated retention exceeds recency-only retention by at least 0.30 absolute accuracy and exceeds random baseline by at least 0.25 across at least three seeds.
- Stop condition: Stop as negative if the anchor-gated method remains below a 0.30 absolute gain over recency after the calibrated training budget or if diagnostics show leakage or non-anchor shortcuts.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-anchor-gated-kv-retention-on-synthetic-l-8081cbedd2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
