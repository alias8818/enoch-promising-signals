# KV-cache latency validation of persistent n-gram speculative decoding on repeated-session text

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-latency-validation-of-persistent-n-gram-speculati-a8cf91e2c9`
Run ID: `kv-cache-latency-validation-of-persistent-n-gram-speculati-a8cf91e2c9-20260614T122051840285+0000`

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

- Parent run decision: Real-LM validation of persistent n-gram speculative decoding cache: enoch://control-plane/projects/real-lm-validation-of-persistent-n-gram-speculative-decodi-dee9c6db20/runs/real-lm-validation-of-persistent-n-gram-speculative-decodi-dee9c6db20-20260614T110711164916+0000
- Parent run decision: PLD+ persistent cross-session n-gram cache spec decoding: enoch://control-plane/projects/pld-persistent-cross-session-n-gram-cache-spec-decoding-f42555210331/runs/pld-persistent-cross-session-n-gram-cache-spec-decoding-f42555210331-20260614T043041251219+0000

## What looked useful

Persistent n-gram memory reached 77.122% acceptance and 63.416% mean model-call reduction at max_draft=8, while shuffled and transient controls had 0% acceptance. Mean latency was slower than baseline at max_draft=8 (0.932x in the main run) and max_draft=4 (0.583x), with only max_draft=2 showing a small mean speedup (1.043x).

## Boundaries and scale limits

No actual LLM weights, logits, sampling loop, GPU kernel, or production KV-cache serving engine were used; text was synthetic repeated-session replay; CPU block timings are local and noisy.

## Claim scope

On deterministic repeated-session replay text with CPU NumPy KV-like attention verification, persistent n-gram speculation reduces target model-call count substantially but does not produce robust latency speedup except for a narrow max_draft=2 ablation.

## Why it stopped

Tier 2 local evidence supports the persistence mechanism but not robust latency improvement; this is useful no-paper evidence rather than paper-positive validation.

## Recommended next action

Stop this no-paper run; the next bounded deepen test should use an actual small-model KV-cache decoding loop and only proceed if max_draft=2 or adaptive drafting shows at least 1.10x median wall-clock speedup with output identity preserved.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-model KV-cache benchmark for adaptive persistent n-gram speculation
- Success threshold: At least 1.10x median wall-clock speedup over autoregressive baseline with no output mismatches and controls within 2% of baseline speed.
- Stop condition: Stop as negative if actual-model median speedup is below 1.05x or output identity fails under fixed-seed greedy decoding.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-latency-validation-of-persistent-n-gram-speculati-a8cf91e2c9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
