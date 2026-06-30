# Robustness benchmark for cached prompt-suffix n-gram decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `robustness-benchmark-for-cached-prompt-suffix-n-gram-decod-8cfdaccf45`
Run ID: `robustness-benchmark-for-cached-prompt-suffix-n-gram-decod-8cfdaccf45-20260604T110114719260+0000`

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

- Parent run decision: Prompt-Suffix N-gram Speculative Decoding for GPT-2: enoch://control-plane/projects/prompt-suffix-n-gram-speculative-decoding-for-gpt-2-7f97ea8c0ed7/runs/prompt-suffix-n-gram-speculative-decoding-for-gpt-2-7f97ea8c0ed7-20260604T071314765174+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ede08e12091f

## What looked useful

Primary min_ngram=2/max_ngram=8 run: overall proposal coverage 0.828, hit rate given proposal 0.912, accepted-token fraction 0.755. Perturbed aggregate passed the explicit Tier 1 threshold with coverage 0.656 and hit rate 0.873, but the prefix_noise_same_suffix case had coverage 0.062 and accepted-token fraction 0.031. A min_ngram=1 ablation forced perturbed coverage to 1.000 but reduced perturbed hit rate to 0.604 and left the brittle case at 0.031 hit rate.

## Boundaries and scale limits

Single small causal LM, 192 primary greedy oracle steps, controlled hand-written prompts, no full batched speculative verification, no end-to-end latency measurement, no larger instruction-tuned models, and no broad natural corpus.

## Claim scope

On a six-case controlled Tier 1 distilgpt2 greedy-decoding benchmark, cached prompt-suffix n-gram proposals aligned strongly with repeated-copy prompts and two of three perturbed-cache prompts, but failed badly on one prefix-noise perturbation that drove a repeated-token continuation absent from the prompt suffix cache.

## Why it stopped

Tier 1 direct evidence supports the mechanism in repeated-copy settings but shows mixed robustness and a clear brittle perturbation case, so it is not paper-positive.

## Recommended next action

Stop this run as no-paper useful signal; next, run a bounded deepen test with real batched prompt-lookup/speculative verification and require both aggregate and per-condition robustness thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Batched prompt-lookup decoding robustness with per-condition failure thresholds
- Success threshold: Across at least 3 model families or sizes, perturbed prompts must achieve accepted-token fraction >= 0.40 aggregate, hit rate given proposal >= 0.60, and no named perturbation family below 0.20 accepted-token fraction while showing positive end-to-end latency benefit versus greedy decoding.
- Stop condition: Stop as negative if any model family has perturbed accepted-token fraction below 0.20 or if batched verification removes the latency benefit despite high proposal agreement.

## Evidence references

- Artifact root: `<local-path>/projects/robustness-benchmark-for-cached-prompt-suffix-n-gram-decod-8cfdaccf45`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
