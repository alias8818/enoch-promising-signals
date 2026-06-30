# 1-bit agent ledger with residual confidence

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `1-bit-agent-ledger-with-residual-confidence-091ea3c78b43`
Run ID: `1-bit-agent-ledger-with-residual-confidence-091ea3c78b43-20260525T031750991242+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d6ad506a8a39

## What looked useful

A quantized aggregate residual can make a one-bit-per-agent ledger behave nearly like full soft aggregation for binary synthetic ensembles; 6 bits was enough in this sweep, giving about 22.8x mean compression versus float32 per-agent confidence storage. This supports a bounded compression mechanism but not a paper-ready real-agent claim.

## Boundaries and scale limits

Synthetic only: 8-32 agents, 4000 cases per configuration, 5 seeds, binary labels, non-strategic simulated confidence. No real LLM traces, multi-class tasks, adversarial confidence, cryptographic ledger implementation, or production online-update behavior were tested.

## Claim scope

In dependency-free synthetic binary multi-agent classification sweeps, storing one vote bit per agent plus a 6- to 8-bit aggregate residual confidence scalar per case preserved full soft-confidence aggregation metrics within 0.002 AUROC and 0.002 Brier across all tested paired settings, while pure one-bit majority did not.

## Why it stopped

No-paper closure: evidence is synthetic and mechanism-level only; it supports a useful compression signal but lacks real-agent and production-ledger validation.

## Recommended next action

Run a bounded real-trace confirmation using public or locally generated multi-agent outputs with raw confidence scores, comparing full soft aggregation, one-bit majority, and 4/6/8-bit aggregate residual ledgers under calibration and distribution-shift diagnostics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace confirmation of one-bit agent ledger residual compression
- Success threshold: 6- or 8-bit residual ledger is within 0.005 AUROC and 0.005 Brier of full soft aggregation on the main real-trace benchmark and beats one-bit majority Brier by at least 0.005.
- Stop condition: Stop if residual ledgers fail to beat one-bit majority calibration by 0.005 Brier or require more than 8 residual bits to stay within 0.005 of full soft aggregation.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-agent-ledger-with-residual-confidence-091ea3c78b43`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
