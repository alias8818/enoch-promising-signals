# Real GPT-2 Decoder Test for Rolling N-gram Cache Lookahead

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-gpt-2-decoder-test-for-rolling-n-gram-cache-lookahead-0bd3406942`
Run ID: `real-gpt-2-decoder-test-for-rolling-n-gram-cache-lookahead-0bd3406942-20260529T161110896893+0000`

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

- Parent run decision: Rolling N-gram Cache Lookahead: enoch://control-plane/projects/rolling-n-gram-cache-lookahead-29c12306aaed/runs/rolling-n-gram-cache-lookahead-29c12306aaed-20260529T081713137906+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5c0c56bfae25

## What looked useful

The mechanism cleared the predefined useful-signal threshold: 57.75% of generated tokens were accepted from GPT-2-verified cache proposals and estimated decoder calls fell from 1,536 baseline calls to 821 verification calls.

## Boundaries and scale limits

Single model (gpt2/GPT-2-small), single corpus split, 24 prompts, 1,536 generated tokens, greedy decoding only, Python reference implementation, and call-count speedup estimate rather than optimized serving latency.

## Claim scope

In a small direct GPT-2-small greedy decoding simulation on 24 WikiText-2 validation prompts, a rolling n-gram cache built only from visible prompt and accepted generated tokens reduced exact decoder verification calls by 46.55% while preserving plain greedy output on the first three baseline-checked prompts.

## Why it stopped

Tier 1 small direct validation produced useful mechanism support but not publication-grade breadth, robustness, or serving-speed evidence.

## Recommended next action

Run a bounded medium confirmation with more prompts, at least one additional GPT-2-family model, an ablated/randomized proposal control, and measured wall-clock latency in an integrated speculative verification path.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium GPT-2-family confirmation for rolling n-gram lookahead
- Success threshold: At least 20% exact decoder-call reduction, at least 15% wall-clock latency reduction versus plain greedy decoding, zero exactness mismatches in audited greedy checks, and clear improvement over randomized proposal controls.
- Stop condition: Stop as unsupported if call reduction falls below 10%, wall-clock latency is not improved, or any unexplained exact greedy mismatch appears.

## Evidence references

- Artifact root: `<local-path>/projects/real-gpt-2-decoder-test-for-rolling-n-gram-cache-lookahead-0bd3406942`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
