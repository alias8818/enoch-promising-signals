# Baseline-Normalized Multi-Model Anchor KV Retention Probe

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `baseline-normalized-multi-model-anchor-kv-retention-probe-c24e2a7999`
Run ID: `baseline-normalized-multi-model-anchor-kv-retention-probe-c24e2a7999-20260529T203813889134+0000`

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

- Parent run decision: Real-Model Exact Anchor KV Retention Probe: enoch://control-plane/projects/real-model-exact-anchor-kv-retention-probe-73b6b05056/runs/real-model-exact-anchor-kv-retention-probe-73b6b05056-20260529T170213155820+0000
- Parent run decision: Exact-Anchor Retrieval Probe for Compressed KV States: enoch://control-plane/projects/exact-anchor-retrieval-probe-for-compressed-kv-states-0289a6dbd66f/runs/exact-anchor-retrieval-probe-for-compressed-kv-states-0289a6dbd66f-20260529T133631049837+0000

## What looked useful

Across 4096 scored prompts, anchor prompts beat no-anchor and wrong-anchor baselines in all four models. Mean paired anchor-minus-no-anchor forced-choice probability lift ranged from +0.0743 to +0.1530, and mean paired anchor-minus-wrong-anchor lift ranged from +0.0818 to +0.1851.

## Boundaries and scale limits

Synthetic color lookup only; small non-instruction models only; no naturalistic QA; no 7B+ models; no contexts beyond about 740 tokens; no internal KV-cache corruption or activation-patching mechanism test; no open-ended generation metric.

## Claim scope

Small pretrained causal LMs (DistilGPT-2, GPT-2, Pythia-70M-deduped, OPT-125M) show baseline-normalized behavioral retention of synthetic key-value color anchors in forced-choice next-token scoring up to about 740 prompt tokens.

## Why it stopped

No-paper useful signal: the behavioral retention effect is reproducible under Tier 2 controls, but the KV mechanism and larger-scale robustness remain unvalidated.

## Recommended next action

Run a bounded deepen follow-up that adds KV-cache or activation-patching corruption of the anchor span and tests whether the baseline-normalized lift collapses, before making any mechanism claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-Intervention Anchor Retention Mechanism Probe
- Success threshold: At least two model families show >=60% collapse of anchor-minus-no-anchor probability lift under selective anchor-span KV corruption, with 95% confidence intervals excluding zero for the original lift and excluding the original lift for the corrupted condition.
- Stop condition: Stop if selective anchor-span KV corruption does not reduce the lift by at least 30% in a smoke run on GPT-2 and Pythia-70M, or if intervention implementation cannot be validated against an equivalent full-prompt scoring check.

## Evidence references

- Artifact root: `<local-path>/projects/baseline-normalized-multi-model-anchor-kv-retention-probe-c24e2a7999`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
