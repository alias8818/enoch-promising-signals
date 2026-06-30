# Direct small-model latency test for prompt-lookback speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-small-model-latency-test-for-prompt-lookback-specul-a611ba1ecf`
Run ID: `direct-small-model-latency-test-for-prompt-lookback-specul-a611ba1ecf-20260602T170516078697+0000`

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

- Parent run decision: Speculative Decoding via Prompt-Lookback: enoch://control-plane/projects/speculative-decoding-via-prompt-lookback-b05211646b1e/runs/speculative-decoding-via-prompt-lookback-b05211646b1e-20260602T124853469694+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7195814c2f2d

## What looked useful

Prompt-lookback showed 1.59x to 2.71x median speedup on exact runs but exact-match rates were only 50% for prompt_lookup_4 and 25% for prompt_lookup_8. The small-assistant path was exact on all runs but about 4.4x slower than baseline greedy decoding.

## Boundaries and scale limits

Single small target model, one tiny assistant model, four synthetic repeated prompts, 20 measured runs per variant, one hardware/software stack; no larger model, serving-batch, long-context, or broad task validation.

## Claim scope

On a GB10 worker with distilgpt2, repeated-prefix prompts, deterministic greedy generation, and Transformers 4.57.6, prompt-lookback speculative decoding can reduce latency on exact-match prompts, but it did not consistently preserve greedy output or new-token cap behavior; the tiny assistant-model path preserved output but was slower than greedy.

## Why it stopped

Tier 1 direct local test produced mixed evidence: prompt-lookback has a speed mechanism but fails exactness/cap reliability in this setup, while the small-assistant speculative path directly failed the latency threshold by running slower than greedy.

## Recommended next action

Stop this run as no-paper useful signal; deepen only if the next test directly diagnoses prompt-lookback token-cap/output divergence and requires exact greedy-equivalent output as the success threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exactness-controlled prompt-lookback latency benchmark
- Success threshold: 100% exact token agreement and token-cap compliance with at least 1.3x median latency speedup and no p95 latency regression versus greedy on the repeated-prefix prompt set.
- Stop condition: Stop as negative if exactness or token-cap compliance falls below 100%, or if median speedup is below 1.3x after controlling for exact output.

## Evidence references

- Artifact root: `<local-path>/projects/direct-small-model-latency-test-for-prompt-lookback-specul-a611ba1ecf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
