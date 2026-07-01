# Tiny Proxy Model Data Selection vs Random for GPT-2-Small Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-proxy-model-data-selection-vs-random-for-gpt-2-small-pretraining-76f016c2f8f8`
Run ID: `tiny-proxy-model-data-selection-vs-random-for-gpt-2-small-pretraining-76f016c2f8f8-20260629T201205308363+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a0f49f1e2746

## What looked useful

Tiny-proxy loss buckets can encode useful difficulty information, but naive extremes are risky. Mid-loss selection improved validation NLL by -0.0051 vs random across 4 seeds; high-loss selection worsened NLL by +0.0689 vs random across all seeds.

## Boundaries and scale limits

Not GPT-2-small pretraining: no 124M-parameter target, no WebText/OpenWebText-scale corpus, no long schedule, no downstream evaluation, and only 512 selected training blocks with 160 target steps per run.

## Claim scope

Bounded WikiText-2 short-pretraining probe with a 0.94M-parameter proxy model and 4.24M-parameter GPT-style target: proxy mid-loss block selection slightly beat random across 4 calibrated seeds, high-loss selection was consistently harmful, and low-loss selection was mixed.

## Why it stopped

No-paper closure: this was a bounded proxy/mechanism probe, not direct GPT-2-small evidence. It produced useful guidance but is too small and short for a publication-grade claim.

## Recommended next action

Run a medium confirmation focused only on proxy mid-loss selection versus random with a larger GPT-style target, a longer fixed sequence-item budget, a frozen protocol, and at least 3 seeds; stop if the mean validation NLL gain is below 0.01 or not positive in most seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium confirmation of tiny-proxy mid-loss selection for causal LM pretraining
- Success threshold: Mean validation NLL at least 0.01 lower than random and positive paired improvement in at least 3 of 4 seeds, with high-loss selection worse than random as a mechanism sanity check.
- Stop condition: Stop as negative/no-paper if mid-loss does not beat random by at least 0.01 mean NLL, if the effect flips sign in multiple seeds, or if runtime exceeds the local GB10 budget without checkpointed useful signal.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-proxy-model-data-selection-vs-random-for-gpt-2-small-pretraining-76f016c2f8f8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
