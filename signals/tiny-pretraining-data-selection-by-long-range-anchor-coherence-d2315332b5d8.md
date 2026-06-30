# Tiny Pretraining Data Selection by Long-Range Anchor Coherence

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-pretraining-data-selection-by-long-range-anchor-coherence-d2315332b5d8`
Run ID: `tiny-pretraining-data-selection-by-long-range-anchor-coherence-d2315332b5d8-20260603T143951224373+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/93566c73e35a

## What looked useful

Anchor-coherence scoring achieved AUROC 0.9993 for synthetic coherent-document identification versus 0.8611 for repeat count. In the 2000-step persistence check, anchor coherence selected 100% coherent examples and reached 0.543 mean held-out candidate accuracy, compared with 0.3047 for repeat count and 0.1113 for random.

## Boundaries and scale limits

No real corpus, no GPT-2-small-class baseline, no downstream benchmark, no natural-language semantic embeddings, and only two training repeats for the persistence check. The result should be treated as mechanism evidence, not a validated pretraining data-selection method.

## Claim scope

Controlled synthetic corpus only: long-range contextual agreement around repeated anchors selected coherent pretraining documents better than random or distant-repeat-count controls, and improved a tiny causal Transformer's held-out synthetic anchor-attribute candidate ranking after sufficient training steps.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic and controlled; it supports the mechanism but does not validate a real pretraining data-selection method.

## Recommended next action

Run a bounded real-corpus deepen test on a small OpenWebText/Wikipedia-style subset using the same selector, repetition and random controls, and a parameter-matched small Transformer evaluated on held-out LM loss plus entity-consistency probes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus anchor-coherence data selection for a small causal LM
- Success threshold: Anchor-coherence selection improves held-out LM loss by at least 2% relative to both controls and improves entity-consistency probe accuracy by at least 5 percentage points in at least two of three seeds.
- Stop condition: Stop if anchor coherence does not beat both controls on either held-out LM loss or entity-consistency accuracy after the fixed training budget, or if selected examples are dominated by boilerplate/template artifacts.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-pretraining-data-selection-by-long-range-anchor-coherence-d2315332b5d8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
