# Strided KV Retention with Local Window on Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `strided-kv-retention-with-local-window-on-long-context-c375ef1641f2`
Run ID: `strided-kv-retention-with-local-window-on-long-context-c375ef1641f2-20260529T210513536128+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/03809f7c3eca

## What looked useful

Fixed striding preserves smooth recency-biased mass and retrieves stride-aligned old targets, but arbitrary old-token retrieval collapses to the probability that the target KV was retained; skipped old tokens are unrecoverable.

## Boundaries and scale limits

No transformer training, real corpus perplexity, real long-context benchmark, or KV-cache kernel benchmark was run. Results are CPU-only synthetic probes with random unit keys and analytic recency weights.

## Claim scope

Bounded synthetic evidence for local-window plus fixed-stride old-KV retention on exact needle retrieval and recency-biased attention-mass proxies at 8k and 16k context lengths.

## Why it stopped

Early proxy falsification: synthetic full-attention control achieved 1.0 random old-target top-1, while sparse fixed-stride retrieval matched retained-target probability and fell as low as 0.016 at 8k stride 64/128 and 0.008 at 16k stride 64.

## Recommended next action

Stop this broad fixed-stride claim; a bounded follow-up should test learned or semantic anchor retention against fixed stride and local-only baselines on non-aligned synthetic retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned anchor retention versus fixed stride for non-aligned long-context retrieval
- Success threshold: At equal retained KV fraction, learned/semantic retention improves non-aligned old-target retrieval by at least 2x over fixed stride and stays within 10 percent relative of full attention on a small direct model-level metric.
- Stop condition: Stop if learned/semantic retention does not beat fixed stride by at least 25 percent relative on synthetic non-aligned retrieval in the first matched-budget probe.

## Evidence references

- Artifact root: `<local-path>/projects/strided-kv-retention-with-local-window-on-long-context-c375ef1641f2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
