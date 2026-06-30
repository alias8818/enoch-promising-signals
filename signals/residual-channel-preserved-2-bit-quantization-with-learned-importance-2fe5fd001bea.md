# Residual-Channel-Preserved 2-bit Quantization with Learned Importance

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `residual-channel-preserved-2-bit-quantization-with-learned-importance-2fe5fd001bea`
Run ID: `residual-channel-preserved-2-bit-quantization-with-learned-importance-2fe5fd001bea-20260525T164011478786+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ff62eb26f6d5

## What looked useful

Residual-norm channel preservation won all 12 seed/fraction comparisons by output MSE. At 12.5% preserved rows it improved mean output MSE versus fp32 from 5.5702 for plain 2-bit to 4.6005 and mean accuracy from 0.5984 to 0.6141. Learned importance improved over plain 2-bit but lost to residual-norm preservation at every tested fraction.

## Boundaries and scale limits

Synthetic teacher classification only; residual MLP only; no transformer or language-model perplexity; preserved channels were stored as fp32 rows, raising average weight bits from 2.0 to 2.924, 3.875, or 5.750 depending on the preserved fraction.

## Claim scope

In a four-seed synthetic residual-MLP post-training quantization probe, preserving selected output channels improves plain 2-bit quantization, but the tested learned relaxed-gate importance selector does not outperform a simple residual-norm channel selector.

## Why it stopped

Bounded proxy evidence is mixed/negative for the learned-importance claim: channel preservation helps, but the learned selector loses to a cheaper residual-norm heuristic and the fp32 preserved rows exceed a strict 2-bit average-weight budget.

## Recommended next action

Stop this no-paper run; any future work should first make the learned selector beat residual-norm preservation under the same residual-MLP protocol before spending transformer-scale compute.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-preserved-2-bit-quantization-with-learned-importance-2fe5fd001bea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
