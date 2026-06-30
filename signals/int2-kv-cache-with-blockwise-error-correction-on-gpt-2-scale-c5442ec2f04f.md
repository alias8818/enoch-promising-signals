# INT2 KV-Cache with Blockwise Error-Correction on GPT-2-Scale

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `int2-kv-cache-with-blockwise-error-correction-on-gpt-2-scale-c5442ec2f04f`
Run ID: `int2-kv-cache-with-blockwise-error-correction-on-gpt-2-scale-c5442ec2f04f-20260619T171433161852+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/06fb855ec8bb

## What looked useful

Residual-mean correction reduced mean KL versus uncorrected INT2 in block sizes 8, 16, and 32, but top-1 agreement remained only 0.67-0.79 and mean KL remained 0.064-0.248 versus the 0.02 threshold. At block size 8, the correction also reduced estimated compression below 2x.

## Boundaries and scale limits

Pretrained GPT-2-small only; short fixed local text corpus; inference-only cache replay; no long-context generation benchmark, no serving latency benchmark, no larger model, no learned correction, and no quantization-aware training.

## Claim scope

On GPT-2-small cached decoding over 576 evaluated next-token positions, simple INT2 per-block min-max KV-cache quantization with a blockwise residual-mean correction slightly reduces KL/logit error but does not preserve next-token distribution fidelity under practical thresholds.

## Why it stopped

Direct bounded GPT-2-small cache-replay evidence is an early falsification of the tested INT2 blockwise residual-mean design, not a full validation or full rejection of all INT2 KV-cache methods.

## Recommended next action

Stop this INT2 residual-mean design as no-paper evidence; any future work should first propose a stronger correction or higher-bit cache scheme and re-run the same GPT-2-small fidelity gate before scaling.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/int2-kv-cache-with-blockwise-error-correction-on-gpt-2-scale-c5442ec2f04f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
