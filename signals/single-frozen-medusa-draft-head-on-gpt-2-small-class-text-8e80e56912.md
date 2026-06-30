# Single frozen Medusa draft head on GPT-2-small-class text

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `single-frozen-medusa-draft-head-on-gpt-2-small-class-text-8e80e56912`
Run ID: `single-frozen-medusa-draft-head-on-gpt-2-small-class-text-8e80e56912-20260610T132622395467+0000`

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

- Parent run decision: Medusa-Single-Head: Frozen-Base + One Tiny Draft Head: enoch://control-plane/projects/medusa-single-head-frozen-base-one-tiny-draft-head-a0518b0fa7f1/runs/medusa-single-head-frozen-base-one-tiny-draft-head-a0518b0fa7f1-20260610T084653404786+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5157dfaf44e2

## What looked useful

Three seeds produced mean Medusa top-1 t+2 accuracy 0.1357 versus shifted-base 0.0250 and unigram 0.0475; mean top-5 0.2726 versus 0.0980 and 0.1641; mean two-token greedy accept rate 0.0477 versus shifted-base 0.0024.

## Boundaries and scale limits

Small controlled validation only: GPT-2 small, WikiText-2, 2,048 train blocks, 512 validation blocks, one t+2 head, no full Medusa tree, no latency benchmark, no draft-model baseline, and no domain robustness testing.

## Claim scope

On WikiText-2 with frozen GPT-2 small, one trainable Medusa-style head predicting token t+2 from hidden state h_t learned a stable future-token signal across three seeds, beating shifted-base and unigram controls and yielding a nonzero two-token greedy acceptance signal.

## Why it stopped

Controlled small direct test supports the mechanism but is insufficient for publication because it measures head accuracy and proxy greedy acceptance rather than end-to-end decoding speedup, broader robustness, or stronger baselines.

## Recommended next action

Run a bounded deepen test implementing actual two-token speculative/Medusa decoding on GPT-2 small, measuring acceptance and wall-clock latency against greedy GPT-2 and a small draft-model baseline before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end two-token Medusa decoding latency on frozen GPT-2 small
- Success threshold: At least 5% wall-clock tokens/sec improvement over greedy GPT-2 on 100 or more held-out prompts without changing verified greedy outputs, and acceptance statistics that beat the small draft-model baseline or explain a clear compute/latency tradeoff.
- Stop condition: Stop if verified generation speed is not improved by at least 2% or if acceptance overhead makes the Medusa path slower than greedy GPT-2 in two independent runs.

## Evidence references

- Artifact root: `<local-path>/projects/single-frozen-medusa-draft-head-on-gpt-2-small-class-text-8e80e56912`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
