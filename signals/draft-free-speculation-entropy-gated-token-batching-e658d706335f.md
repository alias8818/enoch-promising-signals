# Draft-Free Speculation: Entropy-Gated Token Batching

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `draft-free-speculation-entropy-gated-token-batching-e658d706335f`
Run ID: `draft-free-speculation-entropy-gated-token-batching-e658d706335f-20260530T033333444057+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e8ab10a9b95e

## What looked useful

Lower entropy was consistently associated with higher n-gram proposal acceptance (medium K=4 entropy/acceptance correlation -0.204), but strict entropy gates attempted too few positions and the best gates converged to about 90% coverage while still slightly underperforming ungated proposal attempts.

## Boundaries and scale limits

Single small GPT-2-family model, one dataset, greedy argmax acceptance, offline window scoring, and tokens-per-pass accounting rather than live KV-cache serving latency. The result does not rule out stronger draft-free proposers or controllers that include latency/cost features beyond entropy.

## Claim scope

On distilgpt2 with WikiText-2 validation windows and a corpus n-gram proposer, verifier entropy predicts proposal acceptance, but entropy-gated proposal attempts do not beat always attempting the same cheap proposal under verifier-pass accounting for proposal lengths 2, 4, and 8.

## Why it stopped

Bounded proxy evidence is mixed: entropy is predictive, but entropy gating did not improve tokens per verifier pass over the ungated cheap-proposal baseline, so this is not publication-grade support for the hypothesis.

## Recommended next action

Stop this as no-paper useful signal; the next bounded test is a live KV-cache latency benchmark comparing greedy, ungated n-gram verification, and entropy-gated n-gram verification.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache latency test for entropy-gated draft-free n-gram verification
- Success threshold: At least 5% held-out wall-clock tokens/sec improvement over both greedy one-token decoding and ungated n-gram verification, with no change in greedy-decoded output semantics.
- Stop condition: Stop if entropy-gated latency fails to beat either baseline on two proposal lengths for the same model/dataset.

## Evidence references

- Artifact root: `<local-path>/projects/draft-free-speculation-entropy-gated-token-batching-e658d706335f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
