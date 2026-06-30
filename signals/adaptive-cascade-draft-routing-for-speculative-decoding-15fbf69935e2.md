# Adaptive Cascade Draft Routing for Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-cascade-draft-routing-for-speculative-decoding-15fbf69935e2`
Run ID: `adaptive-cascade-draft-routing-for-speculative-decoding-15fbf69935e2-20260529T153821525675+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1e8d7bf3cbbd

## What looked useful

Adaptive contextual UCB improved modeled tokens per cost over the best fixed route by 16.94% in a routeable mixture and 9.41% under noisy shifts, but it was 3.10% worse than the best fixed route in homogeneous chat and was consistently behind a simpler classifier-greedy router in heterogeneous regimes.

## Boundaries and scale limits

No real target or draft LLMs, no GPU latency, no KV-cache or batching effects, no tokenizer/prompt corpus, and no quality-invariance checks. Confirmation used 900,000 simulated blocks, 10 seeds per policy/regime, and a single-process CPU simulator.

## Claim scope

Bounded proxy simulation of speculative-decoding draft-route selection across three synthetic traffic regimes with domain-dependent acceptance probabilities and route costs.

## Why it stopped

Proxy evidence is mixed: routing helps when draft acceptance is heterogeneous, but the tested adaptive online router is not superior to a simpler supervised cue baseline and no direct LLM-serving evidence was produced.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should replay these routing policies on measured acceptance traces from a small real speculative-decoding stack.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-based adaptive draft routing on small real speculative decoding models
- Success threshold: At least 8% improvement over the best fixed real-model baseline and no worse than classifier-greedy within one standard error across at least three prompt domains.
- Stop condition: Stop if contextual routing is below the best fixed route or below classifier-greedy by more than 3% tokens per target-equivalent cost on two independent trace samples.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-cascade-draft-routing-for-speculative-decoding-15fbf69935e2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
