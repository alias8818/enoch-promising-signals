# Real-corpus n-gram decontamination threshold sweep for tiny GPT pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-corpus-n-gram-decontamination-threshold-sweep-for-tin-37783afa42`
Run ID: `real-corpus-n-gram-decontamination-threshold-sweep-for-tin-37783afa42-20260609T210205434729+0000`

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

- Parent run decision: Eval Contamination Removal via N-gram Mining for Tiny Pretraining: enoch://control-plane/projects/eval-contamination-removal-via-n-gram-mining-for-tiny-pretraining-2e88b4f7c5bb/runs/eval-contamination-removal-via-n-gram-mining-for-tiny-pretraining-2e88b4f7c5bb-20260609T162910714068+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/000e22f99bde

## What looked useful

Across seeds 37783 and 37784, no-filter retained 72 injected contaminant documents and achieved mean contaminated-heldout loss 2.0076. Thresholds 0.10 and 0.20 removed all 72 contaminants with zero natural-document removals in both seeds, raised contaminated-heldout loss by about 0.0326 nats, and changed clean validation loss by only +0.0005 nats versus no filter.

## Boundaries and scale limits

Small corpus, exact injected contamination, two seeds, byte-level tiny GPT, no organic web-scale contamination labels, no near-duplicate/paraphrase contamination, no GPT-2-small-class or larger model validation.

## Claim scope

Controlled WikiText-2 exact-copy contamination test with a tiny byte-level GPT: 13-word-gram overlap thresholds from 0.10 to 0.20 removed all injected held-out validation passages while preserving clean validation loss across two 1,500-step seeds.

## Why it stopped

Tier 1 controlled direct test completed and produced useful mechanism evidence, but it is not paper-positive because contamination was exact injected real text in a tiny WikiText-2 byte-GPT setting.

## Recommended next action

Run a bounded deepen test with real near-duplicate and lightly paraphrased held-out passages to determine whether the 0.10-0.20 exact-copy threshold range remains effective beyond exact overlap.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Near-duplicate real-corpus n-gram decontamination threshold sweep for tiny GPT pretraining
- Success threshold: At least one threshold in 0.10-0.20 removes 90% or more of near-duplicate contaminant documents, removes less than 1% of natural documents, increases contaminated-heldout loss versus no-filter, and keeps clean validation loss within 0.01 nats of no-filter in both seeds.
- Stop condition: Stop as a negative/deprioritized path if all thresholds that remove 90% or more of near-duplicate contamination also remove 1% or more natural documents or degrade clean validation loss by more than 0.01 nats in both seeds.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-n-gram-decontamination-threshold-sweep-for-tin-37783afa42`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
