# Quantized n-gram residual draft in a small neural speculative decoding loop

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quantized-n-gram-residual-draft-in-a-small-neural-speculat-67c1ac0579`
Run ID: `quantized-n-gram-residual-draft-in-a-small-neural-speculat-67c1ac0579-20260608T030402328603+0000`

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

- Parent run decision: Tiny N-gram Draft with Quantized Residual Target: enoch://control-plane/projects/tiny-n-gram-draft-with-quantized-residual-target-5c6b899a9606/runs/tiny-n-gram-draft-with-quantized-residual-target-5c6b899a9606-20260607T221346061183+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/291a0c948d7c

## What looked useful

Across three seeds, int8 residual improved accepted draft tokens per target call by 0.438 mean over draft-only, with per-seed gains 0.413, 0.497, and 0.404. It retained 1.009 mean of float-residual acceptance while using 26.5% of the estimated float residual table storage. N-gram-only drafting was worse than neural draft-only, showing the residual combination was the useful mechanism.

## Boundaries and scale limits

Small character-level MLP target and draft only; not GPT-2-small-class, not subword tokenization, not production latency, and not a full LLM serving implementation.

## Claim scope

In a controlled Tiny Shakespeare character-level fixed-context neural speculative decoding loop, an int8 quantized 4-gram residual added to a smaller neural draft improved acceptance against a separately trained small neural target across three seeds.

## Why it stopped

No-paper useful signal: Tier 1 direct mechanism evidence is positive, but it is limited to a small character-level neural setting and is not publication-grade validation.

## Recommended next action

Run a bounded deepen test with a subword Transformer target/draft pair and the same draft-only, n-gram-only, float-residual, and int8-residual controls before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Subword Transformer validation of int8 n-gram residual speculative drafting
- Success threshold: Int8 residual improves accepted draft tokens per target call by at least 0.20 absolute over draft-only in every seed or prompt shard, retains at least 95% of float-residual acceptance, and keeps residual table storage at or below 40% of float residual storage.
- Stop condition: Stop if int8 residual fails to beat draft-only by 0.10 accepted tokens per target call on two independent shards, if quantization retains less than 90% of float-residual acceptance, or if table lookup overhead removes target-call savings in batched validation.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-n-gram-residual-draft-in-a-small-neural-speculat-67c1ac0579`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
