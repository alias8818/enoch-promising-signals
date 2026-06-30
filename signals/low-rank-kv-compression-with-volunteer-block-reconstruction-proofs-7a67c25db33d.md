# Low-Rank KV Compression with Volunteer Block Reconstruction Proofs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `low-rank-kv-compression-with-volunteer-block-reconstruction-proofs-7a67c25db33d`
Run ID: `low-rank-kv-compression-with-volunteer-block-reconstruction-proofs-7a67c25db33d-20260521T234038884465+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f075905c6213

## What looked useful

Volunteer factor-reconstruction proofs worked in the tested algebraic corruption setting with 0/1536 false accepts, but naive fixed-rank low-rank KV compression caused large GPT-2 next-token distribution drift at ranks that actually compressed storage.

## Boundaries and scale limits

One GPT-2 prompt/cache and short synthetic probes; no prompt suite, perplexity run, serving latency measurement, larger-model validation, adversarial volunteer strategy search, or production transfer accounting.

## Claim scope

Bounded local probe of naive per-block SVD low-rank compression on synthetic KV-shaped tensors and one GPT-2 next-token cache, plus random-projection checks for volunteer reconstruction algebra.

## Why it stopped

Proxy and direct local evidence early-falsify the practical compression claim at useful compression ratios; proof feasibility alone does not make the full KV compression system viable.

## Recommended next action

Stop this naive fixed-rank SVD path as no-paper; a bounded next test should use adaptive error-budgeted ranks across a small GPT-2 prompt suite before considering larger scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive error-budgeted KV block ranks with direct GPT-2 logit thresholds
- Success threshold: Median KL <= 0.05, p95 total variation <= 0.15, top-token agreement >= 95%, and realized KV storage compression >= 1.5x across the prompt suite.
- Stop condition: Stop if adaptive ranks need less than 1.25x realized compression or if p95 total variation remains above 0.25 after meeting the sketch error budget.

## Evidence references

- Artifact root: `<local-path>/projects/low-rank-kv-compression-with-volunteer-block-reconstruction-proofs-7a67c25db33d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
