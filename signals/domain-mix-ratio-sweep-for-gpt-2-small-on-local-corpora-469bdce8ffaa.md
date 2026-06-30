# Domain Mix Ratio Sweep for GPT-2-Small on Local Corpora

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `domain-mix-ratio-sweep-for-gpt-2-small-on-local-corpora-469bdce8ffaa`
Run ID: `domain-mix-ratio-sweep-for-gpt-2-small-on-local-corpora-469bdce8ffaa-20260619T074133923376+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b5b380ea115a

## What looked useful

Increasing target-domain sampling probability improves target held-out loss but damages off-domain retention. A balanced 50% target / 25% / 25% mix had the best mean macro loss (0.7134), while 100% target mix had the best code loss (0.4502) but poor off-domain losses (legal 3.9776, biomed 4.5051).

## Boundaries and scale limits

Synthetic corpora only; 240 train and 72 eval documents per domain; 40 update steps per ratio; three seeds; GPT-2-small only; no real local corpus, long training, larger model, or production distribution shift validation.

## Claim scope

On deterministic project-local synthetic code/legal/biomed mini-corpora, GPT-2-small fine-tuned for 40 steps per ratio shows a stable target-domain versus off-domain tradeoff across three seeds: 100% code mix minimizes code held-out loss, while 50% code mix minimizes three-domain macro held-out loss.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic, short-budget GPT-2-small proxy rather than real-corpus validation.

## Recommended next action

Run the same ratio sweep on real project-local corpora with at least three seeds and a larger step budget before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus GPT-2-small domain-mix ratio confirmation
- Success threshold: A middle ratio must beat both 0.0 and 1.0 by at least 10% mean macro held-out loss while preserving a monotonic or near-monotonic target-domain loss improvement trend.
- Stop condition: Stop if the middle-ratio macro advantage disappears in two of three seeds or if real-corpus preprocessing cannot produce comparable held-out splits.

## Evidence references

- Artifact root: `<local-path>/projects/domain-mix-ratio-sweep-for-gpt-2-small-on-local-corpora-469bdce8ffaa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
