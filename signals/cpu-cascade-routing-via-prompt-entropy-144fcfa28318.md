# CPU Cascade Routing via Prompt Entropy

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-cascade-routing-via-prompt-entropy-144fcfa28318`
Run ID: `cpu-cascade-routing-via-prompt-entropy-144fcfa28318-20260529T032909300402+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/78abe1b60d0e

## What looked useful

Entropy routing beat matched length and random baselines in the bounded proxy: entropy cascade mean accuracy 0.9996 at 0.5569 fallback fraction versus length-matched 0.7090 and random-matched 0.7768; entropy AUC for cheap-fail/strong-correct cases was 0.9472 versus length AUC 0.5033.

## Boundaries and scale limits

Synthetic prompts, synthetic cheap/strong model gap, route fraction used as cost proxy, and no real LLM traces or measured CPU inference latency. Strong fallback was trained on the hard/paraphrase distribution, so the result does not validate general prompt difficulty or production cascade routing.

## Claim scope

On a controlled synthetic CPU intent-classification cascade, prompt Shannon entropy identifies lexically diverse prompts where a cheap word-unigram classifier fails and a stronger word-plus-character-ngram fallback succeeds; entropy threshold routing recovered 99.96% mean accuracy while routing 55.69% of prompts to the fallback across 20 seeds.

## Why it stopped

No-paper useful signal only: the run supports the mechanism in a synthetic proxy but does not provide direct real-serving evidence or publication-grade validation.

## Recommended next action

Run a bounded direct follow-up on real prompt traces with paired cheap CPU model and stronger fallback outputs, measuring actual latency and comparing entropy against confidence, length, and learned-router baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace Entropy Routing Against Confidence and Length Baselines
- Success threshold: Entropy or entropy-plus-confidence routing achieves at least 95% of all-strong accuracy with at least 25% lower measured CPU cost or latency, and beats length-only and confidence-only routers at matched cost.
- Stop condition: Stop if entropy AUC for cheap-fail/strong-correct cases is below 0.60 or if entropy routing fails to beat length/confidence baselines at matched cost on two independent prompt domains.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-cascade-routing-via-prompt-entropy-144fcfa28318`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
