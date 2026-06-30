# CPU n-gram speculative decoding for small LM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-decoding-for-small-lm-8dcbb28156c4`
Run ID: `cpu-n-gram-speculative-decoding-for-small-lm-8dcbb28156c4-20260621T040022211838+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b5f990dbbbaa

## What looked useful

Order-4 n-gram drafting reduced verifier calls by 0.831 on code templates, 0.783 on boilerplate, 0.844 on repeated natural text, and 0.000 on random tokens; order sweep 2-6 preserved the domain-dependent pattern.

## Boundaries and scale limits

No neural target LM, no real tokenizer/KV-cache loop, no wall-clock decoding throughput, synthetic/local generated corpora only, and max draft length limited to 6 tokens.

## Claim scope

Bounded proxy evidence that a CPU n-gram drafter can reduce verifier-call counts on surface-repetitive held-out token streams, while providing no benefit on random/non-repeated controls.

## Why it stopped

Proxy-only mechanism evidence is useful but insufficient for paper-positive validation of CPU n-gram speculative decoding on small LMs.

## Recommended next action

Stop this worker run as no-paper useful signal; next bounded action is a real small-neural-LM CPU decoding experiment with output equivalence and wall-clock tokens/sec.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-LM CPU n-gram speculative decoding wall-clock test
- Success threshold: At least 1.3x wall-clock tokens/sec improvement on repetitive code/boilerplate prompts with exact greedy-output equivalence and no more than 5% slowdown on natural-language controls.
- Stop condition: Stop as negative if exact-output equivalence fails, if wall-clock speedup is below 1.1x on repetitive prompts, or if overhead causes more than 5% slowdown on two or more non-repetitive controls.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-decoding-for-small-lm-8dcbb28156c4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
