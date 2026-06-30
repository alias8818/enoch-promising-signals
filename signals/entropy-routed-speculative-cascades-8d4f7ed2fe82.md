# Entropy-Routed Speculative Cascades

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `entropy-routed-speculative-cascades-8d4f7ed2fe82`
Run ID: `entropy-routed-speculative-cascades-8d4f7ed2fe82-20260526T010801046842+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8aaed54ce305

## What looked useful

Entropy is a measurable acceptance signal, but entropy routing by simple quantile thresholds is insufficient by itself; fixed k=8 is best at draft cost ratios 0.05 and 0.10, and fixed k=4 is best at ratio 0.20.

## Boundaries and scale limits

Small model pair, greedy argmax acceptance, 24 built-in prompts, short generated continuations, proxy weighted-forward cost rather than optimized wall-clock latency, no multi-draft cascade, no sampling-mode verification, no large-model or serving trace validation.

## Claim scope

On a bounded greedy speculative decoding proxy using distilgpt2 as draft and gpt2 as target over 24 prompts, draft entropy significantly predicts first-token acceptance, but a simple quartile entropy-routed depth policy does not outperform tuned fixed-depth baselines on weighted-forward efficiency.

## Why it stopped

Proxy/early bounded evaluation found a real entropy-acceptance signal but did not validate the practical speedup claim over tuned fixed-depth speculation.

## Recommended next action

Run one bounded deepen test with an optimized held-out entropy router and real latency timing; stop treating simple entropy routing as a positive result until it beats the fixed-depth frontier.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out optimized entropy router for speculative depth selection
- Success threshold: Held-out entropy router improves effective tokens per weighted forward by at least 5% over the best fixed-depth baseline at draft cost ratio 0.10 and is not worse by more than 2% at ratio 0.20 on both model pairs.
- Stop condition: Stop if the optimized held-out router fails to beat the fixed-depth frontier on either model pair or if real latency contradicts weighted-forward gains.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-routed-speculative-cascades-8d4f7ed2fe82`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
