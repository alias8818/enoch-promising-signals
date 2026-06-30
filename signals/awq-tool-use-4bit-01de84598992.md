# AWQ Tool-Use 4bit

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `awq-tool-use-4bit-01de84598992`
Run ID: `awq-tool-use-4bit-01de84598992-20260530T090313450295+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3158d7e70227

## What looked useful

Activation-aware int4 quantization is worth testing for tool-routing preservation, but this probe did not show a material advantage for tool-use-specific calibration over generic activation calibration.

## Boundaries and scale limits

Synthetic router only; no real LLM, tokenizer, tool-call JSON, argument accuracy, multi-step task success, production traces, or optimized AWQ kernels were evaluated.

## Claim scope

In a synthetic 24-tool linear router with sparse intent features, AWQ-style activation-aware int4 scaling reduced logit MSE by about 84-85% versus naive groupwise int4 and improved reference top-1 agreement by about 6-7 percentage points over 10 seeds.

## Why it stopped

Synthetic/proxy evidence supports activation-aware int4 over naive int4 but does not validate end-to-end LLM tool use, and tool-specific calibration was not materially better than generic calibration.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should evaluate a real small instruction/tool-use model with held-out tool-call traces and compare naive int4, generic-calibrated AWQ, tool-trace-calibrated AWQ, and FP16/BF16.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Small-Model AWQ Tool-Call Trace Evaluation
- Success threshold: Tool-trace-calibrated AWQ must recover at least 95% of FP16/BF16 tool selection accuracy and improve JSON/argument accuracy by at least 3 percentage points over generic-calibrated AWQ on held-out traces.
- Stop condition: Stop if tool-trace-calibrated AWQ is within +/-1 percentage point of generic-calibrated AWQ on tool selection and JSON/argument accuracy, or if both int4 variants fall below 90% of FP16/BF16 tool selection accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/awq-tool-use-4bit-01de84598992`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
