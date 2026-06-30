# Hidden Gradient Puzzle Audits in a Real Training Loop

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `hidden-gradient-puzzle-audits-in-a-real-training-loop-e0239f0774`
Run ID: `hidden-gradient-puzzle-audits-in-a-real-training-loop-e0239f0774-20260523T082006197588+0000`

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

- Parent run decision: Gradient Puzzle Proofs for Volunteer Training Nodes: enoch://control-plane/projects/gradient-puzzle-proofs-for-volunteer-training-nodes-1aca8f1d09c1/runs/gradient-puzzle-proofs-for-volunteer-training-nodes-1aca8f1d09c1-20260523T073915707656+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c86288c1b4e1

## What looked useful

The Tier 1 controlled direct test passed its predefined threshold: leak hidden-gradient top-1 rate 1.0, clean hidden-gradient top-1 rate 0.0, and leak mean ID-OOD gap 0.9619. The hidden feature was top-ranked by the first audit point at step 25 in every leak seed.

## Boundaries and scale limits

Synthetic tabular puzzle, 17 input features, small MLP, 400 steps, five seeds per condition, intentionally simple label-coded shortcut. No language-model, natural-data, long-horizon, multi-shortcut, or adversarially hidden-feature validation was run.

## Claim scope

In a five-seed synthetic binary puzzle trained with a small MLP in a real PyTorch optimizer loop, mean absolute input-gradient audits identified a hidden label-coded shortcut feature as the top-ranked feature in every leak seed and never in clean controls; the leak model also showed a large anti-correlated OOD collapse.

## Why it stopped

Tier 1 direct mechanism evidence met the local success threshold, but the evidence is synthetic small-model support rather than paper-ready validation.

## Recommended next action

Run a bounded deepen follow-up in a small language-model or sequence-classification loop with a canary shortcut token and compare input/embedding-gradient audits against OOD and ablation diagnostics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Canary Shortcut Gradient Audits in a Small Sequence Model
- Success threshold: Leak canary gradient top-1 rate >= 0.8, clean canary top-1 rate <= 0.2, mean leak ID-to-OOD accuracy gap >= 0.25, and canary masking/ablation is top-ranked or causes >= 0.15 loss increase.
- Stop condition: Stop as unsupported if the canary is not top-ranked in at least 4 of 5 leak seeds or if clean controls produce canary top-1 flags in more than 1 of 5 seeds under the same audit.

## Evidence references

- Artifact root: `<local-path>/projects/hidden-gradient-puzzle-audits-in-a-real-training-loop-e0239f0774`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
