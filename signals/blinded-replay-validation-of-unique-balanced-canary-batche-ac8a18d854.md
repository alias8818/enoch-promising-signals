# Blinded Replay Validation of Unique Balanced Canary Batches

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `blinded-replay-validation-of-unique-balanced-canary-batche-ac8a18d854`
Run ID: `blinded-replay-validation-of-unique-balanced-canary-batche-ac8a18d854-20260621T010525075936+0000`

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

- Parent run decision: Canary-Embedded Batches for Cheating-Resistant Volunteer Training Validation: enoch://control-plane/projects/canary-embedded-batches-for-cheating-resistant-volunteer-training-validation-efc31d6b462e/runs/canary-embedded-batches-for-cheating-resistant-volunteer-training-validation-efc31d6b462e-20260621T004722092264+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/871b7fc1a29f

## What looked useful

Balanced unique canary batches are a viable local validation pattern for memory correction and distractor resistance. Layered status-aware memory passed the scoped threshold while transcript search and flat retrieval failed on stale assignments or distractors.

## Boundaries and scale limits

Synthetic corpus, one seed, 32 held-out replay queries, deterministic strategy simulators, no live LLM agent loop, no naturalistic operator traces, and no multi-session persistence stress test.

## Claim scope

In a deterministic Tier 1 synthetic replay with 32 unique canary subjects, four balanced final labels, corrections, and explicit distractors, typed/layered memory recovered confirmed canary tuples with 100% exact accuracy and exceeded the best non-layered baseline by 50 percentage points.

## Why it stopped

Tier 1 direct controlled test completed with useful mechanism support, but the evidence is synthetic and simulator-based rather than publication-grade live-agent validation.

## Recommended next action

Run a bounded live-agent replay using the same balanced canary design across at least 5 seeds and compare layered memory against transcript and flat retrieval with exact tuple accuracy and leakage diagnostics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-Agent Balanced Canary Replay With Correction and Distractor Ablations
- Success threshold: Layered live-agent memory exact accuracy >= 0.85, gap versus best baseline >= 0.30, per-label accuracy standard deviation <= 0.10, and no canary-code duplication or answer leakage in blinded queries.
- Stop condition: Stop as negative if layered memory is below 0.75 exact accuracy on two or more seeds or if the gap versus the best baseline is below 0.15 after all seeds.

## Evidence references

- Artifact root: `<local-path>/projects/blinded-replay-validation-of-unique-balanced-canary-batche-ac8a18d854`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
