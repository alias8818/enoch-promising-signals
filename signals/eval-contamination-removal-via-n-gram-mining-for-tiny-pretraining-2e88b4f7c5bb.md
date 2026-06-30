# Eval Contamination Removal via N-gram Mining for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `eval-contamination-removal-via-n-gram-mining-for-tiny-pretraining-2e88b4f7c5bb`
Run ID: `eval-contamination-removal-via-n-gram-mining-for-tiny-pretraining-2e88b4f7c5bb-20260609T162910714068+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/000e22f99bde

## What looked useful

Exact n-gram mining cleanly removed injected eval contamination and raised eval loss versus contaminated training by a mean 0.167 nats while keeping validation loss close to oracle-clean; continuation accuracy also dropped back toward oracle-clean.

## Boundaries and scale limits

Synthetic documents, exact-span contamination, deliberate benchmark canaries, three seeds, 300 training steps per tiny Transformer, no real benchmark or web-scale corpus; does not test paraphrase/semantic contamination or GPT-2-small-class scale.

## Claim scope

In a deterministic synthetic tiny-pretraining setup with exact injected eval-span contamination, 20-gram document filtering removed the injected documents and reversed contamination-driven improvements in eval loss and continuation accuracy across three seeds.

## Why it stopped

Bounded synthetic evidence supports the mechanism but is not direct or broad enough for a paper; stop as no-paper useful signal rather than over-claiming.

## Recommended next action

Run the same three-way contaminated/mined/oracle control on a real small text corpus with real held-out benchmark snippets and an n-gram threshold sweep.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus n-gram decontamination threshold sweep for tiny GPT pretraining
- Success threshold: A threshold removes at least 95% of exact injected contamination with under 5% clean-document false positives and reduces contaminated eval-loss gain by at least 50% without increasing clean validation loss by more than 0.05 nats.
- Stop condition: Stop if no threshold reaches both contamination-removal and false-positive targets, or if mined-clean training harms clean validation loss more than it reduces contaminated eval advantage.

## Evidence references

- Artifact root: `<local-path>/projects/eval-contamination-removal-via-n-gram-mining-for-tiny-pretraining-2e88b4f7c5bb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
