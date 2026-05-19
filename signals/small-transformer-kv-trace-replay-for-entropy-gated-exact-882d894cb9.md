# Small-transformer KV trace replay for entropy-gated exact retention

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `83`
Project ID: `small-transformer-kv-trace-replay-for-entropy-gated-exact-882d894cb9`
Run ID: `small-transformer-kv-trace-replay-for-entropy-gated-exact-882d894cb9-20260518T181204339418+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/add4f502ddf1

## What looked useful

Entropy-gated exact KV retention achieved 0.489 to 0.968 query accuracy across budgets 8 to 32, compared with recency at 0.008 to 0.025 and random at 0.028 to 0.415; full-cache query accuracy was 1.000.

## Boundaries and scale limits

Synthetic task only; one seed; tiny transformer; no natural-language traces, pretrained-model validation, optimized serving implementation, latency benchmark, or distractor robustness test.

## Claim scope

In a single-seed controlled synthetic delayed-recall task, a trained 2-layer causal transformer retained query-answer accuracy much better with entropy-gated exact KV retention than with recency, random, or low-entropy retention at matched KV budgets.

## Why it stopped

The controlled small direct test supports the mechanism, but the evidence is single-seed synthetic and not publication-grade; controller metadata did not request promising escalation.

## Recommended next action

Stop and archive this as no-paper mechanism evidence; a future independent project would need multi-seed and natural-text pretrained-model replay before any paper claim.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-kv-trace-replay-for-entropy-gated-exact-882d894cb9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
