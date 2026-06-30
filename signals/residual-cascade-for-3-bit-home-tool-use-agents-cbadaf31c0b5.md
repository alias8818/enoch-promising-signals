# Residual cascade for 3-bit home tool-use agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `residual-cascade-for-3-bit-home-tool-use-agents-cbadaf31c0b5`
Run ID: `residual-cascade-for-3-bit-home-tool-use-agents-cbadaf31c0b5-20260524T212401008938+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b3865595438b

## What looked useful

Across five hard synthetic seeds, gated residual-1 matched uniform 4-bit mean accuracy at 3.157 average touched bits, and gated residual-2 slightly exceeded uniform 4-bit mean accuracy at 3.259 average touched bits. Both improved over uniform 3-bit by about 0.2 percentage points.

## Boundaries and scale limits

Synthetic MLP router only; no transformer language model, real tool-call trace, argument-generation metric, quantized kernel latency, energy measurement, or home-device deployment was tested.

## Claim scope

On a deterministic synthetic sparse-prompt tool/argument router, a 3-bit base MLP with validation-selected low-margin 3-bit residual correction matches uniform 4-bit accuracy while touching about 3.16 to 3.26 average weight bits.

## Why it stopped

Proxy-only useful signal: mechanism is supported on synthetic routing, but direct deployed-agent evidence is missing and the effect size is small.

## Recommended next action

Stop this proxy run; run a bounded deepen follow-up on real tool-use traces with a quantized transformer router/head and measured latency or energy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual cascade on real tool-call router traces
- Success threshold: On held-out real traces, gated residual cascade matches uniform 4-bit routing accuracy within 0.1 percentage points while reducing measured latency/energy by at least 10% or average touched weight bits by at least 15%.
- Stop condition: Stop as negative if gated residuals fail to match uniform 4-bit accuracy or if measured latency/energy is not better than uniform 4-bit despite lower average touched bits.

## Evidence references

- Artifact root: `<local-path>/projects/residual-cascade-for-3-bit-home-tool-use-agents-cbadaf31c0b5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
