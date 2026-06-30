# Length Stratification Cuts Padding Waste in CPU Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `length-stratification-cuts-padding-waste-in-cpu-pretraining-f8a7a51138a4`
Run ID: `length-stratification-cuts-padding-waste-in-cpu-pretraining-f8a7a51138a4-20260601T053711338734+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/aa233e0bb664

## What looked useful

Across three measured seeds, random batching averaged 64.19% padding and 8040 real tokens/s, while stratified batching averaged 1.68% padding and 36642 real tokens/s, a 97.38% relative padding-fraction reduction and 4.56x real-token throughput speedup in this CPU proxy.

## Boundaries and scale limits

Synthetic corpus only; forward pass only; no backward/optimizer step, no real text dataset, no validation loss, no production shuffled-bucket policy, and no large-scale pretraining run.

## Claim scope

In a bounded NumPy CPU transformer-forward proxy on synthetic heavy-tailed sequence lengths, sorted length stratification reduced padding slots and improved measured real-token throughput versus random batching.

## Why it stopped

No-paper useful signal: the mechanism is supported by a synthetic forward-only proxy, but direct full-training evidence is still required before making a paper-level pretraining claim.

## Recommended next action

Run a bounded full forward+backward CPU training experiment on a real tokenized corpus comparing random batching with shuffled length buckets, reporting padding, wall time, memory, and validation loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus CPU training test of shuffled length buckets
- Success threshold: At least 25% padding-slot reduction and at least 15% real-token/s improvement with validation loss within one standard deviation of the random-batching baseline.
- Stop condition: Stop if shuffled length buckets improve throughput by less than 10% or worsen validation loss by more than one standard deviation across repeated seeds.

## Evidence references

- Artifact root: `<local-path>/projects/length-stratification-cuts-padding-waste-in-cpu-pretraining-f8a7a51138a4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
