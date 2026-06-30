# Tiny CPU router cascade for local GPT-2-small vs micro-LM serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-cpu-router-cascade-for-local-gpt-2-small-vs-micro-lm-serving-9d3bddb6bf74`
Run ID: `tiny-cpu-router-cascade-for-local-gpt-2-small-vs-micro-lm-serving-9d3bddb6bf74-20260603T193051103918+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/de04c27d0779

## What looked useful

The tiny model was about 15.26x faster per generated token, but mean continuation NLL was 9.74 versus 3.57 for GPT-2-small. Quality-preserving thresholds routed at least 95.83% of examples to GPT-2-small and were slower than the baseline; a 1.0 NLL degradation gave only 1.01x expected speedup.

## Boundaries and scale limits

Small handcrafted prompt suite; tiny-gpt2 checkpoint is a toy/micro proxy, not a production-trained micro-LM; no concurrency, batching, KV-cache serving, trained router, real traffic, or human/task quality evaluation.

## Claim scope

On a 24-example handcrafted local prompt suite using int8 ONNX GPT-2-small and int8 ONNX tiny-gpt2 on an 8-CPU worker, a raw entropy threshold over the tiny model does not provide a useful quality-preserving cascade in front of GPT-2-small.

## Why it stopped

Early bounded proxy falsification: the tested naive tiny-model entropy cascade cannot preserve GPT-2-small continuation quality without routing almost all traffic to GPT-2-small, so latency gains disappear.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should replace the toy tiny-gpt2 with a trained/distilled micro-LM and evaluate a held-out trained router under cached decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated CPU cascade with a trained micro-LM and held-out router
- Success threshold: Held-out micro accept rate >=25%, mean NLL delta versus GPT-2-small <=0.25, and expected cached-decoding latency speedup >=1.25x.
- Stop condition: Stop if the calibrated router cannot reach 10% accepted prompts under <=0.25 mean NLL delta or if the micro prepass overhead keeps speedup below 1.10x.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-cpu-router-cascade-for-local-gpt-2-small-vs-micro-lm-serving-9d3bddb6bf74`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
