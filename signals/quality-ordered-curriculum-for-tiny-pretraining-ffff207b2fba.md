# Quality-Ordered Curriculum for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quality-ordered-curriculum-for-tiny-pretraining-ffff207b2fba`
Run ID: `quality-ordered-curriculum-for-tiny-pretraining-ffff207b2fba-20260620T141732388586+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1a95450465bc

## What looked useful

Quality ordering by itself is not enough in a one-pass tiny-LM setting: early high-quality-first gains reverse after training on low-quality examples, and final clean-domain gains from low-to-high appear to be a recency/domain-focus tradeoff.

## Boundaries and scale limits

No real corpus, tokenizer, transformer, GPU training, GPT-2-small-class baseline, or downstream evaluation. Evidence is useful for mechanism triage but not publication-grade pretraining validation.

## Claim scope

Synthetic tiny-pretraining mechanism probe using a NumPy log-bilinear causal LM and generated quality-labeled text. Naive high-quality-first ordering is harmful after the low-quality tail is consumed; low-to-high improves clean validation NLL but worsens mixed validation NLL.

## Why it stopped

Proxy/synthetic evidence falsifies the naive high-quality-first ordering as a final-quality improvement in this local setting, but does not fully validate or reject large-scale curriculum pretraining.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should evaluate quality-first warmup followed by random replay or quality-weighted sampling on a tiny transformer with real text.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay-stabilized quality curriculum for tiny transformer pretraining
- Success threshold: Quality-first-then-replay improves clean validation NLL by at least 3% versus random while keeping mixed validation NLL within 1% of random across at least 3 seeds.
- Stop condition: Stop if the replay-stabilized schedule fails to beat random on clean validation or worsens mixed validation NLL by more than 1% in a small transformer pilot.

## Evidence references

- Artifact root: `<local-path>/projects/quality-ordered-curriculum-for-tiny-pretraining-ffff207b2fba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
