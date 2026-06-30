# Natural-Language Agent Trace Replay for Anchor-Gated Eviction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `natural-language-agent-trace-replay-for-anchor-gated-evict-42ffed7607`
Run ID: `natural-language-agent-trace-replay-for-anchor-gated-evict-42ffed7607-20260524T224141540894+0000`

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

- Parent run decision: Anchor-Gated Eviction for Long-Context Small Agents: enoch://control-plane/projects/anchor-gated-eviction-for-long-context-small-agents-dbb1e0867935/runs/anchor-gated-eviction-for-long-context-small-agents-dbb1e0867935-20260524T222130936983+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/500874881783

## What looked useful

Anchor-gated eviction reached 0.9619 anchor-query accuracy on explicit anchor traces versus 0.0044 for LRU and 0.5556 for soft salience, but dropped to 0.4594 on paraphrased anchor traces and missed the 15 percentage point oracle-gap threshold.

## Boundaries and scale limits

Small deterministic CPU-only benchmark with generated traces, lexical anchor detection, no real production agent logs, no LLM/human-labeled anchor extraction, and no long-horizon multi-session workflows.

## Claim scope

Controlled synthetic natural-language trace replay with fixed memory capacity shows anchor-gated eviction preserves future-critical facts when anchor cues are lexically recognizable.

## Why it stopped

Controlled Tier 1 evidence supports the eviction mechanism only when anchor cues are recognizable; paraphrase brittleness makes this no-paper useful signal rather than paper-positive validation.

## Recommended next action

Run a bounded deepen follow-up using a small hand-labeled or LLM-labeled trace corpus to test whether robust anchor detection closes the paraphrase gap while preserving the replay accuracy gains.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robust Anchor Detection for Natural-Language Trace Replay
- Success threshold: On paraphrased traces, anchor-gated replay with robust detector achieves anchor-query accuracy >= 0.85, improves by >= 25 percentage points over LRU, and is within 15 percentage points of oracle anchor labels.
- Stop condition: Stop if detector F1 is below 0.80 or replay anchor-query accuracy remains below 0.70 after one bounded detector iteration, because the eviction mechanism is then bottlenecked by anchor recognition.

## Evidence references

- Artifact root: `<local-path>/projects/natural-language-agent-trace-replay-for-anchor-gated-evict-42ffed7607`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
