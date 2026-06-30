# Lookahead/Jacobi self-speculation on GB10 without draft model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `lookahead-jacobi-self-speculation-on-gb10-without-draft-model-211346c80a85`
Run ID: `lookahead-jacobi-self-speculation-on-gb10-without-draft-model-211346c80a85-20260629T094536974883+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d677fc24f5fe

## What looked useful

Jacobi n-gram reuse exists without a draft model: GPT-2 averaged 3.824 tokens per lookahead iteration with 0.321 candidate-token acceptance, and DistilGPT-2 averaged 3.554 tokens per iteration with 0.276 acceptance. However, the unfused prototype achieved only 0.269x and 0.241x of KV-cache greedy throughput respectively because it used 1.844x to 2.051x more model forwards.

## Boundaries and scale limits

Tested only GPT-2-class models, 8 fixed prompts per model, 64 generated tokens per prompt, greedy decoding, fp16 CUDA inference, and an unfused Python/PyTorch prototype. The production fused attention-mask implementation and 7B+ serving-scale behavior were not directly tested.

## Claim scope

On GB10 with cached GPT-2 and DistilGPT-2 checkpoints, a transparent target-model-only Jacobi/lookahead prototype can reproduce full-prefix greedy decoding and generate reusable candidate n-grams, but the unfused implementation is slower than standard KV-cache greedy decoding.

## Why it stopped

Moderate local evidence supports the candidate-reuse mechanism but directly falsifies the practical acceleration claim for a naive unfused implementation; production-fused behavior remains a proxy, not full validation.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should implement or adapt a fused lookahead/verification attention mask on GB10 and require actual speedup over KV-cache greedy, not only an ideal step-count proxy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused lookahead/verification mask for GB10 target-model-only decoding
- Success threshold: At least 1.10x mean wall-clock tokens/s over KV-cache greedy on both GPT-2-class models with 100% equivalence to the declared greedy reference and no prompt-level regressions.
- Stop condition: Stop if fused implementation cannot preserve greedy equivalence, if mean speedup remains below 1.0x after a small parameter sweep, or if memory/attention-mask overhead exceeds the KV-cache baseline by more than 25% on GB10.

## Evidence references

- Artifact root: `<local-path>/projects/lookahead-jacobi-self-speculation-on-gb10-without-draft-model-211346c80a85`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
