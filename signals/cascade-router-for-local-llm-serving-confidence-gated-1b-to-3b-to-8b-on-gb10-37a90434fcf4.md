# Cascade router for local LLM serving: confidence-gated 1B to 3B to 8B on gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cascade-router-for-local-llm-serving-confidence-gated-1b-to-3b-to-8b-on-gb10-37a90434fcf4`
Run ID: `cascade-router-for-local-llm-serving-confidence-gated-1b-to-3b-to-8b-on-gb10-37a90434fcf4-20260621T162158130950+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/02abaca87fa0

## What looked useful

Small-model confidence margins separated correct from wrong answers, and escalating small margin < 2.0 to the 3B tier matched the 7B proxy accuracy while reducing parameter-count cost by 58.0% and measured sequential latency by 33.0%. The strongest standalone tier was 3B, so the original cascade-to-8B mechanism remains unvalidated.

## Boundaries and scale limits

Small 48-example multiple-choice slice; thresholds swept on the evaluation set; 7B code-tuned proxy instead of exact 8B; no real concurrent serving, batching, queueing, resident-model policy, or held-out calibration split.

## Claim scope

On a 48-example ARC-Challenge proxy using local GB10 CUDA inference with Qwen 0.5B, Qwen 3B, and a Qwen 7B code-tuned large proxy, confidence margins were useful for triage and a post-hoc cascade matched large-proxy accuracy with lower average cost/latency; this does not validate the exact 1B-to-3B-to-8B serving claim.

## Why it stopped

Proxy/early bounded result only: exact 8B cache was incomplete, the large tier was replaced by a 7B proxy, and the best no-loss cascade did not call the large proxy.

## Recommended next action

Stop this run as no-paper proxy evidence; next, run a held-out exact-family 1B/3B/8B GB10 serving test if complete models are available.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out exact-family 1B-3B-8B confidence cascade on GB10
- Success threshold: On held-out evaluation, cascade accuracy is at least 99% of 8B-only accuracy while reducing average token compute and p95 latency by at least 25% versus 8B-only serving.
- Stop condition: Stop if exact 8B cannot be loaded locally, if held-out accuracy drops by more than 1% relative to 8B-only at all useful thresholds, or if p95 latency is not improved after accounting for escalation overhead.

## Evidence references

- Artifact root: `<local-path>/projects/cascade-router-for-local-llm-serving-confidence-gated-1b-to-3b-to-8b-on-gb10-37a90434fcf4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
