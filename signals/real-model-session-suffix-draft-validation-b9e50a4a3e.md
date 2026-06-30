# Real-model session suffix draft validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-model-session-suffix-draft-validation-b9e50a4a3e`
Run ID: `real-model-session-suffix-draft-validation-b9e50a4a3e-20260523T074444492533+0000`

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

- Parent run decision: Session-Ngram Suffix-Tree Speculative Decoding: enoch://control-plane/projects/session-ngram-suffix-tree-speculative-decoding-5f46d4dcd4c3/runs/session-ngram-suffix-tree-speculative-decoding-5f46d4dcd4c3-20260523T054434567893+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/56c9da98cb9d

## What looked useful

GPT-2 session_suffix achieved 3.728x target-pass speedup versus 2.430x static_4gram across 24 cases and 1,152 generated tokens. Qwen2.5-0.5B session_suffix achieved 4.220x versus 2.783x static_4gram across 12 cases and 384 generated tokens. Session_suffix beat static_4gram on all three corpora for both models.

## Boundaries and scale limits

Small causal LMs only; synthetic repeated logs/chat/code corpora; greedy decoding only; no production scheduler, batching, KV-cache movement, natural traffic, stochastic decoding, or end-to-end serving throughput measurement.

## Claim scope

In a bounded Tier-1 direct test on synthetic repeated session corpora, an online session-local suffix cache produced draft tokens that GPT-2 and Qwen2.5-0.5B accepted under exact greedy verification often enough to reduce target-model passes versus no-draft and static 4-gram controls.

## Why it stopped

This run satisfies the Tier-1 controlled small direct-test threshold and supports the mechanism, but the evidence is synthetic/small-model and not sufficient for paper or deployment claims.

## Recommended next action

Run one bounded deepen validation on natural repeated agent/code sessions inside a serving-style loop, measuring end-to-end tokens/s, scheduler overhead, target-pass reduction, and exact-output quality versus no-draft and static n-gram baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Serving-style session suffix drafting on natural repeated traces
- Success threshold: At least 1.25x end-to-end tokens/s improvement over no-draft and at least 1.10x over static n-gram on natural traces, with exact greedy-output equivalence and nonnegative result on at least two trace domains.
- Stop condition: Stop negative if target-pass savings disappear after scheduler/lookup overhead, if static n-gram matches or beats session suffix on natural traces, or if exact-output equivalence fails.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-session-suffix-draft-validation-b9e50a4a3e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
