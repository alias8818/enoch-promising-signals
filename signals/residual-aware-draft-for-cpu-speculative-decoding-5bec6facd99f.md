# Residual-Aware Draft for CPU Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `residual-aware-draft-for-cpu-speculative-decoding-5bec6facd99f`
Run ID: `residual-aware-draft-for-cpu-speculative-decoding-5bec6facd99f-20260525T115550958373+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a884e882bba0

## What looked useful

Residual state is a useful conditioning signal for draft distributions in this proxy: best residual acceptance was 0.7893 versus 0.1636 for the best target-call bigram row, and tokens per target verification call improved from 2.3084 to 7.3085. The unoptimized unigram draft remained fastest in one wall-clock control, so the result is mechanism support rather than a latency claim.

## Boundaries and scale limits

Synthetic target only; no pretrained transformer, no deployable trained draft network, and no optimized CPU serving stack. Wall-clock latency evidence is from a Python/NumPy harness and should not be treated as production CPU decoding validation.

## Claim scope

In a controlled synthetic recurrent-softmax target, a residual-conditioned low-rank draft produced lower KL to the target, higher speculative acceptance, and 3.17x more generated tokens per target verification call than a token-only bigram draft.

## Why it stopped

No-paper useful signal: the result supports the residual-aware mechanism on a synthetic proxy but does not provide direct transformer serving evidence.

## Recommended next action

Run a bounded real-transformer follow-up: fit a residual-aware draft head on hidden states from a small CPU-runnable transformer and compare exact speculative decoding latency and acceptance against unigram, bigram, and a token-only learned draft.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-Aware Draft Head on a Small Real Transformer
- Success threshold: Residual-aware draft improves generated tokens per target verification call by at least 25% over the best token-only baseline and improves or matches end-to-end CPU tokens/s within 5% across at least two block sizes.
- Stop condition: Stop as negative if residual-aware draft overhead prevents wall-clock parity or if acceptance/target-call efficiency fails to exceed the best token-only baseline by 10%.

## Evidence references

- Artifact root: `<local-path>/projects/residual-aware-draft-for-cpu-speculative-decoding-5bec6facd99f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
