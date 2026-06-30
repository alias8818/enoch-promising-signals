# N-gram speculative draft for safer agent answers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-draft-for-safer-agent-answers-460381516031`
Run ID: `n-gram-speculative-draft-for-safer-agent-answers-460381516031-20260528T211653130122+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/57ea2dc6f7d8

## What looked useful

The mechanism appears useful as a cheap local safety prior: it reduced harmful-marker leakage from roughly 45% for an unsteered mixed n-gram generator to 0% in the proxy, while improving benign safe-success from 10% for static refusal to about 51% across five seeds.

## Boundaries and scale limits

No real instruction-tuned target model, no public safety benchmark, no human labels, no semantic harmfulness evaluator, no real speculative-decoding acceptance path, and no production latency measurement.

## Claim scope

In a synthetic 3-gram agent-answer benchmark, a safety-trained n-gram candidate draft/reranker eliminated operational marker leakage and improved benign safe-success over a static refusal baseline, but only under toy corpora and regex metrics.

## Why it stopped

No-paper closure: this run produced a reproducible synthetic/proxy useful signal, not direct validation of safer real agent answers.

## Recommended next action

Run a bounded direct-evidence follow-up using a small instruction-tuned model plus a public harmful/benign benchmark, comparing n-gram safety drafting against classifier-gated refusal and normal decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: N-gram safety draft on a small instruction-tuned model and public safety benchmark
- Success threshold: At least 30% relative reduction in unsafe completions versus normal decoding, benign false refusal no worse than classifier-gated refusal by more than 5 absolute percentage points, and less than 25% median latency overhead on the small-model benchmark.
- Stop condition: Stop if unsafe completion reduction is below 10% relative, benign false refusals exceed the classifier-gated baseline by more than 10 absolute percentage points, or latency overhead exceeds 50% without a safety gain.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-safer-agent-answers-460381516031`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
