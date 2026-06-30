# Sparse-Mask-Anchored Volunteer Gradient Verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `sparse-mask-anchored-volunteer-gradient-verification-7e193ae7ed2b`
Run ID: `sparse-mask-anchored-volunteer-gradient-verification-7e193ae7ed2b-20260613T194830855904+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7f239e364199

## What looked useful

At 5% anchor plus 5% volunteers across five seeds, anchor_volunteer reached 0.8875 mean cosine to the dense gradient and 0.7885 gradient-energy capture versus 0.2796 and 0.0835 for anchor_random, with final loss 1.6601 versus 2.1589. Budget sweeps at 2%, 5%, and 10% total sparse updates showed the same direction.

## Boundaries and scale limits

The volunteer selection is oracle-style because it uses the full dense gradient before masking; no sparse backpropagation, runtime speedup, real dataset, transformer, language model, or long-horizon validation was tested.

## Claim scope

On a synthetic teacher/student MLP, a fixed sparse anchor mask plus top-absolute-gradient outside-mask volunteer coordinates recovers dense-gradient direction and training progress far better than anchor-only or random-volunteer controls at matched sparse update budgets.

## Why it stopped

Bounded oracle-gradient verification supports the mechanism but is not full validation of a practical sparse training method.

## Recommended next action

Stop this run as no-paper useful signal; next test should replace oracle dense-gradient volunteer selection with a cheap estimator and require matched-budget loss plus gradient-energy evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Non-oracle volunteer gradient estimator for sparse anchors
- Success threshold: At 10% total sparse update budget, the non-oracle estimator must achieve at least 0.70 dense-gradient energy, beat random volunteers by at least 0.20 final loss on the bounded task, and show a plausible compute-saving path versus dense-gradient oracle selection.
- Stop condition: Stop if non-oracle selection stays below 0.50 dense-gradient energy or fails to beat random volunteers on loss in two independent seeds/settings.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-mask-anchored-volunteer-gradient-verification-7e193ae7ed2b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
