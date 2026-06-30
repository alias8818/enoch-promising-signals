# Int4 quantized agent for home tool-use reliability

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int4-quantized-agent-for-home-tool-use-reliability-6f45e25f5776`
Run ID: `int4-quantized-agent-for-home-tool-use-reliability-6f45e25f5776-20260609T173702743645+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/57caa9d46515

## What looked useful

Competence-controlled synthetic run passed: FP32 mean accuracy 1.000, int4 per-channel mean accuracy 1.000, delta 0.000, no-op int4 accuracy 1.000, induced errors mean 0.0. Held-out phrasing failed: FP32 mean accuracy 0.566, int4 per-channel mean accuracy 0.566, no-op int4 accuracy 0.206.

## Boundaries and scale limits

Synthetic text commands only; small classifier-style policy, not a pretrained instruction LLM; no real Home Assistant traces, speech input, long-horizon planning, tool execution, latency/load testing, or human home deployment. Held-out paraphrase reliability was poor for FP32 and int4, so broader reliability remains unvalidated.

## Claim scope

On a synthetic smart-home command-to-tool-call benchmark with a small PyTorch policy, post-training symmetric int4 quantization preserved exact tool-call accuracy in the in-distribution condition where FP32 reached 100% accuracy across 5 seeds; it did not establish robust home-agent reliability under held-out paraphrases.

## Why it stopped

Mixed proxy evidence: int4 itself did not harm a competent in-distribution synthetic policy, but the broader home tool-use reliability claim failed on held-out paraphrases and was not tested on a real LLM or real home traces.

## Recommended next action

Stop this worker run as a no-paper useful signal; next bounded direct test should compare FP16/BF16 versus int4 on a small pretrained instruction model using real or realistic Home Assistant tool-call traces with paraphrase and no-op safety splits.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small pretrained Home Assistant int4 tool-call reliability evaluation
- Success threshold: FP16/BF16 exact-call accuracy at least 95%; int4 exact-call delta no worse than -1 percentage point in-distribution and no worse than -2 points on paraphrase/no-op splits; invalid JSON rate not increased by more than 0.5 points.
- Stop condition: Stop if the FP16/BF16 baseline is below 90% exact-call accuracy, if int4 causes more than a 5-point exact-call drop, or if no real/realistic Home Assistant trace set can be assembled locally.

## Evidence references

- Artifact root: `<local-path>/projects/int4-quantized-agent-for-home-tool-use-reliability-6f45e25f5776`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
