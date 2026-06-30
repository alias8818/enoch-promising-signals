# Tiny Learned Drafter for Speculative Decoding on a 125M Target

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `tiny-learned-drafter-for-speculative-decoding-on-a-125m-target-7477900f132d`
Run ID: `tiny-learned-drafter-for-speculative-decoding-on-a-125m-target-7477900f132d-20260620T223512226528+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/737af98364f9

## What looked useful

The constrained 6.5M-parameter learned drafter beat unigram and copy-previous controls but did not beat the bigram control; mean accepted was 0.104 tokens at k=4, full-k accept was 0%, and estimated speed was 0.865x serial target.

## Boundaries and scale limits

Only 384 train sequences and 96 eval sequences, sequence length 64, k=4 greedy acceptance, no optimized KV-cache serving, no sampling acceptance, no long-context or multi-domain validation.

## Claim scope

Bounded local GPT-2 124M-class greedy speculative verification on WikiText-2 prefixes with a one-layer GRU drafter trained on target argmax labels.

## Why it stopped

Bounded local evidence does not support the tiny learned drafter hypothesis: the constrained learned drafter remained below a bigram control and the estimated throughput was slower than serial target decoding.

## Recommended next action

Stop this run as no-paper useful negative signal; a bounded deepen follow-up should only proceed if it changes the objective to top-k/KL target distillation on at least 10k prefixes and requires mean accepted prefix length >=1.0 at k=4 plus measured speedup above serial target.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Top-k distillation for a tiny GPT-2 speculative drafter
- Success threshold: Mean accepted prefix length >=1.0 at k=4, full-k accept rate >=10%, and measured speculative tokens/second at least 1.15x serial GPT-2 target on held-out prefixes.
- Stop condition: Stop as negative if held-out mean accepted prefix length remains below 0.5 after 10k prefixes or measured speculative throughput is still below serial target.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-learned-drafter-for-speculative-decoding-on-a-125m-target-7477900f132d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
